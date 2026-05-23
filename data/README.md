# `data/songdata.db`

beatoraja がローカルで生成する **`songdata.db`** を、このパスに置いてコミットするか、CI の前に配置してください。

## 更新のしかた（ユーザー作業）

1. PC 上の beatoraja のデータフォルダから `songdata.db` をコピーする。
2. 本リポジトリの `data/songdata.db` に上書きする。
3. `git add data/songdata.db && git commit && git push` で更新する。

GitHub の Web 画面から **Add file → Upload files** で置き換えても構いません。

## サイズが大きい場合

Git LFS の利用や、リポジトリを表公開専用に分けることを検討してください。Actions のランナー上では通常の `git clone` で取得できる必要があります。
