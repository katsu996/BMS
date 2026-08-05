---
type: "query"
date: "2026-08-04T00:49:10.192720+00:00"
question: "c17 Table Fetch & Cache Internals（難易度表 URL の .json 分岐・.bmt キャッシュ）の構造と本ツールとの対応"
contributor: "graphify"
outcome: "useful"
source_nodes: ["Table URL .json-suffix vs HTML-mode branching", ".bmt gzip cache keyed by URL SHA-256", "TableDataAccessor.DifficultyTableAccessor#read"]
---

# Q: c17 Table Fetch & Cache Internals（難易度表 URL の .json 分岐・.bmt キャッシュ）の構造と本ツールとの対応

## Answer

c17 (3 nodes, all from docs/bms/beatoraja-difficulty-table-url-and-filtered-publish.md): hub TableDataAccessor.DifficultyTableAccessor#read references 1) Table URL .json-suffix vs HTML-mode branching (URL ending .json goes to DifficultyTableParser as header JSON; otherwise treated as source URL for glassist/BeMusicSeeker-style hosting) and 2) .bmt gzip cache keyed by URL SHA-256 (TableDataAccessor#getFileName uses URL string SHA-256 hex as filename, gzip .bmt stored under tablepath). TOOL CORRESPONDENCE: filter_table.py:66 _resolve_bmstable_header_url implements the same .json branch (passthrough) and concretizes the HTML mode by reading <meta name="bmstable"> from the HTML body (repo-specific contract; docs/index.html -> table/filtered_header.json). Doc section 5.2 recommended pipeline (enumerate sha256 from source table, filter via song WHERE sha256 IN (...) AND minbpm IS NOT NULL AND maxbpm IS NOT NULL AND minbpm != maxbpm, publish new JSON at new URL) is exactly what this repo's filter tool implements. GRAPH FINDING: c17 has NO direct edge to c0 implementation nodes (_resolve_bmstable_header_url); only implementation-side contact is c14 test_bmstable_resolve.py (3 tests: .json passthrough, HTML meta resolution, trailing-slash). Bridge candidates: c3 node 'bmstable HTML meta entry (docs/index.html -> table/filtered_header.json)'.

## Outcome

- Signal: useful

## Source Nodes

- Table URL .json-suffix vs HTML-mode branching
- .bmt gzip cache keyed by URL SHA-256
- TableDataAccessor.DifficultyTableAccessor#read