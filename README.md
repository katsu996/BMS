# test-CursorToSlack

## ドキュメント

- [beatoraja 楽曲データベース（BMS）仕様メモ](docs/bms-beatoraja-song-db.md) — `songdata.db` / `songinfo.db` のテーブル概要と更新挙動の整理
- [条件付き BMS 仮想フォルダ生成ツール — 要件定義・調査](docs/requirements-filtered-bms-folder-tool.md)
- [beatoraja `default.json` 断片例: `minbpm != maxbpm`](examples/beatoraja-default-json-snippet-changing-bpm.json)
- [beatoraja と LR2oraja / Endless Dream の違い](docs/beatoraja-vs-lr2oraja-derivatives.md)
- [beatoraja: 難易度表の URL 公開・追加と、条件で絞った表の再公開](docs/beatoraja-difficulty-table-url-and-filtered-publish.md)

## GitHub Pages（静的ファイルの公開）

難易度表 JSON などを **GitHub Pages** に載せる手順と、ワークフロー・`docs/` の雛形です。

- **手順書**: [docs/github-pages-publish-guide.md](docs/github-pages-publish-guide.md)
- **ワークフロー**: [.github/workflows/pages.yml](.github/workflows/pages.yml)
- **公開ルート**: [docs/](docs/)（`.nojekyll` と `index.html` を含む）

別リポジトリでは、上記パスをコピーし、リポジトリの **Settings → Pages → Source: GitHub Actions** を選べば同じ構成で公開できます。
