# Level Normalization

> 33 nodes · cohesion 0.13

## Key Concepts

- **beatoraja_rows.py** (20 connections) — `tools/table-filter/beatoraja_rows.py`
- **sync_header_level_order_from_beatoraja_rows()** (15 connections) — `tools/table-filter/beatoraja_rows.py`
- **apply_beatoraja_custom_level_to_level()** (13 connections) — `tools/table-filter/beatoraja_rows.py`
- **TestBeatorajaRows** (12 connections) — `tools/table-filter/tests/test_beatoraja_rows.py`
- **Any** (9 connections)
- **sanitize_header_for_beatoraja()** (9 connections) — `tools/table-filter/beatoraja_rows.py`
- **test_beatoraja_rows.py** (9 connections) — `tools/table-filter/tests/test_beatoraja_rows.py`
- **row_passes_beatoraja_strict_decoder()** (8 connections) — `tools/table-filter/beatoraja_rows.py`
- **_build_beatoraja_rows()** (8 connections) — `tools/table-filter/filter_table.py`
- **sanitize_chart_row_for_beatoraja()** (7 connections) — `tools/table-filter/beatoraja_rows.py`
- **normalize_beatoraja_chart_row()** (6 connections) — `tools/table-filter/beatoraja_rows.py`
- **strip_keys_cfg()** (6 connections) — `tools/table-filter/beatoraja_rows.py`
- **Q&A session: beatoraja 互換レイヤー（c0）の行整形とレベル処理の仕組み** (5 connections) — `graphify-out/memory/query_20260803_132440_beatoraja_互換レイヤー_c0_の行整形とレベル処理の仕組み.md`
- **C4 beatoraja Row Compat** (4 connections) — `graphify-out/memory/query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査.md`
- **_custom_level_to_level_string()** (4 connections) — `tools/table-filter/beatoraja_rows.py`
- **md5-first dedup key (beatoraja treats md5 as song identity)** (3 connections) — `graphify-out/memory/query_20260803_132440_beatoraja_互換レイヤー_c0_の行整形とレベル処理の仕組み.md`
- **_cfg_bool_default_true()** (3 connections) — `tools/table-filter/beatoraja_rows.py`
- **.test_sanitize_strip_source_keys()** (3 connections) — `tools/table-filter/tests/test_beatoraja_rows.py`
- **.test_apply_custom_level_disabled_keeps_level()** (2 connections) — `tools/table-filter/tests/test_beatoraja_rows.py`
- **.test_apply_custom_level_overwrites_level_and_strips_field()** (2 connections) — `tools/table-filter/tests/test_beatoraja_rows.py`
- **.test_beatoraja_folder_tag()** (2 connections) — `tools/table-filter/tests/test_beatoraja_rows.py`
- **.test_normalize_empty_title()** (2 connections) — `tools/table-filter/tests/test_beatoraja_rows.py`
- **.test_output_header_name_forces_name()** (2 connections) — `tools/table-filter/tests/test_beatoraja_rows.py`
- **.test_sanitize_header_drops_empty_course()** (2 connections) — `tools/table-filter/tests/test_beatoraja_rows.py`
- **.test_strict_decoder_requires_level_and_long_hash()** (2 connections) — `tools/table-filter/tests/test_beatoraja_rows.py`
- *... and 8 more nodes in this community*

## Relationships

- [Core Filter Pipeline](Core_Filter_Pipeline.md) (16 shared connections)
- [Config Schema & SQL](Config_Schema_%26_SQL.md) (6 shared connections)
- [beatoraja Row Compatibility](beatoraja_Row_Compatibility.md) (3 shared connections)
- [Source Tables & Outputs](Source_Tables_%26_Outputs.md) (1 shared connections)
- [Pages UI JSON Loading](Pages_UI_JSON_Loading.md) (1 shared connections)

## Source Files

- `graphify-out/memory/query_20260803_132440_beatoraja_互換レイヤー_c0_の行整形とレベル処理の仕組み.md`
- `graphify-out/memory/query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査.md`
- `tools/table-filter/beatoraja_rows.py`
- `tools/table-filter/filter_table.py`
- `tools/table-filter/tests/test_beatoraja_rows.py`

## Audit Trail

- EXTRACTED: 164 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*