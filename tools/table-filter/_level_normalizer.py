"""レベル値の型正規化（int / float / str → str 変換）を一元化。"""

from __future__ import annotations

from typing import Any


def level_to_str(raw: Any) -> str | None:
    """任意のレベル値を正規化した文字列を返す。None／空文字列は None に変換。"""
    if raw is None:
        return None
    if isinstance(raw, bool):
        return str(raw).lower()
    if isinstance(raw, int):
        return str(raw)
    if isinstance(raw, float):
        return str(int(raw)) if raw.is_integer() else str(raw).strip()
    s = str(raw).strip()
    return s if s else None


def level_to_float(raw: Any) -> float | None:
    """レベル値を float に変換。変換不可の場合は None。"""
    s = level_to_str(raw)
    if s is None:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def level_to_lookup_keys(raw: Any) -> list[str]:
    """カスタムレベルマップのルックアップ用キー一覧を返す。"""
    s = level_to_str(raw)
    if s is None:
        return []
    seen: set[str] = set()
    out: list[str] = []
    for k in [s] + _integer_variants(s):
        if k not in seen:
            seen.add(k)
            out.append(k)
    return out


def _integer_variants(s: str) -> list[str]:
    """文字列が数値の場合、整数表現のバリエーションを追加。"""
    try:
        f = float(s)
        if f.is_integer():
            return [str(int(f))]
    except ValueError:
        pass
    return []
