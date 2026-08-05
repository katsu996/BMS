# beatoraja Song DB

> 35 nodes · cohesion 0.09

## Key Concepts

- **docs/ as GitHub Pages publish root** (17 connections) — `docs/README.md`
- **build job (CI steps)** (13 connections) — `.github/workflows/pages.yml`
- **build / deploy job separation (deploy-pages recommendation)** (10 connections) — `docs/ci-github-pages-workflow.md`
- **フロントエンド移行コスト判断メモ** (10 connections) — `docs/frontend-migration-costs.md`
- **songdata.db を GitHub Releases のアセットとして配布する手順** (8 connections) — `docs/github-releases-songdata.md`
- **ユーザー向け設定 JSON フォルダ README** (6 connections) — `tools/table-filter/config/README.md`
- **upload-songdata-github-release.ps1（GitHub REST API アップロード本体）** (5 connections) — `docs/github-releases-songdata.md`
- **songdata.db - beatoraja song DB (gitignored, fetched from Release)** (5 connections) — `AGENTS.md`
- **songdata.db from Latest Release (empty-file fails)** (4 connections) — `docs/ci-github-pages-workflow.md`
- **docs/table/pages_ui_config.json（Pages UI 設定）** (4 connections) — `tools/table-filter/config/README.md`
- **filter_table.py - main filter CLI** (4 connections) — `AGENTS.md`
- **Deploy GitHub Pages workflow** (3 connections) — `.github/workflows/pages.yml`
- **songdata.db + difficulty-table JSON to filtered JSON to GitHub Pages pipeline** (3 connections) — `AGENTS.md`
- **バンドル + TypeScript 中間案** (3 connections) — `docs/frontend-migration-costs.md`
- **静的 HTML 配信（現状維持案）** (3 connections) — `docs/frontend-migration-costs.md`
- **Vite + React + shadcn/ui フル移行案** (3 connections) — `docs/frontend-migration-costs.md`
- **upload-songdata-github-release.bat（アップロードラッパー・ASCII のみ）** (3 connections) — `docs/github-releases-songdata.md`
- **upload-songdata-github-release.secrets.txt（PAT・owner/repo 設定）** (3 connections) — `docs/github-releases-songdata.md`
- **songdata.db（beatoraja の楽曲 DB・Git 管理外）** (3 connections) — `docs/github-releases-songdata.md`
- **build_pages_table.py - browser_rows.json generator** (3 connections) — `AGENTS.md`
- **deploy job (actions/deploy-pages)** (2 connections) — `.github/workflows/pages.yml`
- **minbpm != maxbpm filtered republication pipeline** (2 connections) — `docs/bms/beatoraja-difficulty-table-url-and-filtered-publish.md`
- **Gitignored JSON - CI must fail instead of deploying empty table** (2 connections) — `docs/ci-github-pages-workflow.md`
- **browser_rows.json - Pages top table rows** (2 connections) — `AGENTS.md`
- **pages_ui_config.json - Pages top UI config** (2 connections) — `AGENTS.md`
- *... and 10 more nodes in this community*

## Relationships

- [beatoraja Row Compatibility](beatoraja_Row_Compatibility.md) (7 shared connections)
- [Pages UI JSON Loading](Pages_UI_JSON_Loading.md) (5 shared connections)
- [Source Tables & Outputs](Source_Tables_%26_Outputs.md) (4 shared connections)
- [Notion Design System](Notion_Design_System.md) (4 shared connections)
- [CI Validation Checks](CI_Validation_Checks.md) (3 shared connections)
- [GitHub Actions CI/CD](GitHub_Actions_CI-CD.md) (2 shared connections)
- [Release Upload Script](Release_Upload_Script.md) (1 shared connections)
- [Pages UI Column Config](Pages_UI_Column_Config.md) (1 shared connections)

## Source Files

- `.github/workflows/pages.yml`
- `AGENTS.md`
- `docs/README.md`
- `docs/bms/beatoraja-difficulty-table-url-and-filtered-publish.md`
- `docs/ci-github-pages-workflow.md`
- `docs/frontend-migration-costs.md`
- `docs/github-releases-songdata.md`
- `tools/table-filter/config/README.md`

## Audit Trail

- EXTRACTED: 116 (86%)
- INFERRED: 19 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*