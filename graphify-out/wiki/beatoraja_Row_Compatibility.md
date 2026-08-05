# beatoraja Row Compatibility

> 34 nodes · cohesion 0.11

## Key Concepts

- **Difficulty table filter internals god doc (data flow / beatoraja compat / provenance)** (30 connections) — `docs/github-actions-songdata-table-filter.md`
- **Audit: C13 Bmstable JSON Contract vs C11 Pages UI Column Config (誤エッジ監査)** (14 connections) — `graphify-out/memory/query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査.md`
- **beatoraja / jbmstable-parser JSON output contract** (9 connections) — `docs/beatoraja-jbmstable-table-json.md`
- **filter_table.py data flow (allowed-hash set -> fetch -> intersect -> merge -> outputs)** (8 connections) — `docs/github-actions-songdata-table-filter.md`
- **filter_table.py main() runtime hub orchestration** (8 connections) — `graphify-out/memory/query_20260801_070842_難易度表フィルタのコアが_pages_ui_フロントエンドからフィルタパイプライン_統計_行整形_s.md`
- **filtered_header.json - beatoraja header JSON** (7 connections) — `AGENTS.md`
- **jbmstable-parser compatibility rules for filtered_data.json** (5 connections) — `docs/github-actions-songdata-table-filter.md`
- **browser_rows.json meta (pages_ui, legends, table_rows_source_file)** (5 connections) — `docs/github-actions-songdata-table-filter.md`
- **Merge dedup by md5/sha256 with custom_level-wins policy** (4 connections) — `docs/github-actions-songdata-table-filter.md`
- **source_table_* provenance metadata on merged rows** (4 connections) — `docs/github-actions-songdata-table-filter.md`
- **AST coupling measurement: filter_table.py degree 56 / AST 54 (41 cross-community imports)** (4 connections) — `graphify-out/memory/query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査.md`
- **C13 Bmstable JSON Contract (beatoraja domain contract)** (4 connections) — `graphify-out/memory/query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査.md`
- **level_order regeneration from final rows (K14+ folders)** (3 connections) — `docs/beatoraja-jbmstable-table-json.md`
- **level_stats.json aggregation (SQL before/after per source, level_rows)** (3 connections) — `docs/github-actions-songdata-table-filter.md`
- **beatoraja HTML 入口（docs/table/bmstable.html）** (3 connections) — `docs/table/bmstable.html`
- **filtered_data.json - beatoraja data rows** (3 connections) — `AGENTS.md`
- **build_pages_table.py -> browser_rows.json -> pages-index-main.js pipeline** (3 connections) — `graphify-out/memory/query_20260801_070842_難易度表フィルタのコアが_pages_ui_フロントエンドからフィルタパイプライン_統計_行整形_s.md`
- **Q&A session: how filter core ties 6 communities** (3 connections) — `graphify-out/memory/query_20260801_070842_難易度表フィルタのコアが_pages_ui_フロントエンドからフィルタパイプライン_統計_行整形_s.md`
- **C11 Pages UI Column Config** (3 connections) — `graphify-out/memory/query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査.md`
- **Wisdom: doc-level bridge ≠ code coupling** (3 connections) — `graphify-out/memory/query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査.md`
- **bmstable HTML meta entry (docs/index.html -> table/filtered_header.json)** (3 connections) — `README.md`
- **jbmstable-parser decodeJSONTableData(accept=false)** (2 connections) — `docs/beatoraja-jbmstable-table-json.md`
- **jbmstable-parser (exch-bms2)** (2 connections) — `docs/beatoraja-jbmstable-table-json.md`
- **beatoraja TableData.validate() requirements** (2 connections) — `docs/beatoraja-jbmstable-table-json.md`
- **Difficulty tables as chart metadata lists** (2 connections) — `docs/bms/beatoraja-difficulty-table-url-and-filtered-publish.md`
- *... and 9 more nodes in this community*

## Relationships

- [beatoraja Song DB](beatoraja_Song_DB.md) (7 shared connections)
- [Pages UI JSON Loading](Pages_UI_JSON_Loading.md) (6 shared connections)
- [GitHub Actions CI/CD](GitHub_Actions_CI-CD.md) (4 shared connections)
- [Core Filter Pipeline](Core_Filter_Pipeline.md) (4 shared connections)
- [Level Normalization](Level_Normalization.md) (3 shared connections)
- [CI Validation Checks](CI_Validation_Checks.md) (2 shared connections)
- [Source Tables & Outputs](Source_Tables_%26_Outputs.md) (1 shared connections)
- [Notion Design System](Notion_Design_System.md) (1 shared connections)
- [Index Table Rendering](Index_Table_Rendering.md) (1 shared connections)

## Source Files

- `AGENTS.md`
- `README.md`
- `docs/beatoraja-jbmstable-table-json.md`
- `docs/bms/beatoraja-difficulty-table-url-and-filtered-publish.md`
- `docs/github-actions-songdata-table-filter.md`
- `docs/table/bmstable.html`
- `graphify-out/memory/query_20260801_070842_難易度表フィルタのコアが_pages_ui_フロントエンドからフィルタパイプライン_統計_行整形_s.md`
- `graphify-out/memory/query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査.md`

## Audit Trail

- EXTRACTED: 130 (86%)
- INFERRED: 21 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*