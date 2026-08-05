# Pages UI JSON Loading

> 30 nodes · cohesion 0.11

## Key Concepts

- **BMS repository README (songdata.db x difficulty tables -> GitHub Pages)** (17 connections) — `README.md`
- **sql_where -- song-table SQL filter fragment** (10 connections) — `README.md`
- **filter_config.json key schema (docs/filter-config-schema.md)** (8 connections) — `docs/filter-config-schema.md`
- **Difficulty table filter CLI overview (tools/table-filter)** (7 connections) — `tools/table-filter/README.md`
- **resolve_sql_where implementation verification finding** (6 connections) — `graphify-out/memory/query_20260801_071438_resolve_sql_where_の実装が_readme_の_sql_where_仕様と一致するか.md`
- **minbpm != maxbpm WHERE condition (SQLite NULL semantics)** (5 connections) — `graphify-out/memory/query_20260801_071337_minbpm____maxbpm_再公開パイプラインの分岐はどこにつながる.md`
- **sql_where_disable_identifier_whitelist doc drift finding (3 files)** (5 connections) — `graphify-out/memory/query_20260801_071438_resolve_sql_where_の実装が_readme_の_sql_where_仕様と一致するか.md`
- **songdata.db (beatoraja song DB, Git-untracked, Latest GitHub Release asset)** (5 connections) — `README.md`
- **Identifier whitelist always on (no disable path in sql_where_guard.py)** (4 connections) — `docs/filter-config-schema.md`
- **var BPM condition (minbpm != maxbpm, SQLite NULL semantics)** (4 connections) — `README.md`
- **sql_where_disable_identifier_whitelist (deprecated, ignored; whitelist always on)** (4 connections) — `README.md`
- **sql_where_preset (const_bpm / var_bpm fixed safe SQL)** (4 connections) — `README.md`
- **SQL injection defense (forbidden patterns + always-on identifier whitelist)** (4 connections) — `tools/table-filter/README.md`
- **Documented knowledge gap (requirements doc community not wired to implementation)** (3 connections) — `graphify-out/memory/query_20260801_071337_minbpm____maxbpm_再公開パイプラインの分岐はどこにつながる.md`
- **minbpm != maxbpm filtered republication pipeline** (3 connections) — `graphify-out/memory/query_20260801_071337_minbpm____maxbpm_再公開パイプラインの分岐はどこにつながる.md`
- **Q&A session: where the minbpm != maxbpm republication branch connects** (3 connections) — `graphify-out/memory/query_20260801_071337_minbpm____maxbpm_再公開パイプラインの分岐はどこにつながる.md`
- **custom_level_mapping (per-source original level -> custom level)** (3 connections) — `README.md`
- **source_tables / source_tables_path difficulty-table source configuration** (3 connections) — `README.md`
- **check_filter_config_example_sync.py** (3 connections) — `tools/table-filter/check_filter_config_example_sync.py`
- **EXPECTED_KEYS CI sync via check_filter_config_example_sync.py** (2 connections) — `docs/filter-config-schema.md`
- **CI exit codes (beatoraja_empty_rows_policy fail=1; GITHUB_ACTIONS missing DB errors)** (2 connections) — `docs/github-actions-songdata-table-filter.md`
- **Q&A session: resolve_sql_where vs README spec verification** (2 connections) — `graphify-out/memory/query_20260801_071438_resolve_sql_where_の実装が_readme_の_sql_where_仕様と一致するか.md`
- **bms** (2 connections) — `pyproject.toml`
- **beatoraja_level_from_custom_level level overwrite for K-folder split** (2 connections) — `README.md`
- **const BPM condition (minbpm = maxbpm with IS NOT NULL)** (2 connections) — `README.md`
- *... and 5 more nodes in this community*

## Relationships

- [beatoraja Row Compatibility](beatoraja_Row_Compatibility.md) (6 shared connections)
- [beatoraja Song DB](beatoraja_Song_DB.md) (5 shared connections)
- [Source Tables & Outputs](Source_Tables_%26_Outputs.md) (4 shared connections)
- [Level Normalization](Level_Normalization.md) (1 shared connections)
- [Notion Design System](Notion_Design_System.md) (1 shared connections)
- [CI Validation Checks](CI_Validation_Checks.md) (1 shared connections)
- [GitHub Actions CI/CD](GitHub_Actions_CI-CD.md) (1 shared connections)

## Source Files

- `README.md`
- `docs/filter-config-schema.md`
- `docs/github-actions-songdata-table-filter.md`
- `graphify-out/memory/query_20260801_071337_minbpm____maxbpm_再公開パイプラインの分岐はどこにつながる.md`
- `graphify-out/memory/query_20260801_071438_resolve_sql_where_の実装が_readme_の_sql_where_仕様と一致するか.md`
- `pyproject.toml`
- `tools/table-filter/README.md`
- `tools/table-filter/check_filter_config_example_sync.py`

## Audit Trail

- EXTRACTED: 92 (77%)
- INFERRED: 27 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*