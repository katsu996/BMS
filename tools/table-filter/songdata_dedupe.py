"""songdata.db の sha256 重複を整理し、beatoraja のフォルダ SONG COUNT と一致させる。"""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from dataclasses import dataclass
from typing import Sequence

_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_MD5_RE = re.compile(r"^[0-9a-f]{32}$")


@dataclass(frozen=True)
class SongdataDedupeReport:
    duplicate_sha256_groups: int
    rows_removed: int
    rows_before: int
    rows_after: int


@dataclass(frozen=True)
class SongdataLookupCount:
    """beatoraja の HashBar → getSongDatas() 相当の件数。"""

    lookup_rows: int
    unique_sha256: int


def normalize_sha256(raw: object) -> str | None:
    if raw is None:
        return None
    s = str(raw).strip().lower()
    return s if _SHA256_RE.fullmatch(s) else None


def normalize_md5(raw: object) -> str | None:
    if raw is None:
        return None
    s = str(raw).strip().lower()
    return s if _MD5_RE.fullmatch(s) else None


def hash_for_beatoraja_lookup(row: dict) -> str | None:
    """
    beatoraja HashBar の elementsHash と同じ優先順位:
    sha256 があれば sha256、無ければ md5。
    """
    sha = normalize_sha256(row.get("sha256"))
    if sha:
        return sha
    return normalize_md5(row.get("md5"))


def _where_hashes_clause(hashes: Sequence[str]) -> str:
    """beatoraja getSongDatas と同じ OR 句（空の IN () は偽）。"""
    md5_parts: list[str] = []
    sha_parts: list[str] = []
    for h in hashes:
        if len(h) > 32:
            sha_parts.append("'" + h + "'")
        else:
            md5_parts.append("'" + h + "'")
    clauses: list[str] = []
    if md5_parts:
        clauses.append("md5 IN (" + ",".join(md5_parts) + ")")
    if sha_parts:
        clauses.append("sha256 IN (" + ",".join(sha_parts) + ")")
    if not clauses:
        return "0"
    return " OR ".join(clauses)


def count_beatoraja_songdata_lookup(db_path: str, hashes: Sequence[str]) -> SongdataLookupCount:
    """
    beatoraja SQLiteSongDatabaseAccessor.getSongDatas(String[] hashes) と同型の
    WHERE md5 IN (...) OR sha256 IN (...) のヒット行数を数える。
    """
    if not hashes:
        return SongdataLookupCount(lookup_rows=0, unique_sha256=0)
    where = _where_hashes_clause(list(hashes))
    sql = f"SELECT sha256 FROM song WHERE {where}"
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
    finally:
        con.close()
    lookup_rows = len(rows)
    unique_sha256 = len({normalize_sha256(r[0]) for r in rows if normalize_sha256(r[0])})
    return SongdataLookupCount(lookup_rows=lookup_rows, unique_sha256=unique_sha256)


def lookup_counts_by_level(
    rows: Sequence[dict],
    db_path: str,
    *,
    level_field: str = "level",
) -> dict[str, SongdataLookupCount]:
    """レベルごとに beatoraja フォルダ SONG COUNT（lookup）と一意 sha256 件数を返す。"""
    by_level: dict[str, list[str]] = {}
    for row in rows:
        lv = row.get(level_field)
        if lv is None:
            continue
        key = str(lv).strip()
        if not key:
            continue
        h = hash_for_beatoraja_lookup(row)
        if h:
            by_level.setdefault(key, []).append(h)
    out: dict[str, SongdataLookupCount] = {}
    for lv, hashes in by_level.items():
        out[lv] = count_beatoraja_songdata_lookup(db_path, hashes)
    return out


def count_duplicate_sha256_groups(db_path: str) -> tuple[int, int]:
    """(重複 sha256 グループ数, 削除対象行数) を返す。"""
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        cur = con.cursor()
        cur.execute(
            """
            SELECT LOWER(TRIM(sha256)) AS s, COUNT(*) AS c
            FROM song
            WHERE sha256 IS NOT NULL AND LENGTH(TRIM(sha256)) >= 64
            GROUP BY LOWER(TRIM(sha256))
            HAVING COUNT(*) > 1
            """
        )
        groups = cur.fetchall()
    finally:
        con.close()
    extra = sum(int(c) - 1 for _, c in groups)
    return len(groups), extra


def dedupe_songdata_db(db_path: str, *, dry_run: bool = False) -> SongdataDedupeReport:
    """
    同一 sha256 の song 行を 1 件にまとめる（rowid 最小を残す）。
    beatoraja は getSongDatas で重複行をすべて返すが、選曲一覧は sha256 で潰すため、
    重複 DB 行があると SONG COUNT だけが水増しになる。
    """
    con = sqlite3.connect(db_path)
    try:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM song")
        before = int(cur.fetchone()[0])
        groups, extra = count_duplicate_sha256_groups(db_path)
        if extra == 0:
            return SongdataDedupeReport(
                duplicate_sha256_groups=0,
                rows_removed=0,
                rows_before=before,
                rows_after=before,
            )
        if dry_run:
            return SongdataDedupeReport(
                duplicate_sha256_groups=groups,
                rows_removed=extra,
                rows_before=before,
                rows_after=before - extra,
            )
        cur.execute(
            """
            DELETE FROM song
            WHERE sha256 IS NOT NULL AND LENGTH(TRIM(sha256)) >= 64
              AND rowid NOT IN (
                SELECT MIN(rowid)
                FROM song
                WHERE sha256 IS NOT NULL AND LENGTH(TRIM(sha256)) >= 64
                GROUP BY LOWER(TRIM(sha256))
              )
            """
        )
        removed = cur.rowcount if cur.rowcount is not None and cur.rowcount >= 0 else extra
        con.commit()
        cur.execute("SELECT COUNT(*) FROM song")
        after = int(cur.fetchone()[0])
        return SongdataDedupeReport(
            duplicate_sha256_groups=groups,
            rows_removed=removed,
            rows_before=before,
            rows_after=after,
        )
    finally:
        con.close()


def main() -> int:
    ap = argparse.ArgumentParser(
        description="songdata.db の sha256 重複を除去（beatoraja フォルダ SONG COUNT 用）"
    )
    ap.add_argument("--db", default="songdata.db", help="songdata.db のパス")
    ap.add_argument("--dry-run", action="store_true", help="削除せず件数のみ表示")
    args = ap.parse_args()
    db = args.db
    if not __import__("os").path.isfile(db):
        print(f"エラー: {db} がありません。", file=sys.stderr)
        return 1
    groups, extra = count_duplicate_sha256_groups(db)
    if extra == 0:
        print(f"{db}: sha256 重複はありません。")
        return 0
    report = dedupe_songdata_db(db, dry_run=args.dry_run)
    verb = "削除予定" if args.dry_run else "削除"
    print(
        f"{db}: sha256 重複グループ {report.duplicate_sha256_groups} 件、"
        f"{verb}行数 {report.rows_removed}（{report.rows_before} → {report.rows_after}）"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
