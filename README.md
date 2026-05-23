# test-CursorToSlack

## GitHub Pages（別リポジトリ公開用）

難易度表 JSON などを **別の公開用リポジトリ**で GitHub Pages に載せる手順と、必要なワークフロー・静的ファイルの雛形を同梱しています。

- **手順書**: [docs/github-pages-publish-guide.md](docs/github-pages-publish-guide.md)
- **ワークフロー**: [.github/workflows/pages.yml](.github/workflows/pages.yml)（`docs/` をデプロイ）
- **公開ルート**: [docs/](docs/)（`.nojekyll` と `index.html` を含む）

別リポジトリでは、上記パスをそのままコピーし、GitHub の **Settings → Pages → Source: GitHub Actions** を選べば同じ構成で公開できます。