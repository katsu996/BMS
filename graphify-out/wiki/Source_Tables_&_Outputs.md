# Source Tables & Outputs

> 40 nodes · cohesion 0.09

## Key Concepts

- **songdata.db schema (folder / song tables)** (14 connections) — `docs/bms/bms-beatoraja-song-db.md`
- **resolve_sql_where()** (12 connections) — `tools/table-filter/sql_where_guard.py`
- **sql_where_guard.py** (10 connections) — `tools/table-filter/sql_where_guard.py`
- **validate_sql_where()** (8 connections) — `tools/table-filter/sql_where_guard.py`
- **CommandBar.java (getSongDatas)** (7 connections) — `docs/bms/requirements-filtered-bms-folder-tool.md`
- **SQL virtual folder (folder/default.json + CommandBar)** (7 connections) — `docs/bms/requirements-filtered-bms-folder-tool.md`
- **Q&A session: SQL 仮想フォルダ（folder/default.json + CommandBar）の実装詳細と本ツールへの示唆** (7 connections) — `graphify-out/memory/query_20260803_132704_sql_仮想フォルダ_folder_default_json___commandbar_の実装詳細と.md`
- **TestSqlWhereGuard** (7 connections) — `tools/table-filter/tests/test_sql_where_guard.py`
- **beatoraja (exch-bms2) baseline player** (6 connections) — `docs/bms/beatoraja-vs-lr2oraja-derivatives.md`
- **BMS / beatoraja background memos index** (6 connections) — `docs/bms/README.md`
- **Virtual-folder tool requirements v0.2** (6 connections) — `docs/bms/requirements-filtered-bms-folder-tool.md`
- **minbpm != maxbpm WHERE condition (SQLite NULL semantics)** (5 connections) — `docs/bms/requirements-filtered-bms-folder-tool.md`
- **Q&A session: beatoraja baseline と LR2oraja / Endless Dream フォークの差と、このツールへの影響** (5 connections) — `graphify-out/memory/query_20260803_132558_beatoraja_baseline_と_lr2oraja___endless_dream_フォーク.md`
- **Table URL .json-suffix vs HTML-mode branching** (4 connections) — `docs/bms/beatoraja-difficulty-table-url-and-filtered-publish.md`
- **LR2oraja Endless Dream - QoL fork (seraxis)** (4 connections) — `docs/bms/beatoraja-vs-lr2oraja-derivatives.md`
- **LR2oraja - LR2-gauge fork (wcko87)** (4 connections) — `docs/bms/beatoraja-vs-lr2oraja-derivatives.md`
- **songinfo.db schema (information table)** (4 connections) — `docs/bms/bms-beatoraja-song-db.md`
- **SQLiteSongDatabaseAccessor.java** (4 connections) — `docs/bms/bms-beatoraja-song-db.md`
- **test_sql_where_guard.py** (4 connections) — `tools/table-filter/tests/test_sql_where_guard.py`
- **SongUtils.crc32 path-hash parent IDs** (3 connections) — `docs/bms/bms-beatoraja-song-db.md`
- **songinfo INNER JOIN drops unanalysed songs** (3 connections) — `docs/bms/requirements-filtered-bms-folder-tool.md`
- **SQL virtual folder + songdata.db identical across forks (JAR swap install)** (3 connections) — `graphify-out/memory/query_20260803_132558_beatoraja_baseline_と_lr2oraja___endless_dream_フォーク.md`
- **SONG_TABLE_COLUMNS whitelist mirrors beatoraja song columns** (3 connections) — `graphify-out/memory/query_20260803_132704_sql_仮想フォルダ_folder_default_json___commandbar_の実装詳細と.md`
- **Q&A session: c2（SQL Where Guard & Song DB Internals）合流後の主要ノードの整理** (3 connections) — `graphify-out/memory/query_20260804_004211_c2_sql_where_guard___song_db_internals_合流後の主要ノードの整.md`
- **TableDataAccessor.DifficultyTableAccessor#read** (2 connections) — `docs/bms/beatoraja-difficulty-table-url-and-filtered-publish.md`
- *... and 15 more nodes in this community*

## Relationships

- [Core Filter Pipeline](Core_Filter_Pipeline.md) (9 shared connections)
- [Pages UI JSON Loading](Pages_UI_JSON_Loading.md) (4 shared connections)
- [beatoraja Song DB](beatoraja_Song_DB.md) (4 shared connections)
- [GitHub Actions CI/CD](GitHub_Actions_CI-CD.md) (4 shared connections)
- [beatoraja Row Compatibility](beatoraja_Row_Compatibility.md) (1 shared connections)
- [Level Normalization](Level_Normalization.md) (1 shared connections)

## Source Files

- `docs/bms/README.md`
- `docs/bms/beatoraja-difficulty-table-url-and-filtered-publish.md`
- `docs/bms/beatoraja-vs-lr2oraja-derivatives.md`
- `docs/bms/bms-beatoraja-song-db.md`
- `docs/bms/requirements-filtered-bms-folder-tool.md`
- `graphify-out/memory/query_20260803_132558_beatoraja_baseline_と_lr2oraja___endless_dream_フォーク.md`
- `graphify-out/memory/query_20260803_132704_sql_仮想フォルダ_folder_default_json___commandbar_の実装詳細と.md`
- `graphify-out/memory/query_20260804_004211_c2_sql_where_guard___song_db_internals_合流後の主要ノードの整.md`
- `tools/table-filter/sql_where_guard.py`
- `tools/table-filter/tests/test_sql_where_guard.py`

## Audit Trail

- EXTRACTED: 144 (87%)
- INFERRED: 21 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*