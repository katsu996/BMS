---
type: "query"
date: "2026-08-01T07:14:38.446386+00:00"
question: "resolve_sql_where の実装が README の sql_where 仕様と一致するか検証"
contributor: "graphify"
outcome: "useful"
source_nodes: ["sql_where_guard.py", "sql_where - song-table SQL filter fragment", "sql_where_preset (const_bpm / var_bpm)"]
---

# Q: resolve_sql_where の実装が README の sql_where 仕様と一致するか検証

## Answer

Verified against code: SQL_WHERE_PRESETS in sql_where_guard.py matches README examples exactly (const_bpm = minbpm IS NOT NULL AND maxbpm IS NOT NULL AND minbpm = maxbpm; var_bpm = minbpm != maxbpm). SQLite NULL semantics honored (explicit IS NOT NULL). FOUND DOC DRIFT: README.md:49, tools/table-filter/README.md:53, docs/filter-config-schema.md:13 still document sql_where_disable_identifier_whitelist=true as functional, but sql_where_guard.py validate_sql_where() takes no such flag (whitelist always on) and filter_config.example.json marks the key deprecated (ignored). Implementation-vs-doc mismatch in 3 files.

## Outcome

- Signal: useful

## Source Nodes

- sql_where_guard.py
- sql_where - song-table SQL filter fragment
- sql_where_preset (const_bpm / var_bpm)