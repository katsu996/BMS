import json
import re
import tempfile
import unittest
from pathlib import Path

from pages_ui_json import load_pages_ui_config, strip_jsonc_style_comments


class TestStripJsonc(unittest.TestCase):
    def test_line_comment_outside_string(self) -> None:
        s = '{"a": 1, // c\n "b": 2}'
        self.assertEqual(json.loads(strip_jsonc_style_comments(s)), {"a": 1, "b": 2})

    def test_line_comment_not_inside_double_quoted(self) -> None:
        s = '{"a": "http://x", "b": 2}'
        self.assertEqual(json.loads(strip_jsonc_style_comments(s)), {"a": "http://x", "b": 2})

    def test_block_comment(self) -> None:
        s = '{"a": 1 /* x */ , "b": 2}'
        self.assertEqual(json.loads(strip_jsonc_style_comments(s)), {"a": 1, "b": 2})

    def test_url_in_string_preserved(self) -> None:
        s = '{"url": "https://example.com/a//b"}'
        self.assertEqual(json.loads(strip_jsonc_style_comments(s)), {"url": "https://example.com/a//b"})


class TestLoadPagesUiConfig(unittest.TestCase):
    def test_load_file_with_comments(self) -> None:
        body = """// top
{
  "version": 1,
  "column_widths": {
    // "t:level": "6ch",
    "t:title": "40ch"
  },
  "column_visible_defaults": {
    "table": { // inline
      "id": false
    },
    "db": {}
  }
}
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".json") as tmp:
            tmp.write(body)
            path = tmp.name
        try:
            d = load_pages_ui_config(path)
        finally:
            Path(path).unlink(missing_ok=True)
        self.assertEqual(d["version"], 1)
        self.assertEqual(d["column_widths"]["t:title"], "40ch")
        self.assertNotIn("t:level", d["column_widths"])
        self.assertEqual(d["column_visible_defaults"]["table"]["id"], False)

    def test_repo_pages_ui_has_index_table(self) -> None:
        repo = Path(__file__).resolve().parents[3] / "docs" / "table" / "pages_ui_config.json"
        d = load_pages_ui_config(str(repo))
        it = d.get("index_table")
        self.assertIsInstance(it, dict)
        self.assertIsInstance(it.get("table_column_order"), list)
        self.assertIsInstance(it.get("db_column_order"), list)
        self.assertIsInstance(it.get("column_labels"), dict)
        self.assertIsInstance(it.get("ir_subcolumns"), list)
        self.assertGreaterEqual(len(it["ir_subcolumns"]), 1)
        for col in it["ir_subcolumns"]:
            self.assertIn("colgroup_key", col)
            self.assertIn("href_template", col)
        cc = it.get("chart_column")
        self.assertIsInstance(cc, dict)
        self.assertEqual(cc.get("colgroup_key"), "chart")
        trail = it.get("trailing_table_columns")
        self.assertIsInstance(trail, list)
        self.assertEqual(trail, [])
        lead = it.get("leading_table_columns")
        self.assertIsInstance(lead, list)
        self.assertEqual(lead, ["custom_level"])
        tco = it.get("table_column_order")
        self.assertIsInstance(tco, list)
        self.assertGreater(len(tco), 0)
        self.assertEqual(tco[0], "custom_level")


def _extract_default_index_table(js_path: Path) -> dict:
    """pages-index-column-runtime.js の `DEFAULT_INDEX_TABLE` リテラルを JSON として抽出する。

    このリテラルは JSON 互換（キー・文字列はダブルクォート）のため、
    文字列を考慮したブレースマッチングで `{...}` を切り出して `json.loads` する。
    """
    text = js_path.read_text(encoding="utf-8")
    marker = "DEFAULT_INDEX_TABLE ="
    idx = text.find(marker)
    if idx < 0:
        raise AssertionError("pages-index-column-runtime.js に DEFAULT_INDEX_TABLE が見つかりません")
    start = text.find("{", idx)
    if start < 0:
        raise AssertionError("DEFAULT_INDEX_TABLE の { が見つかりません")
    depth = 0
    in_string = False
    escape = False
    i = start
    n = len(text)
    while i < n:
        c = text[i]
        if in_string:
            if escape:
                escape = False
            elif c == "\\":
                escape = True
            elif c == '"':
                in_string = False
        else:
            if c == '"':
                in_string = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
        i += 1
    if depth != 0:
        raise AssertionError("DEFAULT_INDEX_TABLE の閉じ括弧が見つかりません")
    literal = text[start : i + 1]
    # JS オブジェクトリテラルのキーはアンクォート（table_column_order: [...]）のため、
    # `{` / `,` に続く識別子キーをダブルクォートして JSON として解釈できるようにする。
    literal = re.sub(r"([{,]\s*)([A-Za-z_$][A-Za-z0-9_$]*)(\s*:)", r'\1"\2"\3', literal)
    loaded = json.loads(literal)
    if not isinstance(loaded, dict):
        raise AssertionError("DEFAULT_INDEX_TABLE がオブジェクトではありません")
    return loaded


class TestDefaultIndexTableSync(unittest.TestCase):
    def test_repo_default_index_table_syncs_with_config(self) -> None:
        """JS の DEFAULT_INDEX_TABLE は設定 JSON の index_table と同期していること。

        `pages-index-column-runtime.js` は古い browser_rows.json 用のフォールバックとして
        設定と同じ列定義を持つ必要がある（docs/pages-ui-config.md「同期しておくこと」）。
        設定を編集したら必ずこちらも合わせる。
        """
        repo = Path(__file__).resolve().parents[3]
        d = load_pages_ui_config(str(repo / "docs" / "table" / "pages_ui_config.json"))
        config_index_table = d.get("index_table")
        self.assertIsInstance(config_index_table, dict)
        js_default = _extract_default_index_table(repo / "docs" / "assets" / "pages-index-column-runtime.js")
        self.assertEqual(config_index_table, js_default)
