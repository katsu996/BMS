# songdata.db と SQL で難易度表を絞り込み、GitHub Actions で公開する

## 結論: GitHub Actions だけで実現できるか

**はい。** 次の条件を満たせば、**GitHub Actions のみ**で「元表 JSON を取得 → `songdata.db` に SQL で問い合わせ → 交差でフィルタ → `docs/` に出力 → GitHub Pages で配信」まで完結できます。

1. **ワークフロー実行時に `songdata.db` がリポジトリに存在する**（通常は `git push` でコミットしておく）。
2. **元難易度表のヘッダー JSON が HTTPS で取得できる**（`filter_config.json` の `source_header_url`）。データ本体はヘッダーの `data_url` か、設定で別 URL を指定。
3. **公開先のベース URL**が分かる（Actions では `SITE_BASE_URL` をワークフローが自動設定し、ヘッダーの `data_url` を書き換え）。

**GitHub が提供していないもの:** ブラウザだけで「手元の `songdata.db` を Actions に渡す」専用 UIはありません。**ユーザーが DB をリポジトリに載せて更新する**（push または Web のファイル追加）想定です。機密や巨大ファイルを載せない運用を推奨します。

## このリポジトリでの流れ

1. `data/songdata.db` を配置してコミット（更新時は上書きコミット）。
2. `tools/table-filter/filter_config.json` で `source_header_url` と `sql_where` を設定する。`site_base_url` は空のままでよい（Actions が `SITE_BASE_URL` を渡す）。
3. `main` へ push するか、Actions の **Run workflow** で手動実行する。
4. **Deploy GitHub Pages** ジョブが `docs/` 全体（生成された `docs/table/*.json` を含む）を公開する。
5. beatoraja の **Table URL** に  
   `https://<owner>.github.io/<repo>/table/filtered_header.json`  
   のような **`.json` で終わる URL** を登録する。

## 制限・注意

- **フィルタ結果は「元表に載っている譜面」のみ**です。`songdata.db` にしか無い曲は難易度表には出ません（交差フィルタ）。
- **段位コース（`course`）**は、譜面が落ちて要件を満たさなくなると **コース定義が壊れる**可能性があります。スクリプトは `charts` が空のコースを削除しますが、運用仕様は各自で確認してください。
- **外部表の取得**はネットワーク依存です。相手サーバの障害・レート制限で失敗する場合があります。
- **`sql_where` は信頼できる設定のみ**をコミットしてください（簡易的な禁止キーワードチェックのみ）。

## 関連ファイル

| ファイル | 説明 |
|----------|------|
| [tools/table-filter/filter_table.py](../tools/table-filter/filter_table.py) | フィルタ本体（Python 標準ライブラリのみ） |
| [tools/table-filter/filter_config.json](../tools/table-filter/filter_config.json) | 実際に読む設定（URL・SQL 等） |
| [tools/table-filter/README.md](../tools/table-filter/README.md) | 設定項目の短い説明 |
| [.github/workflows/pages.yml](../.github/workflows/pages.yml) | フィルタ実行後に Pages をデプロイ |

## 参考（beatoraja 側）

- `song` テーブルに `md5`, `sha256`, `minbpm`, `maxbpm` などが格納される（ローカルスキャン結果）。
- 難易度表の JSON はコミュニティ表ごとに細部は異なるが、多くは **データ配列の各要素に `sha256` / `md5`** を持つ。
