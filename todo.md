# 保守・改善バックログ

以前ここに列挙していた **P0〜P3 の項目は実装済み**です（モジュール分割・SQL ガード・HTTP リトライ・CI の ruff / unittest / スモークテスト・Pages 用 CSS 共通化・`page_title` 分離・ドキュメント整備など）。詳細は該当コミットの差分を参照してください。

| 優先度 | 意味 |
|--------|------|
| **P0** | 放置すると障害・セキュリティ・beatoraja 互換破壊につながりやすい |
| **P1** | 回帰を防ぐためのテストや CI |
| **P2** | 可読性・分割・設定の整理 |
| **P3** | UX やドキュメント、あればよいが必須ではない |

---

## 定期メンテ（カレンダーではなくトリガーで実施）

- **beatoraja / LR2oraja の新バージョン**が出たら: 難易度表まわりの挙動を確認し、必要なら [`docs/beatoraja-jbmstable-table-json.md`](docs/beatoraja-jbmstable-table-json.md) とユニットテストを更新する。  
- **`source_tables.json`（または `source_tables_path`）を差し替えたとき**: 元表の JSON キー変更で `custom_level_source_key` や level 集計がずれていないか確認する。  
- **GitHub の Actions / Pages の仕様変更**: `pages.yml` の `actions/*` メジャー更新時はリリースノートを読んでからマージする。

---

## バックログ（未着手・任意）

次の表は **継続開発で改善すると効果が大きい候補**です（上の「優先度」の定義に沿って並べています）。着手したら優先度を見直し、完了したら**該当行を削除**してください。

### P0（信頼性・互換・運用リスク）

| 優先度 | 内容 |
|--------|------|
| **P0** | **複数ソース取得の部分失敗**: 1 本だけ Cloudflare 等で落ちたときにジョブ全体を失敗させるか、失敗ソースを stderr に列挙して続行するかを方針化し、`filter_table.py` とドキュメントを揃える（運用で「どれが欠けた表か」が分かることが重要）。 |
| **P0** | **`songdata.db` 肥大化**: Actions の実行時間・ディスク・キャッシュ方針（LFS・スリム DB・差分更新の可否）を整理し、`data/README.md` と CI のタイムアウト方針に反映する。 |
| **P0** | **beatoraja 本体の互換追従**: `DifficultyTableParser` / `TableData.validate` の前提が変わった場合に備え、公式リリースノートを見るチェックリストを `docs/beatoraja-jbmstable-table-json.md` に追記する。 |

### P1（テスト・CI・回帰防止）

| 優先度 | 内容 |
|--------|------|
| **P1** | **スモークテスト拡充**: 生成された `browser_rows.json` の列キーと `docs/index.html` の表示列（IR / Chart 等）の整合、`filtered_header.json` の `data_url` 相対解決の回帰を `smoke_check_outputs.py` に足す。 |
| **P1** | **`pages_ui_config.json` の検証**: `build_pages_table` が埋め込む `meta.pages_ui` と、未知のキー・型崩れ時の警告または CI 失敗を検討する。 |
| **P1** | **`workflow_dispatch` 入力**: 手動実行時だけ別の `filter_config` パスや「ドライラン（fetch のみ）」を選べると、本番 `main` を汚さず検証しやすい。 |
| **P1** | **Dependabot / Actions ピン留め**: `actions/checkout` 等の更新方針（自動 PR のマージ条件）を README か docs に一文で明文化する。 |

### P2（構造・保守性・設定の一貫性）

| 優先度 | 内容 |
|--------|------|
| **P2** | **`docs/index.html` の JS 分割**: 列リサイズ・ソート・フィルタ・IR セル生成などを `docs/assets/*.js` に分離し、読みやすさと差分の見やすさを上げる。 |
| **P2** | **列定義の単一ソース化**: `tablePri` / `dbPriFull` / `pages_ui_config` の列順・ラベルの重複を減らし、将来列追加時の取りこぼしを防ぐ（完全自動化でなくても「生成スクリプト」やコメントでの正規化から可）。 |
| **P2** | **`ubuntu-latest` のランナーで `actions/setup-python` の 3.14.3 が取れない場合の代替**（利用可能なマイナーへの一時ピン、`allow-prerelease` 等）を [`docs/github-actions-songdata-table-filter.md`](docs/github-actions-songdata-table-filter.md) に追記する。 |
| **P2** | **`source_tables.json` のスキーマ検証**: 必須キー欠落・`custom_level_mapping` の型ミスを CI で早期検知する（`jsonschema` は使わず標準ライブラリでも可）。 |

### P3（ユーザビリティ・任意機能）

| 優先度 | 内容 |
|--------|------|
| **P3** | **ツールバー開閉の永続化**: 「並び替え・絞り込み・列の表示」パネルの開閉状態を `sessionStorage` に保存し、再訪問時に復元する。 |
| **P3** | **`docs/table/index.html`**: `filtered_header.json` / `filtered_data.json` / `bmstable.html` への直リンクと beatoraja 登録時の注意を一覧するショートページ。 |
| **P3** | **URL クエリで状態共有**: キーワード・出自フィルタ・ソート条件をクエリに反映し、リンクコピーで同じ表示を再現できるようにする。 |
| **P3** | **一覧の CSV / JSON エクスポート**: 現在フィルタ済みの行だけをダウンロードできるボタン（クライアントのみで完結）。 |
| **P3** | **大量行向け表示**: 仮想スクロールまたはページングで、数万行でも初期描画とスクロールを軽くする。 |
| **P3** | **アクセシビリティ**: 表の `caption`、フォーカスリング、キーボードでツールバー操作、スクリーンリーダー向けの列ヘッダ関連付けの見直し。 |
| **P3** | **ローディング・エラー UI**: `browser_rows.json` 取得中のスケルトン、失敗時の再試行ボタンとメッセージの統一。 |
| **P3** | **モバイルレイアウト**: 狭い幅では列をカード化する、または横スクロールのヒントを強化する。 |
| **P3** | **`level-stats.html` とトップの体験揃え**: テーマ切替・フィルタの有無など、両ページで操作感が違う部分を揃える。 |
| **P3** | **多言語（i18n）**: ラベル文言を JSON 化し、ja / en の切替を検討（規模が大きければ別リポジトリ化の判断材料にもなる）。 |

---

## 完了したら

新しいバックログ項目を追加するときは優先度を付け、完了したら**該当行を削除**するか `## 完了済み` に移し、**いつ・どの PR で**終わったかを一行メモすると、あとから見た人が迷いません。
