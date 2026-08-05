---
type: "query"
date: "2026-08-01T07:13:37.527034+00:00"
question: "minbpm != maxbpm 再公開パイプラインの分岐はどこにつながる？"
contributor: "graphify"
outcome: "useful"
source_nodes: ["minbpm != maxbpm filtered republication pipeline", "minbpm != maxbpm WHERE condition (SQLite NULL semantics)", "sql_where - song-table SQL filter fragment", "songdata.db（beatoraja の楽曲 DB・Git 管理外）"]
---

# Q: minbpm != maxbpm 再公開パイプラインの分岐はどこにつながる？

## Answer

Expanded from original query via vocab: [minbpm, maxbpm, sqlite, songdata, database, filter, release, table]. Community 9 (Beatoraja Song DB Internals) is a requirements-only community: 20 doc concepts. minbpm != maxbpm filtered republication pipeline (docs/bms/beatoraja-difficulty-table-url-and-filtered-publish.md) --references[EXTRACTED]--> songdata.db (c5 AGENTS.md). minbpm != maxbpm WHERE condition (docs/bms/requirements-filtered-bms-folder-tool.md) --rationale_for--> songinfo INNER JOIN drops unanalysed songs [EXTRACTED]; --references--> songdata.db schema + songinfo.db schema; --semantically_similar_to[INFERRED]--> sql_where fragment (README.md, c9). KEY FINDING: no edges exist between c9 and the implementation c11 (resolve_sql_where/validate_sql_where) or c2 - the branch is wired only at the artifact level (songdata.db) and by INFERRED similarity, a documented knowledge gap.

## Outcome

- Signal: useful

## Source Nodes

- minbpm != maxbpm filtered republication pipeline
- minbpm != maxbpm WHERE condition (SQLite NULL semantics)
- sql_where - song-table SQL filter fragment
- songdata.db（beatoraja の楽曲 DB・Git 管理外）