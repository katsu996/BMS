# Difficulty table filter internals god doc (data flow / beatoraja compat / provenance)

> God node · 30 connections · `docs/github-actions-songdata-table-filter.md`

**Community:** [beatoraja Row Compatibility](beatoraja_Row_Compatibility.md)

## Connections by Relation

### conceptually_related_to
- filter_table.py data flow (allowed-hash set -> fetch -> intersect -> merge -> outputs) `EXTRACTED`
- jbmstable-parser compatibility rules for filtered_data.json `EXTRACTED`
- browser_rows.json meta (pages_ui, legends, table_rows_source_file) `EXTRACTED`
- Merge dedup by md5/sha256 with custom_level-wins policy `EXTRACTED`
- source_table_* provenance metadata on merged rows `EXTRACTED`
- AST coupling measurement: filter_table.py degree 56 / AST 54 (41 cross-community imports) `EXTRACTED`
- level_stats.json aggregation (SQL before/after per source, level_rows) `EXTRACTED`
- Wisdom: doc-level bridge ≠ code coupling `INFERRED`
- CI exit codes (beatoraja_empty_rows_policy fail=1; GITHUB_ACTIONS missing DB errors) `EXTRACTED`
- stellabms HTML -> bmstable header JSON resolution example `EXTRACTED`
- beatoraja TableData.validate() requirement (name non-empty, >=1 valid chart) `EXTRACTED`
- C0 CI/CD `EXTRACTED`

### references
- filter_table.py `EXTRACTED`
- [BMS repository README (songdata.db x difficulty tables -> GitHub Pages)](BMS_repository_README_%28songdata.db_x_difficulty_tables_-__GitHub_Pages%29.md) `EXTRACTED`
- [docs/ as GitHub Pages publish root](docs-_as_GitHub_Pages_publish_root.md) `EXTRACTED`
- build_pages_table.py `EXTRACTED`
- [Audit: C13 Bmstable JSON Contract vs C11 Pages UI Column Config (誤エッジ監査)](Audit-_C13_Bmstable_JSON_Contract_vs_C11_Pages_UI_Column_Config_%28%E8%AA%A4%E3%82%A8%E3%83%83%E3%82%B8%E7%9B%A3%E6%9F%BB%29.md) `EXTRACTED`
- build job (CI steps) `EXTRACTED`
- 別リポジトリで GitHub Pages に公開する手順 `EXTRACTED`
- build / deploy job separation (deploy-pages recommendation) `EXTRACTED`
- songdata.db を GitHub Releases のアセットとして配布する手順 `EXTRACTED`
- filter_table.py main() runtime hub orchestration `EXTRACTED`
- Difficulty table filter CLI overview (tools/table-filter) `EXTRACTED`
- Table URL .json-suffix vs HTML-mode branching `EXTRACTED`
- docs/table/pages_ui_config.json（Pages UI 設定） `EXTRACTED`
- pages_ui_config.json `EXTRACTED`
- config/filter_config.json（実行時設定） `EXTRACTED`
- Q&A session: how filter core ties 6 communities `EXTRACTED`
- jbmstable-parser (exch-bms2) external library `EXTRACTED`
- config/source_tables.json（既定の難易度表ソース一覧） `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*