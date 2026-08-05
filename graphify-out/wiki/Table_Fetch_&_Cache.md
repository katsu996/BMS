# Table Fetch & Cache

> 8 nodes · cohesion 0.32

## Key Concepts

- **TestBmstableResolve** (5 connections) — `tools/table-filter/tests/test_bmstable_resolve.py`
- **object** (3 connections)
- **.test_resolve_from_directory_url_html()** (3 connections) — `tools/table-filter/tests/test_bmstable_resolve.py`
- **test_bmstable_resolve.py** (2 connections) — `tools/table-filter/tests/test_bmstable_resolve.py`
- **.test_resolve_from_html_meta()** (2 connections) — `tools/table-filter/tests/test_bmstable_resolve.py`
- **.test_resolve_json_body_without_json_suffix()** (2 connections) — `tools/table-filter/tests/test_bmstable_resolve.py`
- **末尾が / のときも HTML として bmstable を解決する（.json 誤認を防ぐ）。** (1 connections) — `tools/table-filter/tests/test_bmstable_resolve.py`
- **.test_json_url_passthrough()** (1 connections) — `tools/table-filter/tests/test_bmstable_resolve.py`

## Relationships

- [Core Filter Pipeline](Core_Filter_Pipeline.md) (1 shared connections)

## Source Files

- `tools/table-filter/tests/test_bmstable_resolve.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*