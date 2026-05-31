---
date: 2026-05-31
tags:
  - entity
  - project
  - ml
  - autonomous-research
  - llm-training
type: entity
status: active
---

# temp_autoresearch

Karpathy's autoresearch project — autonomous LLM training agent that modifies `train.py`, runs 5-minute experiments, and optimizes for validation loss.

## Overview

One day, frontier AI research used to be done by meat computers... This repo is the story of how it all began. The idea: give an AI agent a small but real LLM training setup and let it experiment autonomously overnight.

## Core Files

| File | Purpose |
|------|---------|
| `train.py` | The single file the agent edits (GPT model, Muon + AdamW optimizer, training loop) |
| `prepare.py` | Fixed constants, one-time data prep, runtime utilities (do not modify) |
| `program.md` | Baseline instructions for one agent (human edits this) |

## Key Design

- **Fixed 5-minute time budget** per experiment (wall clock)
- **val_bpb** (validation bits per byte) — lower is better, vocab-size-independent
- Agent only touches `train.py` — manageable scope, reviewable diffs
- Single GPU, self-contained, no distributed training

## Architecture

```
train.py edits:
├── Model: GPT with configurable DEPTH
├── Optimizer: Muon + AdamW
├── Attention: Flash-style patterns (L, SSSL)
└── Training: Fixed batch size, gradient accumulation
```

## Forks

- [autoresearch-macos](https://github.com/miolini/autoresearch-macos) — MacOS
- [autoresearch-mlx](https://github.com/trevin-creator/autoresearch-mlx) — MacOS MLX
- [autoresearch-win-rtx](https://github.com/jsegov/autoresearch-win-rtx) — Windows RTX
- [autoresearch-amd](https://github.com/andyluo7/autoresearch) — AMD

## Related

- [[wiki/entities/GitNexus]] — AI Git analysis tool
- [[wiki/concepts/Autonomous-Agent-Research]] — Concept page for autonomous research agents

## Source

`E:\_Knowledge\ObsidianVault\temp_autoresearch\`