---
type: "query"
date: "2026-08-03T13:27:04.954169+00:00"
question: "SQL 仮想フォルダ（folder/default.json + CommandBar）の実装詳細と本ツールへの示唆"
contributor: "graphify"
outcome: "useful"
source_nodes: ["SQL virtual folder (folder/default.json + CommandBar)", "CommandBar.java (getSongDatas)", "Virtual-folder tool requirements v0.2", "sql_where_guard.py"]
---

# Q: SQL 仮想フォルダ（folder/default.json + CommandBar）の実装詳細と本ツールへの示唆

## Answer

Expanded from original query via vocab: [virtual, folder, sql, commandbar, song, database]. SQL virtual folder (c9): BarManager reads folder/default.json; CommandBar.java getSongDatas(sql,...) runs the WHERE fragment. With songinfo.db enabled the query is SELECT DISTINCT md5, sha256 FROM song INNER JOIN (information LEFT OUTER JOIN (score LEFT OUTER JOIN scorelog)) ON song.sha256=information.sha256 WHERE <sql>; without songinfo it is song LEFT OUTER JOIN (score...) - same fragment does NOT work in both modes (doc 2.3/4). INNER JOIN drops songs without information rows (rationale node: songinfo INNER JOIN drops unanalysed songs). Table-qualified song.maxbpm recommended (LEVEL node uses song.mode). CONNECTION TO THIS TOOL: sql_where_guard.py SONG_TABLE_COLUMNS whitelist mirrors the same song columns; filter_table.py applies fragment to SELECT DISTINCT md5, sha256 FROM song WHERE (...) - same shape as CommandBar query but song-only, no information join.

## Outcome

- Signal: useful

## Source Nodes

- SQL virtual folder (folder/default.json + CommandBar)
- CommandBar.java (getSongDatas)
- Virtual-folder tool requirements v0.2
- sql_where_guard.py