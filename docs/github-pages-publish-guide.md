# GitHub Pages で静的ファイルを公開する（別リポジトリ想定）

## 概要

`docs/` をサイトルートとして HTTPS 公開します。beatoraja の **難易度表 Table URL** には、**`https://.../something.json`** のように **JSON で終わる URL** を登録するのが扱いやすいです。

## 手順の要点

1. リポジトリの **Settings → Pages → Build and deployment → Source** で **GitHub Actions** を選ぶ。
2. 本リポジトリの [.github/workflows/pages.yml](../.github/workflows/pages.yml) のとおり、`main` への push で `docs/` がデプロイされる。
3. 公開 URL は `https://<ユーザー>.github.io/<リポジトリ名>/` 形式（**`docs/foo.json` → `/foo.json`**）。

## 難易度表の自動生成

[songdata.db と SQL で絞り込んだ表](./github-actions-songdata-table-filter.md) を **同じワークフロー**内で生成してから `docs/` に載せる構成にしています。

## 公式ドキュメント

- [GitHub Pages の概要](https://docs.github.com/ja/pages/getting-started-with-github-pages/github-pages-basics)
