---
type: "query"
date: "2026-08-03T13:25:58.081722+00:00"
question: "beatoraja baseline と LR2oraja / Endless Dream フォークの差と、このツールへの影響"
contributor: "graphify"
outcome: "useful"
source_nodes: ["beatoraja (exch-bms2) baseline player", "LR2oraja - LR2-gauge fork (wcko87)", "LR2oraja Endless Dream - QoL fork (seraxis)"]
---

# Q: beatoraja baseline と LR2oraja / Endless Dream フォークの差と、このツールへの影響

## Answer

Expanded from original query via vocab: [beatoraja, lr2oraja, fork, baseline, player, dream]. Graph (c9): fork derivation tree hyperedge [EXTRACTED 1.00] beatoraja (exch-bms2) -> LR2oraja (wcko87) -> Endless Dream (seraxis), all three linked by references edges; baseline conceptually_related_to[INFERRED] SQLiteSongDatabaseAccessor.java and references SQL virtual folder (folder/default.json + CommandBar). Doc docs/bms/beatoraja-vs-lr2oraja-derivatives.md: forks differ in gauge/judgment (LR2-style), LN early-release, TOTAL formula, IR support (LR2oraja not IR-oriented), Endless Dream adds QoL (downloaders, GBATTLE, osu, performance). CRITICAL for this tool: SQL virtual folder + songdata.db concepts identical across forks (JAR swap install), so minbpm != maxbpm and all sql_where semantics apply equally to all three; only IR-related UI matters differently.

## Outcome

- Signal: useful

## Source Nodes

- beatoraja (exch-bms2) baseline player
- LR2oraja - LR2-gauge fork (wcko87)
- LR2oraja Endless Dream - QoL fork (seraxis)