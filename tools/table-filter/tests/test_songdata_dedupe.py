"""songdata_dedupe のユニットテスト。"""

from __future__ import annotations

import sqlite3
import tempfile
import unittest
from pathlib import Path

from songdata_dedupe import (
    count_beatoraja_songdata_lookup,
    dedupe_songdata_db,
    hash_for_beatoraja_lookup,
    lookup_counts_by_level,
)

SHA_A = "a" * 64
SHA_B = "b" * 64
MD5_A = "c" * 32


def _make_db(path: Path) -> None:
    con = sqlite3.connect(path)
    try:
        con.execute(
            "CREATE TABLE song ("
            "md5 TEXT, sha256 TEXT, title TEXT, path TEXT, "
            "level INTEGER, difficulty INTEGER, mode INTEGER)"
        )
        con.execute(
            "INSERT INTO song VALUES (?, ?, ?, ?, 1, 1, 0)",
            (MD5_A, SHA_A, "t1", "/a/bms1"),
        )
        con.execute(
            "INSERT INTO song VALUES (?, ?, ?, ?, 1, 1, 0)",
            (MD5_A, SHA_A, "t1 dup", "/a/bms2"),
        )
        con.execute(
            "INSERT INTO song VALUES (?, ?, ?, ?, 1, 1, 0)",
            ("d" * 32, SHA_B, "t2", "/b/bms"),
        )
        con.commit()
    finally:
        con.close()


class TestSongdataDedupe(unittest.TestCase):
    def test_hash_for_beatoraja_lookup_prefers_sha256(self) -> None:
        row = {"md5": MD5_A, "sha256": SHA_A}
        self.assertEqual(hash_for_beatoraja_lookup(row), SHA_A)

    def test_lookup_count_inflated_before_dedupe(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "songdata.db"
            _make_db(db)
            cnt = count_beatoraja_songdata_lookup(str(db), [SHA_A])
            self.assertEqual(cnt.lookup_rows, 2)
            self.assertEqual(cnt.unique_sha256, 1)

    def test_dedupe_and_lookup_matches_unique(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "songdata.db"
            _make_db(db)
            rep = dedupe_songdata_db(str(db))
            self.assertEqual(rep.rows_removed, 1)
            cnt = count_beatoraja_songdata_lookup(str(db), [SHA_A, SHA_B])
            self.assertEqual(cnt.lookup_rows, 2)
            self.assertEqual(cnt.unique_sha256, 2)
            by_lv = lookup_counts_by_level(
                [{"level": "8", "sha256": SHA_A}, {"level": "8", "sha256": SHA_B}],
                str(db),
            )
            self.assertEqual(by_lv["8"].lookup_rows, 2)

    def test_dedupe_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "songdata.db"
            _make_db(db)
            dedupe_songdata_db(str(db))
            rep2 = dedupe_songdata_db(str(db))
            self.assertEqual(rep2.rows_removed, 0)


if __name__ == "__main__":
    unittest.main()
