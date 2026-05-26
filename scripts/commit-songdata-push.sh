#!/usr/bin/env bash
set -euo pipefail

# =============================================================================
# songdata.db をリポジトリの data/songdata.db にコピーしてコミット・push する
# 使い方: このファイルを songdata.db と同じディレクトリにコピーし、REPO_ROOT を
#         編集するか、環境変数 K_ORIGINAL_REPO でクローンのルートを渡して実行:
#           K_ORIGINAL_REPO=/path/to/repo ./commit-songdata-push.sh
# =============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DB="${SCRIPT_DIR}/songdata.db"
TARGET_REL="data/songdata.db"

# 既定の REPO_ROOT（コピー先で編集して使う）
REPO_ROOT="${REPO_ROOT:-/path/to/test-CursorToSlack}"
if [[ -n "${K_ORIGINAL_REPO:-}" ]]; then
  REPO_ROOT="${K_ORIGINAL_REPO}"
fi

TARGET_DB="${REPO_ROOT}/${TARGET_REL}"

echo ""
echo "[commit-songdata-push] songdata.db をリポジトリへ反映します。"
echo "  ソース: ${SOURCE_DB}"
echo "  先  : ${TARGET_DB}"
echo ""

if [[ ! -d "${REPO_ROOT}/.git" ]]; then
  echo "ERROR: REPO_ROOT に .git がありません: ${REPO_ROOT}" >&2
  echo "  スクリプト内の REPO_ROOT を編集するか、K_ORIGINAL_REPO を設定してください。" >&2
  exit 1
fi

if [[ ! -f "${SOURCE_DB}" ]]; then
  echo "ERROR: 同一ディレクトリに songdata.db がありません: ${SOURCE_DB}" >&2
  exit 1
fi

if [[ ! -d "${REPO_ROOT}/data" ]]; then
  echo "ERROR: リポジトリに data がありません: ${REPO_ROOT}/data" >&2
  exit 1
fi

if ! command -v git >/dev/null 2>&1; then
  echo "ERROR: git が見つかりません。" >&2
  exit 1
fi

cp -f "${SOURCE_DB}" "${TARGET_DB}"

cd "${REPO_ROOT}"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: git 作業ツリーではありません。" >&2
  exit 1
fi

if [[ -z "$(git status --porcelain -- "${TARGET_REL}" 2>/dev/null || true)" ]]; then
  echo "変更がありません（コピー先は既に同一内容です）。push は行いません。"
  exit 0
fi

echo "----- git status（対象ファイル）-----"
git status -- "${TARGET_REL}"
echo "----- git diff --stat（対象ファイル）-----"
git diff --stat -- "${TARGET_REL}"
echo "----------------------------------------"

read -r -p "コミットして origin へ push しますか？ [y/N]: " ANS
if [[ "${ANS}" != "y" && "${ANS}" != "Y" ]]; then
  echo "中止しました（ファイルはコピー済みです。必要なら手元で git checkout 等してください）。"
  exit 0
fi

BRANCH="$(git rev-parse --abbrev-ref HEAD)"
if [[ -z "${BRANCH}" || "${BRANCH}" == "HEAD" ]]; then
  echo "ERROR: デタッチ HEAD など、push 可能なブランチではありません。" >&2
  exit 1
fi

git add -- "${TARGET_REL}"
git commit -m "chore(data): update songdata.db"
git push -u origin "${BRANCH}"

echo "完了しました。"
