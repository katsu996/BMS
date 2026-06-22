"""filter_table.py のマージ重複除去（md5 キー・custom_level 優先）。"""

from __future__ import annotations

import unittest

from filter_table import (
    _custom_level_numeric,
    _replace_merged_row_keep_source_metadata,
    _row_dedupe_key,
    _should_replace_merged_row_by_custom_level,
)


class TestRowDedupeKey(unittest.TestCase):
    def test_md5_preferred_over_sha256(self) -> None:
        row = {
            "md5": "a" * 32,
            "sha256": "b" * 64,
        }
        self.assertEqual(_row_dedupe_key(row), "md5:" + "a" * 32)

    def test_sha256_when_no_md5(self) -> None:
        row = {"sha256": "c" * 64}
        self.assertEqual(_row_dedupe_key(row), "sha256:" + "c" * 64)

    def test_same_md5_same_key_regardless_of_sha256(self) -> None:
        md5 = "d" * 32
        k1 = _row_dedupe_key({"md5": md5})
        k2 = _row_dedupe_key({"md5": md5, "sha256": "e" * 64})
        self.assertEqual(k1, k2)


class TestCustomLevelDedupePriority(unittest.TestCase):
    def test_numeric_comparison(self) -> None:
        self.assertEqual(_custom_level_numeric({"custom_level": 15}, "custom_level"), 15.0)
        self.assertEqual(_custom_level_numeric({"custom_level": "14"}, "custom_level"), 14.0)

    def test_higher_custom_level_wins(self) -> None:
        prev = {"custom_level": 14, "level": "11", "title": "low"}
        new_row = {"custom_level": 15, "level": "12", "title": "high"}
        self.assertTrue(_should_replace_merged_row_by_custom_level(prev, new_row, "custom_level"))

    def test_equal_or_lower_does_not_replace(self) -> None:
        prev = {"custom_level": 15, "title": "keep"}
        self.assertFalse(_should_replace_merged_row_by_custom_level(prev, {"custom_level": 14}, "custom_level"))
        self.assertFalse(_should_replace_merged_row_by_custom_level(prev, {"custom_level": 15}, "custom_level"))

    def test_replace_keeps_merged_source_names(self) -> None:
        prev: dict = {
            "custom_level": 14,
            "title": "old",
            "source_table_names": ["第2通常難易度表", "Starlight"],
            "source_table_short_names": ["▽", "sr"],
        }
        new_row = {
            "custom_level": 15,
            "title": "new",
            "sha256": "f" * 64,
            "source_table_names": ["Starlight"],
            "source_table_short_names": ["sr"],
        }
        _replace_merged_row_keep_source_metadata(prev, new_row)
        self.assertEqual(prev["title"], "new")
        self.assertEqual(prev["custom_level"], 15)
        self.assertEqual(prev["sha256"], "f" * 64)
        self.assertEqual(prev["source_table_names"], ["第2通常難易度表", "Starlight"])
        self.assertEqual(prev["source_table_short_names"], ["▽", "sr"])


if __name__ == "__main__":
    unittest.main()
