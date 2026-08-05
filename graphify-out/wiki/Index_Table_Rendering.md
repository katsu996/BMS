# Index Table Rendering

> 22 nodes · cohesion 0.15

## Key Concepts

- **load_pages_ui_config()** (11 connections) — `tools/table-filter/pages_ui_json.py`
- **strip_jsonc_style_comments()** (8 connections) — `tools/table-filter/pages_ui_json.py`
- **test_pages_ui_json.py** (7 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **Path** (6 connections)
- **pages_ui_json.py** (6 connections) — `tools/table-filter/pages_ui_json.py`
- **.test_repo_default_index_table_syncs_with_config()** (5 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **TestStripJsonc** (5 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **_extract_default_index_table()** (4 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **TestLoadPagesUiConfig** (3 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **.test_load_file_with_comments()** (3 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **.test_repo_pages_ui_has_index_table()** (3 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **TestDefaultIndexTableSync** (2 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **.test_block_comment()** (2 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **.test_line_comment_not_inside_double_quoted()** (2 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **.test_line_comment_outside_string()** (2 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **.test_url_in_string_preserved()** (2 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **Any** (1 connections)
- **`docs/table/pages_ui_config.json` 用の読み込み。 標準の `json.load` は `//` 行コメントや `/* */`…** (1 connections) — `tools/table-filter/pages_ui_json.py`
- **ダブルクォート／シングルクォート文字列の外側だけで `//` と `/* */` を除去する。** (1 connections) — `tools/table-filter/pages_ui_json.py`
- **pages_ui_config を読み込み、辞書で返す。ルートがオブジェクトでなければ空辞書。** (1 connections) — `tools/table-filter/pages_ui_json.py`
- **JS の DEFAULT_INDEX_TABLE は設定 JSON の index_table と同期していること。 `pages-index-column-…** (1 connections) — `tools/table-filter/tests/test_pages_ui_json.py`
- **pages-index-column-runtime.js の `DEFAULT_INDEX_TABLE` リテラルを JSON として抽出する。…** (1 connections) — `tools/table-filter/tests/test_pages_ui_json.py`

## Relationships

- [GitHub Actions CI/CD](GitHub_Actions_CI-CD.md) (5 shared connections)
- [CI Validation Checks](CI_Validation_Checks.md) (1 shared connections)
- [beatoraja Row Compatibility](beatoraja_Row_Compatibility.md) (1 shared connections)

## Source Files

- `tools/table-filter/pages_ui_json.py`
- `tools/table-filter/tests/test_pages_ui_json.py`

## Audit Trail

- EXTRACTED: 75 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*