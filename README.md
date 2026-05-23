# test-CursorToSlack

## GitHub Pages と難易度表フィルタ

別リポジトリで **GitHub Pages** に静的ファイルを載せる手順と、**`songdata.db` + SQL** で元難易度表を絞り込んだ JSON を **GitHub Actions だけ**で生成して同じサイトに載せる仕組みです。

| 内容 | ドキュメント |
|------|----------------|
| Pages の基本 | [docs/github-pages-publish-guide.md](docs/github-pages-publish-guide.md) |
| Actions × songdata.db × 難易度表 | [docs/github-actions-songdata-table-filter.md](docs/github-actions-songdata-table-filter.md) |
| フィルタ設定・ローカル実行 | [tools/table-filter/README.md](tools/table-filter/README.md) |
| `songdata.db` の置き場所 | [data/README.md](data/README.md) |
| ワークフロー | [.github/workflows/pages.yml](.github/workflows/pages.yml) |

### クイックスタート

1. `data/songdata.db` をコミットする（更新のたびに差し替え）。
2. `tools/table-filter/filter_config.json` の `source_header_url` に元表のヘッダー JSON の URL を書く。
3. `main` に push → Actions がフィルタ（DB が無い／URL が空のときはスキップ）→ `docs/` を Pages 公開。

beatoraja の Table URL には `https://<owner>.github.io/<repo>/table/filtered_header.json` を登録します。
