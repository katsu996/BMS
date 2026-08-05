# Config Schema & SQL

> 31 nodes · cohesion 0.12

## Key Concepts

- **level_stats.py** (14 connections) — `tools/table-filter/level_stats.py`
- **build_merged_custom_level_rows()** (11 connections) — `tools/table-filter/level_stats.py`
- **level_to_str()** (9 connections) — `tools/table-filter/_level_normalizer.py`
- **sort_level_stat_keys()** (9 connections) — `tools/table-filter/level_stats.py`
- **_level_normalizer.py** (8 connections) — `tools/table-filter/_level_normalizer.py`
- **level_to_lookup_keys()** (7 connections) — `tools/table-filter/_level_normalizer.py`
- **merge_level_compare_rows()** (7 connections) — `tools/table-filter/level_stats.py`
- **Any** (7 connections)
- **level_to_float()** (6 connections) — `tools/table-filter/_level_normalizer.py`
- **level_bucket_for_stats()** (6 connections) — `tools/table-filter/level_stats.py`
- **source_indices_for_merged_row()** (6 connections) — `tools/table-filter/level_stats.py`
- **test_level_stats.py** (6 connections) — `tools/table-filter/tests/test_level_stats.py`
- **_accumulate_custom_level_buckets()** (5 connections) — `tools/table-filter/level_stats.py`
- **TestLevelStats** (5 connections) — `tools/table-filter/tests/test_level_stats.py`
- **_source_columns_from_stats()** (4 connections) — `tools/table-filter/level_stats.py`
- **_integer_variants()** (3 connections) — `tools/table-filter/_level_normalizer.py`
- **Any** (3 connections)
- **_by_source_for_columns()** (3 connections) — `tools/table-filter/level_stats.py`
- **.test_build_merged_custom_level_rows_by_source()** (2 connections) — `tools/table-filter/tests/test_level_stats.py`
- **.test_merge_compare_rows()** (2 connections) — `tools/table-filter/tests/test_level_stats.py`
- **.test_sort_numeric_then_unknown()** (2 connections) — `tools/table-filter/tests/test_level_stats.py`
- **.test_source_indices_for_merged_row()** (2 connections) — `tools/table-filter/tests/test_level_stats.py`
- **レベル値の型正規化（int / float / str → str 変換）を一元化。** (1 connections) — `tools/table-filter/_level_normalizer.py`
- **レベル値を float に変換。変換不可の場合は None。** (1 connections) — `tools/table-filter/_level_normalizer.py`
- **カスタムレベルマップのルックアップ用キー一覧を返す。** (1 connections) — `tools/table-filter/_level_normalizer.py`
- *... and 6 more nodes in this community*

## Relationships

- [Core Filter Pipeline](Core_Filter_Pipeline.md) (14 shared connections)
- [Level Normalization](Level_Normalization.md) (6 shared connections)

## Source Files

- `tools/table-filter/_level_normalizer.py`
- `tools/table-filter/level_stats.py`
- `tools/table-filter/tests/test_level_stats.py`

## Audit Trail

- EXTRACTED: 136 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*