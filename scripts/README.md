# 補助スクリプト

## `songdata.db` を Web 以外からコミット・push する

`data/songdata.db` が **25MB 超**などで GitHub の Web からの置き換えが困難なとき、**ローカルでコピー → `git push`** するための補助です。

| ファイル | 環境 |
|-----------|------|
| [commit-songdata-push.bat](commit-songdata-push.bat) | Windows（コマンドプロンプト / PowerShell から実行可） |
| [commit-songdata-push.sh](commit-songdata-push.sh) | Linux / macOS |

### 使い方（想定）

1. リポジトリから **`commit-songdata-push.bat`**（または **`.sh`**）を、**`songdata.db` と同じフォルダ**（リポジトリの外）にコピーする。
2. コピーしたファイルを開き、**`REPO_ROOT`** を自分のクローンのルート（`.git` があるディレクトリ）に書き換える。  
   - 毎回パスを変えたくない場合は、環境変数 **`K_ORIGINAL_REPO`** にクローンのルートを設定してから実行してもよい（バッチ／シェルともに **`K_ORIGINAL_REPO` が優先**）。
3. そのフォルダでスクリプトを実行する。  
   - 同一階層に **`songdata.db`** があることを確認してから、**`data/songdata.db` へ上書きコピー**する。  
   - **変更がない**場合はコミット・push は行わない。  
   - **変更がある**場合は `git status` / `git diff --stat` を表示し、**`y` / `N` の確認**のあと **`git add` → `git commit` → `git push -u origin 現在ブランチ`** を行う。

コミットメッセージは固定で `chore(data): update songdata.db` です。メッセージを変えたい場合は、コミット後に `git commit --amend` してください。
