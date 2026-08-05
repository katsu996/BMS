---
type: "session"
date: "2026-08-04T00:42:11.163635+00:00"
question: "c2（SQL Where Guard & Song DB Internals）合流後の主要ノードの整理"
contributor: "graphify"
outcome: "useful"
source_nodes: ["SQL virtual folder (folder/default.json + CommandBar)", "SongUtils.crc32 path-hash parent IDs", "songdata.db schema (folder / song tables)"]
---

# Q: c2（SQL Where Guard & Song DB Internals）合流後の主要ノードの整理

## Answer

Session summary after the --update that merged the requirements/song-DB docs (old c9) with sql_where_guard implementation (old c11) into community c2 (40 nodes, cohesion 0.09). 1) SQL virtual folder (folder/default.json + CommandBar) node (degree 5): references CommandBar.java getSongDatas; incoming references from Q&A session note (bridge head to sql_where_guard.py EXTRACTED 1.0), beatoraja baseline player, Virtual-folder tool requirements v0.2, and INFERRED edge from LR2oraja fork. 2) SongUtils.crc32 path-hash parent IDs (degree 1): folder parent-child via CRC32 of path string stored in parent/song.folder; the deprecated approach C' (direct folder INSERT) that requirements v0.2 §3.2/§5 rejects (fragile, update-resistant) - the chosen design is approach A (folder/default.json SQL fragment). 3) songdata.db schema (folder/song tables) hub (degree 8): links DB producers (SQLiteSongDatabaseAccessor.java, songdata-updater performance strategies) and consumers (minbpm != maxbpm condition, SQL virtual folder, forks-compat); sole shares_data_with edge to songinfo.db schema; INFERRED edge to c10 songdata.db Release-fetch node bridges requirements docs world (c2) and GitHub Actions world (c10). 4) filter_table.py _query_allowed_hashes() consumes the same song table contract.

## Outcome

- Signal: useful

## Source Nodes

- SQL virtual folder (folder/default.json + CommandBar)
- SongUtils.crc32 path-hash parent IDs
- songdata.db schema (folder / song tables)