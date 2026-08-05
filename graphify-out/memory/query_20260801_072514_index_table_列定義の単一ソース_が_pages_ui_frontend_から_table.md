---
type: "query"
date: "2026-08-01T07:25:14.190246+00:00"
question: "index_table（列定義の単一ソース）が Pages UI Frontend から Table Build、Table Rendering へどう流れるか"
contributor: "graphify"
outcome: "useful"
source_nodes: ["index_table（列定義の単一ソース）", "build_pages_table.py", "pages-index-column-runtime.js", "load_pages_ui_config()"]
---

# Q: index_table（列定義の単一ソース）が Pages UI Frontend から Table Build、Table Rendering へどう流れるか

## Answer

Expanded from original query via vocab: [index, table, column, pages, ui, build]. index_table node (docs/pages-ui-config.md, c3): references[EXTRACTED] build_pages_table.py (c2), pages-index-column-runtime.js (c3); references[INFERRED] pages-index-main.js (c6); semantically_similar_to[INFERRED] DEFAULT_INDEX_TABLE JS fallback. Data flow: config JSON docs/table/pages_ui_config.json (user edits) -> build_pages_table.py main() calls load_pages_ui_config() (c10 JSONC loader) -> embedded as browser_rows.json meta.pages_ui -> validate_pages_ui() in check_browser_rows_pages_ui.py (c9) CI-validates -> pages-index-main.js (c6) fetches and mergeIndexTable() (c3 runtime) merges column definitions, tableColTitle() resolves headers.

## Outcome

- Signal: useful

## Source Nodes

- index_table（列定義の単一ソース）
- build_pages_table.py
- pages-index-column-runtime.js
- load_pages_ui_config()