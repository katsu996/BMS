---
type: "query"
date: "2026-08-01T07:26:20.792031+00:00"
question: "DEFAULT_INDEX_TABLE（JS フォールバック）と index_table 設定の関係は？"
contributor: "graphify"
outcome: "useful"
source_nodes: ["DEFAULT_INDEX_TABLE（JS 側のフォールバック既定値）", "index_table（列定義の単一ソース）", "pages-index-column-runtime.js"]
---

# Q: DEFAULT_INDEX_TABLE（JS フォールバック）と index_table 設定の関係は？

## Answer

Expanded from original query via vocab: [default, index, table, fallback, js]. DEFAULT_INDEX_TABLE (pages-index-column-runtime.js:8) is the hardcoded JS fallback; docs/pages-ui-config.md:53 documents it: used when browser_rows.json is stale/missing meta.pages_ui.index_table, and must stay synced with repo index_table (also stated in code comment L3). mergeIndexTable() (L159-206) merges per-key: if meta.pages_ui.index_table key is non-empty it wins, else DEFAULT_INDEX_TABLE value; object keys (column_labels, column_hidden_fallback, group_labels, chart_column) merged via Object.assign with config priority. So precedence: pages_ui_config.json (authoritative, embedded by build_pages_table.py) > DEFAULT_INDEX_TABLE (static fallback). The graph edge between them is semantically_similar_to [INFERRED] but the real relationship is EXTRACTED-level 'fallback_for' documented in code comment L3 + spec doc L53.

## Outcome

- Signal: useful

## Source Nodes

- DEFAULT_INDEX_TABLE（JS 側のフォールバック既定値）
- index_table（列定義の単一ソース）
- pages-index-column-runtime.js