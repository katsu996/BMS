# songdata.db schema (folder / song tables)

> God node · 14 connections · `docs/bms/bms-beatoraja-song-db.md`

**Community:** [Source Tables & Outputs](Source_Tables_%26_Outputs.md)

## Connections by Relation

### conceptually_related_to
- songdata.db from Latest Release (empty-file fails) `INFERRED`
- bms `INFERRED`

### references
- SQL virtual folder (folder/default.json + CommandBar) `EXTRACTED`
- BMS / beatoraja background memos index `EXTRACTED`
- songdata.db - beatoraja song DB (gitignored, fetched from Release) `INFERRED`
- minbpm != maxbpm WHERE condition (SQLite NULL semantics) `EXTRACTED`
- var BPM condition (minbpm != maxbpm, SQLite NULL semantics) `EXTRACTED`
- SQLiteSongDatabaseAccessor.java `EXTRACTED`
- SongUtils.crc32 path-hash parent IDs `EXTRACTED`
- SQL virtual folder + songdata.db identical across forks (JAR swap install) `EXTRACTED`
- Q&A session: c2（SQL Where Guard & Song DB Internals）合流後の主要ノードの整理 `EXTRACTED`
- songdata-updater performance strategies `EXTRACTED`

### shares_data_with
- _query_allowed_hashes() `EXTRACTED`
- songinfo.db schema (information table) `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*