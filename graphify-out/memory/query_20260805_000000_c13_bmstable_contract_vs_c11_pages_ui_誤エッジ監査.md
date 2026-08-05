---
type: "audit"
date: "2026-08-05T00:00:00+00:00"
question: "C13（Bmstable JSON Contract）は C11（Pages UI Column Config）/C8 と実装経路で正しく分離されているか？誤エッジの監査"
contributor: "assistant"
outcome: "useful"
source_nodes: ["filtered_header.json - beatoraja header JSON", "filtered_data.json - beatoraja data rows", "beatoraja HTML 入口（docs/table/bmstable.html）", "level_order regeneration from final rows (K14+ folders)", "jbmstable-parser JSON output contract", "browser_rows.json meta (pages_ui, legends, table_rows_source_file)"]
---

# Q: 監査 — C13（Bmstable JSON Contract）と C11（Pages UI Column Config）の実装経路に誤エッジはないか？

## Background

前回クエリ（god doc ブリッジ解析, betweenness 0.402）で、`docs/github-actions-songdata-table-filter.md` が 5 コミュニティを束ねるブリッジであり、その degree 26（内 C0 CI/CD に 19 本）の偏りは「文書の横断性」であって「コードの結合度」ではない可能性が浮上。AST エッジ（`_origin=ast`）で実コードの import 網を検証した。

## AST 結合度の実測（filter_table.py, degree 56 / AST 54）

- AST 54 中 41 本が CROSS-community:
  - C4 beatoraja Row Compat: 9 import（`sanitize_chart_row_for_beatoraja`, `sync_header_level_order_from_beatoraja_rows` 等）
  - C5 Level Normalization: 8 import（`level_to_float`, `build_merged_custom_level_rows`, `merge_level_compare_rows`）
  - C2 Source Tables & Outputs: 8 import（`load_resolved_filter_config`, `normalize_source_tables`, `_resolve_config_pipeline`）
  - C3 beatoraja Song DB: 2 import（`resolve_sql_where`, `validate_sql_where`）
  - C15 Bmstable URL Resolve: 1（`test_bmstable_resolve.py`）
- **結論: godoc の「コード結合度が薄い」仮説は誤り。実装は C1 ハブとして dense に結合している。**

## 実装経路の実コード確認

filter_table.py `_write_outputs()` (L328-435):
- L351: `header_path = output_header_filename` → docs/table/filtered_header.json
- L367: `sanitize_header_for_beatoraja(new_header)`（C4）
- L399: `sync_header_level_order_from_beatoraja_rows(new_header, beatoraja_rows)`（C4）
- L406: `save_json(header_path, new_header)`

build_pages_table.py `main()` (L31-186):
- L98: `filtered = load_json(filtered_path)` — **ヘッダーは read しない**
- L68: `pages_ui_cfg = pages_ui_config_path`（C8 `load_pages_ui_config`）

check_browser_rows_pages_ui.py: `_io_helpers.load_json` のみで browser_rows を検証。

**→ C13（filtered_header）と C11（Pages UI Column Config）は実装経路上で独立。ヘッダーの唯一の消費者は beatoraja 本体（外部世界）。**

## 誤エッジの監査（C13 → C11/C8）

C13 の全 13 ノードから C11/C8 へのクロスエッジを精密に検索。

**結果: 該当 0 件。誤エッジなし。**

`docs_table_filtered_header_file` の全エッジ:
- `rationale_for → level_order regeneration` （C13 内、正当）
- `conceptually_related_to → Difficulty tables as chart metadata lists`（C13 内、正当）
- `references → beatoraja HTML 入口（docs/table/bmstable.html）`（C13 内、正当）

※ `filtered_header → docs_table_bmstable_bmstable_entry` は文書（docs/…）由来の HTML メタ。
実装フローではないが誤りではない。

## Outcome

- 誤エッジなしと確認。グラフの C13（beatoraja ドメイン契約）と C11（Pages 列設定）の分離は実装に忠実。
- C13 ↔ C11 を束ねるのは実装上の間接経路（C4 → beatoraja_rows 登録）のみ。読みやすさの観点では「C13 と C11 は結合」と誤読する誘因がある。

## Source Nodes