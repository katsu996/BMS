# sync_header_level_order_from_beatoraja_rows()

> God node · 15 connections · `tools/table-filter/beatoraja_rows.py`

**Community:** [Level Normalization](Level_Normalization.md)

## Connections by Relation

### calls
- _write_outputs() `EXTRACTED`
- sort_level_stat_keys() `EXTRACTED`
- .test_sync_level_order_empty_rows_removes_key() `EXTRACTED`
- .test_sync_level_order_from_rows() `EXTRACTED`
- .test_sync_level_order_replaces_stale_header() `EXTRACTED`

### conceptually_related_to
- C4 beatoraja Row Compat `EXTRACTED`

### contains
- beatoraja_rows.py `EXTRACTED`

### imports
- filter_table.py `EXTRACTED`
- test_beatoraja_rows.py `EXTRACTED`

### rationale_for
- beatoraja / jbmstable-parser は header の level_order で難易度フォルダを作る `EXTRACTED`
- beatoraja / jbmstable-parser は header の level_order で難易度フォルダを作る。 マージ後に行の level… `EXTRACTED`

### references
- Any `EXTRACTED`
- Q&A session: beatoraja 互換レイヤー（c0）の行整形とレベル処理の仕組み `EXTRACTED`
- level_order regeneration from final rows (K14+ folders) `EXTRACTED`

### shares_data_with
- filtered_header.json - beatoraja header JSON `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*