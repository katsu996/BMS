# Graph Report - .  (2026-08-05)

## Corpus Check
- Corpus is ~32,247 words - fits in a single context window. You may not need a graph.

## Summary
- 432 nodes · 906 edges · 15 communities
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 65 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- GitHub Actions CI/CD
- Core Filter Pipeline
- Source Tables & Outputs
- beatoraja Song DB
- beatoraja Row Compatibility
- Level Normalization
- Notion Design System
- Config Schema & SQL
- Pages UI JSON Loading
- Index Table Rendering
- Release Upload Script
- Pages UI Column Config
- CI Validation Checks
- Bmstable JSON Contract
- Table Fetch & Cache

## God Nodes (most connected - your core abstractions)
1. `Difficulty table filter internals god doc (data flow / beatoraja compat / provenance)` - 30 edges
2. `main()` - 18 edges
3. `BMS repository README (songdata.db x difficulty tables -> GitHub Pages)` - 17 edges
4. `docs/ as GitHub Pages publish root` - 17 edges
5. `sync_header_level_order_from_beatoraja_rows()` - 15 edges
6. `index_table（列定義の単一ソース）` - 15 edges
7. `songdata.db schema (folder / song tables)` - 14 edges
8. `Audit: C13 Bmstable JSON Contract vs C11 Pages UI Column Config (誤エッジ監査)` - 14 edges
9. `apply_beatoraja_custom_level_to_level()` - 13 edges
10. `load_resolved_filter_config()` - 13 edges

## Surprising Connections (you probably didn't know these)
- `sync_header_level_order_from_beatoraja_rows()` --shares_data_with--> `filtered_header.json - beatoraja header JSON`  [INFERRED]
  tools/table-filter/beatoraja_rows.py → AGENTS.md
- `apply_beatoraja_custom_level_to_level()` --references--> `beatoraja_level_from_custom_level level overwrite for K-folder split`  [EXTRACTED]
  tools/table-filter/beatoraja_rows.py → README.md
- `md5-first dedup key (beatoraja treats md5 as song identity)` --conceptually_related_to--> `_row_dedupe_key()`  [INFERRED]
  graphify-out/memory/query_20260803_132440_beatoraja_互換レイヤー_c0_の行整形とレベル処理の仕組み.md → tools/table-filter/filter_table.py
- `load_pages_ui_config()` --conceptually_related_to--> `C8 Pages UI Config (load_pages_ui_config)`  [EXTRACTED]
  tools/table-filter/pages_ui_json.py → graphify-out/memory/query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査.md
- `bms` --conceptually_related_to--> `songdata.db schema (folder / song tables)`  [INFERRED]
  pyproject.toml → docs/bms/bms-beatoraja-song-db.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **GitHub Pages CI/CD pipeline (build, validate, deploy)** — _github_workflows_pages_buildjob, tools_table_filter_filter_table_file, tools_table_filter_build_pages_table_file, tools_table_filter_check_browser_rows_pages_ui_file, tools_table_filter_smoke_check_outputs_file, _github_workflows_pages_deployjob [INFERRED 0.95]
