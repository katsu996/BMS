# CI Validation Checks

> 20 nodes · cohesion 0.17

## Key Concepts

- **index_table（列定義の単一ソース）** (15 connections) — `docs/pages-ui-config.md`
- **index_table のデータフロー（config→build→render）** (8 connections) — `graphify-out/memory/query_20260801_072514_index_table_列定義の単一ソース_が_pages_ui_frontend_から_table.md`
- **DEFAULT_INDEX_TABLE（JS 静的フォールバック）** (6 connections) — `docs/pages-ui-config.md`
- **build_pages_table.py** (5 connections) — `docs/pages-ui-config.md`
- **pages-index-column-runtime.js** (5 connections) — `docs/pages-ui-config.md`
- **DEFAULT_INDEX_TABLE 静的フォールバック関係** (5 connections) — `graphify-out/memory/query_20260801_072620_default_index_table_js_フォールバック_と_index_table_設定の関係.md`
- **test_repo_default_index_table_syncs_with_config（同期テスト）** (4 connections) — `graphify-out/memory/query_20260801_072620_default_index_table_js_フォールバック_と_index_table_設定の関係.md`
- **pages_ui_config.json** (3 connections) — `docs/pages-ui-config.md`
- **test_repo_default_index_table_syncs_with_config** (3 connections) — `docs/pages-ui-config.md`
- **config/filter_config.json（実行時設定）** (3 connections) — `tools/table-filter/config/README.md`
- **meta.pages_ui（browser_rows.json 埋め込み）** (2 connections) — `docs/pages-ui-config.md`
- **pages_ui_json.py（JSONC コメント除去）** (2 connections) — `docs/pages-ui-config.md`
- **load_pages_ui_config()（JSONC ローダー）** (2 connections) — `graphify-out/memory/query_20260801_072514_index_table_列定義の単一ソース_が_pages_ui_frontend_から_table.md`
- **validate_pages_ui()** (2 connections) — `graphify-out/memory/query_20260801_072514_index_table_列定義の単一ソース_が_pages_ui_frontend_から_table.md`
- **mergeIndexTable()（キーごとのマージ）** (2 connections) — `graphify-out/memory/query_20260801_072620_default_index_table_js_フォールバック_と_index_table_設定の関係.md`
- **column_visible_defaults（列表示の既定）** (1 connections) — `docs/pages-ui-config.md`
- **column_widths（列幅の既定）** (1 connections) — `docs/pages-ui-config.md`
- **check_browser_rows_pages_ui.py（CI 検証）** (1 connections) — `graphify-out/memory/query_20260801_072514_index_table_列定義の単一ソース_が_pages_ui_frontend_から_table.md`
- **pages-index-main.js（fetch・描画）** (1 connections) — `graphify-out/memory/query_20260801_072514_index_table_列定義の単一ソース_が_pages_ui_frontend_から_table.md`
- **CI での index_table 同期検証** (1 connections) — `graphify-out/memory/query_20260801_072620_default_index_table_js_フォールバック_と_index_table_設定の関係.md`

## Relationships

- [beatoraja Song DB](beatoraja_Song_DB.md) (3 shared connections)
- [beatoraja Row Compatibility](beatoraja_Row_Compatibility.md) (2 shared connections)
- [GitHub Actions CI/CD](GitHub_Actions_CI-CD.md) (1 shared connections)
- [Index Table Rendering](Index_Table_Rendering.md) (1 shared connections)
- [Pages UI JSON Loading](Pages_UI_JSON_Loading.md) (1 shared connections)

## Source Files

- `docs/pages-ui-config.md`
- `graphify-out/memory/query_20260801_072514_index_table_列定義の単一ソース_が_pages_ui_frontend_から_table.md`
- `graphify-out/memory/query_20260801_072620_default_index_table_js_フォールバック_と_index_table_設定の関係.md`
- `tools/table-filter/config/README.md`

## Audit Trail

- EXTRACTED: 54 (75%)
- INFERRED: 18 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*