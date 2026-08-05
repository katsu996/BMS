# Core Filter Pipeline

> 45 nodes · cohesion 0.10

## Key Concepts

- **filter_table.py** (59 connections) — `tools/table-filter/filter_table.py`
- **main()** (18 connections) — `tools/table-filter/filter_table.py`
- **Any** (17 connections)
- **die()** (12 connections) — `tools/table-filter/sql_where_guard.py`
- **_write_outputs()** (11 connections) — `tools/table-filter/filter_table.py`
- **_row_dedupe_key()** (9 connections) — `tools/table-filter/filter_table.py`
- **test_filter_dedupe.py** (8 connections) — `tools/table-filter/tests/test_filter_dedupe.py`
- **_resolve_bmstable_header_url()** (7 connections) — `tools/table-filter/filter_table.py`
- **_should_replace_merged_row_by_custom_level()** (7 connections) — `tools/table-filter/filter_table.py`
- **fetch_bytes()** (7 connections) — `tools/table-filter/http_fetch.py`
- **_custom_level_numeric()** (6 connections) — `tools/table-filter/filter_table.py`
- **_apply_custom_level()** (5 connections) — `tools/table-filter/filter_table.py`
- **_filter_data_array()** (5 connections) — `tools/table-filter/filter_table.py`
- **_json_from_http_body()** (5 connections) — `tools/table-filter/filter_table.py`
- **_replace_merged_row_keep_source_metadata()** (5 connections) — `tools/table-filter/filter_table.py`
- **TestCustomLevelDedupePriority** (5 connections) — `tools/table-filter/tests/test_filter_dedupe.py`
- **validate_json_field_name()** (4 connections) — `tools/table-filter/beatoraja_rows.py`
- **_chart_row_allowed()** (4 connections) — `tools/table-filter/filter_table.py`
- **_filter_course_object()** (4 connections) — `tools/table-filter/filter_table.py`
- **_filter_course_structure()** (4 connections) — `tools/table-filter/filter_table.py`
- **_query_allowed_hashes()** (4 connections) — `tools/table-filter/filter_table.py`
- **_row_level_lookup_keys()** (4 connections) — `tools/table-filter/filter_table.py`
- **http_fetch.py** (4 connections) — `tools/table-filter/http_fetch.py`
- **TestRowDedupeKey** (4 connections) — `tools/table-filter/tests/test_filter_dedupe.py`
- **_empty_rows_policy_fail()** (3 connections) — `tools/table-filter/filter_table.py`
- *... and 20 more nodes in this community*

## Relationships

- [Level Normalization](Level_Normalization.md) (16 shared connections)
- [GitHub Actions CI/CD](GitHub_Actions_CI-CD.md) (15 shared connections)
- [Config Schema & SQL](Config_Schema_%26_SQL.md) (14 shared connections)
- [Source Tables & Outputs](Source_Tables_%26_Outputs.md) (9 shared connections)
- [beatoraja Row Compatibility](beatoraja_Row_Compatibility.md) (4 shared connections)
- [Bmstable JSON Contract](Bmstable_JSON_Contract.md) (2 shared connections)
- [Table Fetch & Cache](Table_Fetch_%26_Cache.md) (1 shared connections)

## Source Files

- `graphify-out/memory/query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査.md`
- `tools/table-filter/beatoraja_rows.py`
- `tools/table-filter/filter_table.py`
- `tools/table-filter/http_fetch.py`
- `tools/table-filter/sql_where_guard.py`
- `tools/table-filter/tests/test_filter_dedupe.py`
- `tools/table-filter/tests/test_http_fetch.py`

## Audit Trail

- EXTRACTED: 255 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*