- **Generated table JSON artifacts (gitignored, CI-regenerated)** — docs_table_filtered_header_file, docs_table_filtered_data_file, docs_table_filtered_data_enriched_file, docs_table_browser_rows_file, docs_table_level_stats_file [INFERRED 0.95]
- **sql_where configuration subsystem (free-form fragment, presets, whitelist)** — readme_sql_where, readme_sql_where_preset, readme_minbpm_eq_maxbpm_condition, readme_minbpm_neq_maxbpm_condition, readme_sql_where_disable_identifier_whitelist [EXTRACTED 1.00]
- **beatoraja fork derivation tree (beatoraja -> LR2oraja -> Endless Dream)** — docs_bms_beatoraja_vs_lr2oraja_derivatives_beatoraja, docs_bms_beatoraja_vs_lr2oraja_derivatives_lr2oraja, docs_bms_beatoraja_vs_lr2oraja_derivatives_endlessdream [EXTRACTED 1.00]
- **Filter pipeline: allowed-hash set -> fetch -> intersect -> merge -> outputs -> Pages UI** — docs_github_actions_songdata_table_filter_dataflow_pipeline, graphify_out_memory_query_20260801_070842_pages_ui_s_runtime_hub, docs_github_actions_songdata_table_filter_level_stats, docs_github_actions_songdata_table_filter_provenance_metadata, graphify_out_memory_query_20260801_070842_pages_ui_s_pages_ui_pipeline [INFERRED 0.85]
- **minbpm != maxbpm branch (SQLite NULL semantics) through republication** — readme_minbpm_neq_maxbpm_condition, graphify_out_memory_query_20260801_071337_minbpm_maxbpm_where_condition, graphify_out_memory_query_20260801_071337_minbpm_maxbpm_republication_pipeline, readme_songdata_db [INFERRED 0.85]
- **index_table の単一ソースフロー（config→build→render）** — docs_pages_ui_config_pages_ui_config_json, docs_pages_ui_config_index_table, docs_pages_ui_config_build_pages_table_py, docs_pages_ui_config_meta_pages_ui, graphify_out_memory_query_20260801_072514_index_table_pages_ui_frontend_table_pages_index_main_js, docs_pages_ui_config_pages_index_column_runtime_js [EXTRACTED 1.00]
- **index_table と DEFAULT_INDEX_TABLE の同期メカニズム** — docs_pages_ui_config_index_table, docs_pages_ui_config_default_index_table, docs_pages_ui_config_test_repo_default_index_table_syncs_with_config, graphify_out_memory_query_20260801_072620_default_index_table_js_index_table_merge_index_table, graphify_out_memory_query_20260801_072620_default_index_table_js_index_table_ci_sync_detection [EXTRACTED 1.00]
- **beatoraja 互換レイヤー（c0）: データ行 level 分割 + header level_order 再生成** — tools_table_filter_beatoraja_rows_row_passes_beatoraja_strict_decoder, tools_table_filter_beatoraja_rows_apply_beatoraja_custom_level_to_level, tools_table_filter_beatoraja_rows_sync_header_level_order_from_beatoraja_rows [EXTRACTED 1.00]
- **beatoraja fork derivation tree (baseline → LR2oraja → Endless Dream)** — docs_bms_beatoraja_vs_lr2oraja_derivatives_beatoraja, docs_bms_beatoraja_vs_lr2oraja_derivatives_lr2oraja, docs_bms_beatoraja_vs_lr2oraja_derivatives_endlessdream [EXTRACTED 1.00]
- **SQL WHERE フラグメント適用パイプライン（beatoraja CommandBar ↔ 本ツール sql_where_guard/filter_table）** — docs_bms_requirements_filtered_bms_folder_tool_sql_virtual_folder, docs_bms_requirements_filtered_bms_folder_tool_commandbar, tools_table_filter_sql_where_guard, tools_table_filter_filter_table [INFERRED 0.75]
- **c2 community core nodes (merged from c9 requirements docs + c11 sql_where_guard implementation)** — docs_bms_requirements_filtered_bms_folder_tool_sql_virtual_folder, docs_bms_bms_beatoraja_song_db_crc_parent_ids, docs_bms_bms_beatoraja_song_db_songdata_db_schema [INFERRED 0.85]
- **songdata.db schema producer/consumer network** — docs_bms_bms_beatoraja_song_db_songdata_db_schema, docs_bms_bms_beatoraja_song_db_sqlitesongdatabaseaccessor, docs_bms_bms_beatoraja_song_db_songdata_updater_strategies, readme_minbpm_neq_maxbpm_condition, docs_bms_requirements_filtered_bms_folder_tool_sql_virtual_folder, graphify_out_memory_query_20260803_132558_beatoraja_baseline_fork_sql_virtual_folder_shared_across_forks, tools_table_filter_filter_table_query_allowed_hashes, docs_bms_bms_beatoraja_song_db_songinfo_db_schema [INFERRED 0.75]
- **SQL virtual folder design decision (approach A folder/default.json fragment over deprecated approach C')** — docs_bms_requirements_filtered_bms_folder_tool_requirements, docs_bms_bms_beatoraja_song_db_crc_parent_ids, docs_bms_requirements_filtered_bms_folder_tool_sql_virtual_folder, docs_bms_requirements_filtered_bms_folder_tool_commandbar [INFERRED 0.75]
- **beatoraja DifficultyTableAccessor fetch & cache flow** — graphify_out_memory_query_20260804_004910_c17_table_fetch___cache_internals_難易度表_url_の__json_tabledataaccessor_difficultytableaccessor_read, graphify_out_memory_query_20260804_004910_c17_table_fetch___cache_internals_難易度表_url_の__json_table_url_json_suffix_vs_html_mode_branching, graphify_out_memory_query_20260804_004910_c17_table_fetch___cache_internals_難易度表_url_の__json_bmt_gzip_cache_keyed_by_url_sha_256 [EXTRACTED 1.00]
- **フロントエンド移行判断トレードオフ（現状維持 / 中間 / フル移行の比較）** — docs_frontend_migration_costs_static_html, docs_frontend_migration_costs_bundle_ts, docs_frontend_migration_costs_vite_react_shadcn [INFERRED 0.85]
- **現状維持が成立する変更範囲（pages-index-*.js + pages_ui_config.json + ユニットテスト）** — docs_frontend_migration_costs_frontend_migration_costs, docs_assets_pages_index_main, docs_table_pages_ui_config, tools_table_filter_check_browser_rows_pages_ui [INFERRED 0.85]
- **songdata.db Release-to-CI pipeline** — songdata_db, docs_github_releases_songdata_release_distribution, docs_ci_github_pages_workflow_latest_release_songdata [INFERRED 0.75]
- **docs/ ディレクトリのドキュメント索引ハブ** — docs_readme_docs_publish_root, readme_bms_overview, docs_bms_readme_background_memos [INFERRED 0.75]
- **C13 beatoraja header output pipeline (_write_outputs)** — tools_table_filter_filter_table_write_outputs, tools_table_filter_beatoraja_rows_sanitize_header_for_beatoraja, tools_table_filter_beatoraja_rows_sync_header_level_order_from_beatoraja_rows, tools_table_filter_io_helpers_save_json, docs_table_filtered_header_file [EXTRACTED 1.00]
- **C11/C8 Pages UI config consumer chain (no header dependency)** — tools_table_filter_build_pages_table_main, tools_table_filter_pages_ui_json_load_pages_ui_config, tools_table_filter_check_browser_rows_pages_ui_main, tools_table_filter_io_helpers_load_json, docs_table_filtered_data_file [EXTRACTED 1.00]
- **Indirect binding of C13 and C11 via C4 (beatoraja_rows)** — graphify_out_memory_query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査_c13_bmstable_json_contract, graphify_out_memory_query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査_c4_beatoraja_row_compat, graphify_out_memory_query_20260805_000000_c13_bmstable_contract_vs_c11_pages_ui_誤エッジ監査_c11_pages_ui_column_config [EXTRACTED 1.00]

## Communities (15 total, 0 thin omitted)

### Community 0 - "GitHub Actions CI/CD"
Cohesion: 0.09
Nodes (34): main(), _norm_hash(), Any, main(), Any, validate_browser_rows(), validate_pages_ui(), _resolve_config_pipeline() (+26 more)

### Community 1 - "Core Filter Pipeline"
Cohesion: 0.10
Nodes (33): C1 Implementation Hub (filter_table.py), patch, validate_json_field_name(), _apply_custom_level(), _chart_row_allowed(), _custom_level_numeric(), _empty_rows_policy_fail(), _filter_course_object() (+25 more)

### Community 2 - "Source Tables & Outputs"
Cohesion: 0.09
Nodes (32): .bmt gzip cache keyed by URL SHA-256, TableDataAccessor.DifficultyTableAccessor#read, Table URL .json-suffix vs HTML-mode branching, beatoraja (exch-bms2) baseline player, LR2oraja Endless Dream - QoL fork (seraxis), LR2oraja - LR2-gauge fork (wcko87), SongUtils.crc32 path-hash parent IDs, songdata.db schema (folder / song tables) (+24 more)

### Community 3 - "beatoraja Song DB"
Cohesion: 0.09
Nodes (35): build job (CI steps), Deploy GitHub Pages workflow, deploy job (actions/deploy-pages), songdata.db + difficulty-table JSON to filtered JSON to GitHub Pages pipeline, stdlib-only constraint for tools/table-filter scripts, minbpm != maxbpm filtered republication pipeline, build / deploy job separation (deploy-pages recommendation), Gitignored JSON - CI must fail instead of deploying empty table (+27 more)

### Community 4 - "beatoraja Row Compatibility"
Cohesion: 0.11
Nodes (34): jbmstable-parser decodeJSONTableData(accept=false), jbmstable-parser (exch-bms2), level_order regeneration from final rows (K14+ folders), beatoraja / jbmstable-parser JSON output contract, beatoraja TableData.validate() requirements, Upstream update compatibility checklist, Difficulty tables as chart metadata lists, beatoraja TableData structure (name/url/tag/folder/course) (+26 more)

### Community 5 - "Level Normalization"
Cohesion: 0.13
Nodes (20): beatoraja / jbmstable-parser は header の level_order で難易度フォルダを作る, md5-first dedup key (beatoraja treats md5 as song identity), beatoraja はデータ行の level 文字列でフォルダを分割する（本体 TableDataAccessor）, Q&A session: beatoraja 互換レイヤー（c0）の行整形とレベル処理の仕組み, C4 beatoraja Row Compat, apply_beatoraja_custom_level_to_level(), _cfg_bool_default_true(), _custom_level_to_level_string() (+12 more)

### Community 6 - "Notion Design System"
Cohesion: 0.09
Nodes (24): Hairline + layered micro-shadow elevation, Dark indigo hero band (#213183), Monochrome-plus-blue single-accent discipline, Notion Blue primary (#0075de), Notion design system analysis (warm paper-calm), NotionInter typography (tuned Inter), Decorative multi-color sticker palette, Warm Paper canvas (#f6f5f4) (+16 more)

### Community 7 - "Config Schema & SQL"
Cohesion: 0.12
Nodes (24): _integer_variants(), level_to_float(), level_to_lookup_keys(), level_to_str(), Any, レベル値の型正規化（int / float / str → str 変換）を一元化。, レベル値を float に変換。変換不可の場合は None。, カスタムレベルマップのルックアップ用キー一覧を返す。 (+16 more)

### Community 8 - "Pages UI JSON Loading"
Cohesion: 0.11
Nodes (28): EXPECTED_KEYS CI sync via check_filter_config_example_sync.py, filter_config.json key schema (docs/filter-config-schema.md), Identifier whitelist always on (no disable path in sql_where_guard.py), CI exit codes (beatoraja_empty_rows_policy fail=1; GITHUB_ACTIONS missing DB errors), Documented knowledge gap (requirements doc community not wired to implementation), minbpm != maxbpm filtered republication pipeline, Q&A session: where the minbpm != maxbpm republication branch connects, songinfo INNER JOIN drops unanalysed songs requirement (+20 more)

### Community 9 - "Index Table Rendering"
Cohesion: 0.15
Nodes (13): Path, load_pages_ui_config(), Any, `docs/table/pages_ui_config.json` 用の読み込み。 標準の `json.load` は `//` 行コメントや `/* */`…, ダブルクォート／シングルクォート文字列の外側だけで `//` と `/* */` を除去する。, pages_ui_config を読み込み、辞書で返す。ルートがオブジェクトでなければ空辞書。, strip_jsonc_style_comments(), _extract_default_index_table() (+5 more)

### Community 10 - "Release Upload Script"
Cohesion: 0.16
Nodes (16): applyHrefTemplate(), bpmNumber(), cellHtml(), chartCellHtml(), collectAllKeys(), dbFieldRaw(), esc(), escAttr() (+8 more)

### Community 11 - "Pages UI Column Config"
Cohesion: 0.17
Nodes (16): Format-GitHubAuthHelp(), Get-ErrorHttpStatusCode(), Get-ReleaseAssets(), Get-ReleaseByTag(), Get-UploadHeaders(), Invoke-GitHubAuthorized(), Invoke-GitHubDelete(), Invoke-GitHubGet() (+8 more)

### Community 12 - "CI Validation Checks"
Cohesion: 0.17
Nodes (20): build_pages_table.py, column_visible_defaults（列表示の既定）, column_widths（列幅の既定）, DEFAULT_INDEX_TABLE（JS 静的フォールバック）, index_table（列定義の単一ソース）, meta.pages_ui（browser_rows.json 埋め込み）, pages-index-column-runtime.js, pages_ui_config.json (+12 more)

### Community 13 - "Bmstable JSON Contract"
Cohesion: 0.31
Nodes (9): bmstable HTML meta entry (docs/index.html -> table/filtered_header.json), .bmt gzip cache keyed by URL SHA-256, c17 Table Fetch & Cache Internals, DifficultyTableParser, Doc section 5.2 recommended pipeline (sha256 enumerate + SQL filter + republish), Table URL .json-suffix vs HTML-mode branching, TableDataAccessor.DifficultyTableAccessor#read, TableDataAccessor#getFileName (+1 more)

### Community 14 - "Table Fetch & Cache"
Cohesion: 0.32
Nodes (3): object, 末尾が / のときも HTML として bmstable を解決する（.json 誤認を防ぐ）。, TestBmstableResolve

## Knowledge Gaps
- **31 isolated node(s):** `smoke_check_outputs.py - pre-deploy smoke check`, `check_browser_rows_pages_ui.py - meta.pages_ui validator`, `check_filter_config_example_sync.py - config key sync check`, `source_tables.json - default difficulty-table sources`, `filtered_data_enriched.json - rows with provenance columns` (+26 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Difficulty table filter internals god doc (data flow / beatoraja compat / provenance)` connect `beatoraja Row Compatibility` to `GitHub Actions CI/CD`, `Core Filter Pipeline`, `Source Tables & Outputs`, `beatoraja Song DB`, `Notion Design System`, `Pages UI JSON Loading`, `CI Validation Checks`?**
  _High betweenness centrality (0.380) - this node is a cross-community bridge._
- **Why does `別リポジトリで GitHub Pages に公開する手順` connect `Notion Design System` to `Pages UI JSON Loading`, `beatoraja Song DB`, `beatoraja Row Compatibility`?**
  _High betweenness centrality (0.126) - this node is a cross-community bridge._
- **Why does `フロントエンド移行コスト判断メモ` connect `beatoraja Song DB` to `Pages UI JSON Loading`, `GitHub Actions CI/CD`, `Release Upload Script`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._
- **What connects `smoke_check_outputs.py - pre-deploy smoke check`, `check_browser_rows_pages_ui.py - meta.pages_ui validator`, `check_filter_config_example_sync.py - config key sync check` to the rest of the system?**
  _31 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `GitHub Actions CI/CD` be split into smaller, more focused modules?**
  _Cohesion score 0.08521870286576169 - nodes in this community are weakly interconnected._
- **Should `Core Filter Pipeline` be split into smaller, more focused modules?**
  _Cohesion score 0.09898989898989899 - nodes in this community are weakly interconnected._
- **Should `Source Tables & Outputs` be split into smaller, more focused modules?**
  _Cohesion score 0.09102564102564102 - nodes in this community are weakly interconnected._