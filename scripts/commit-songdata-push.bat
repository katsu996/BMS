@echo off
setlocal EnableExtensions EnableDelayedExpansion

rem =============================================================================
rem  songdata.db をリポジトリの data/songdata.db にコピーしてコミット・push する
rem  使い方: このファイルを songdata.db と同じフォルダにコピーし、下の REPO_ROOT を
rem          あなたのクローンのルート（.git があるディレクトリ）に書き換えて実行。
rem  前提: git が PATH にあり、リモートへ push する認証が済んでいること。
rem =============================================================================

rem --- ここを自分の環境に合わせて編集（コピー先で毎回直してもよい）---
set "REPO_ROOT=C:\path\to\test-CursorToSlack"

rem 環境変数 K_ORIGINAL_REPO があればそちらを優先（編集不要で済む場合向け）
if defined K_ORIGINAL_REPO set "REPO_ROOT=%K_ORIGINAL_REPO%"

set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
set "SOURCE_DB=%SCRIPT_DIR%\songdata.db"
set "TARGET_REL=data\songdata.db"
set "TARGET_DB=%REPO_ROOT%\%TARGET_REL%"

echo.
echo [commit-songdata-push] songdata.db をリポジトリへ反映します。
echo   ソース: "%SOURCE_DB%"
echo   先  : "%TARGET_DB%"
echo.

if not defined REPO_ROOT (
  echo ERROR: REPO_ROOT が空です。バッチ先頭の REPO_ROOT か環境変数 K_ORIGINAL_REPO を設定してください。
  exit /b 1
)

if not exist "%REPO_ROOT%\.git\" (
  echo ERROR: REPO_ROOT に .git がありません: "%REPO_ROOT%"
  exit /b 1
)

if not exist "%SOURCE_DB%" (
  echo ERROR: 同一フォルダに songdata.db がありません: "%SOURCE_DB%"
  exit /b 1
)

if not exist "%REPO_ROOT%\data\" (
  echo ERROR: リポジトリに data フォルダがありません: "%REPO_ROOT%\data"
  exit /b 1
)

where git >nul 2>&1
if errorlevel 1 (
  echo ERROR: git が PATH に見つかりません。
  exit /b 1
)

copy /Y "%SOURCE_DB%" "%TARGET_DB%" >nul
if errorlevel 1 (
  echo ERROR: コピーに失敗しました。
  exit /b 1
)

pushd "%REPO_ROOT%" || (
  echo ERROR: リポジトリへ移動できませんでした。
  exit /b 1
)

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
  echo ERROR: git 作業ツリーではありません。
  popd
  exit /b 1
)

git status --porcelain -- "%TARGET_REL%" | findstr /r "." >nul
if errorlevel 1 (
  echo 変更がありません（コピー先は既に同一内容です）。push は行いません。
  popd
  exit /b 0
)

echo ----- git status（対象ファイル）-----
git status -- "%TARGET_REL%"
echo ----- git diff --stat（対象ファイル）-----
git diff --stat -- "%TARGET_REL%"
echo ----------------------------------------

set /p "ANS=コミットして origin へ push しますか？ [y/N]: "
if /i not "%ANS%"=="y" (
  echo 中止しました（ファイルはコピー済みです。必要なら手元で git checkout 等してください）。
  popd
  exit /b 0
)

for /f "delims=" %%B in ('git rev-parse --abbrev-ref HEAD') do set "BRANCH=%%B"
if "%BRANCH%"=="" (
  echo ERROR: 現在ブランチを取得できませんでした。
  popd
  exit /b 1
)

git add -- "%TARGET_REL%"
if errorlevel 1 (
  echo ERROR: git add に失敗しました。
  popd
  exit /b 1
)

git commit -m "chore(data): update songdata.db"
if errorlevel 1 (
  echo ERROR: git commit に失敗しました（ステージングやフックを確認してください）。
  popd
  exit /b 1
)

git push -u origin "%BRANCH%"
set "PUSH_RC=%ERRORLEVEL%"
popd

if not "%PUSH_RC%"=="0" (
  echo ERROR: git push が失敗しました（認証・ブランチ保護・ネットワークを確認）。
  exit /b 1
)

echo 完了しました。
exit /b 0
