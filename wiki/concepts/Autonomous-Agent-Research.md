---
date: 2026-05-31
tags:
  - concept
  - ai
  - autonomous
  - ml
  - research
type: concept
status: active
---

# Autonomous Agent Research

The practice of AI agents conducting research independently — modifying code, running experiments, evaluating results, and iterating without human intervention.

## Examples in Vault

1. **[[wiki/entities/temp_autoresearch]]** — Karpathy's autoresearch
   - Fixed 5-minute experiment budget
   - val_bpb metric (lower = better)
   - Single file (`train.py`) for agent modifications
   - Wake up to experimental results

2. **[[wiki/entities/genericagent]]** — Python autonomous agent
   - `BaseHandler` class with dispatch loop
   - Multiple frontends (desktop, Qt, Streamlit, DingTalk, QQ)
   - Tool callbacks for extensibility

3. **[[wiki/entities/graphify-repo]]** — Knowledge graph extraction
   - Autonomous extraction from documents and code
   - Clustering and scoring algorithms
   - Multiple export formats

## Key Patterns

| Pattern | Description |
|---------|-------------|
| Fixed time budget | Prevents runaway experiments |
| Single modification target | Keeps diffs manageable |
| Objective metric | val_bpb, loss, accuracy |
| Iterator loop | Modify → Run → Evaluate → Keep/Discard → Repeat |

## Autonomy Spectrum

```
Human in loop                    Fully autonomous
      ↓                               ↓
  Human reviews each step    →    Agent runs overnight
  Human approves changes     →    Changes auto-applied
  Manual experiment launch   →    Scheduled/triggered runs
```

## Related Concepts

- [[wiki/concepts/Knowledge-Graph-Extraction]] — Extracting structured knowledge from unstructured sources
- [[wiki/concepts/AI-First-Workflow]] — AI-first vault organization

## Source Projects

- `temp_autoresearch/` — ML training automation
- `genericagent/` — General-purpose agent framework
- `graphify-repo/` — Knowledge extraction

## Tags

#autonomous #ai-research #ml #agent-systems