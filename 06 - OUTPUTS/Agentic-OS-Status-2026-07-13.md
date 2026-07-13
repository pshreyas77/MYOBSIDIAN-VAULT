---
title: "Agentic OS — System Status"
date: "2026-07-13"
status: built-ready
flow: Karpathy method + Agentic OS + Obsidian vault
---

# Agentic OS Status — 2026-07-13

## What's Built

### Agentic OS (Fable 5 Pattern) — `agentic-os/`
All 8 Builds present:

| Build | Layer | Status | File |
|-------|-------|--------|------|
| 1 | Constitution | ✓ | `agentic-os/AGENTS.md` |
| 2 | Walls & Gate | ✓ | `agentic-os/contract.md` |
| 3 | Heartbeat Loop | ✓ | `agentic-os/loop/loop.sh` |
| 4 | Trust Ledger | ✓ | `agentic-os/loop/scripts/trust-log.sh` |
| 5 | Standing Goals | ✓ | `agentic-os/loop/verify-goals.sh` |
| 6 | Budget | ✓ | `agentic-os/loop/scripts/cost-check.sh` |
| 7 | Optional Loops | ✓ | compost + sparring + quorum |
| 8 | Ops/Makefile | ✓ (partial) | scripts wired, no Makefile |

### Karpathy Method Skills — `~/.hermes/skills/knowledge-management/`

| Skill | Status | Location |
|-------|--------|----------|
| `kb-compile` | ✓ | `~/.hermes/skills/knowledge-management/kb-compile/SKILL.md` |
| `kb-report` | ✓ | `~/.hermes/skills/knowledge-management/kb-report/SKILL.md` |
| `kb-healthcheck` | ✓ | `~/.hermes/skills/knowledge-management/kb-healthcheck/SKILL.md` |

### Cron Jobs

| Job | Schedule | Status |
|-----|----------|--------|
| kb-weekly-healthcheck | Mon 09:00 IST | ✓ enabled |
| Night Shift Scout | Daily 23:30 IST | ✓ |
| Night Shift Refinery | Daily 03:00 IST | ✓ |
| Night Shift Editor | Daily 06:00 IST | ✓ |
| Night Shift Audit | Sun 22:00 IST | ✓ |
| History Watchdog Scout | Mon 02:00 IST | ✓ |
| Vault Auto-Commit | Daily 22:00 IST | ✓ |

## What Needs Doing

### 1. Set `OPENROUTER_API_KEY`
The Agentic OS loop uses `call.sh` which talks to OpenRouter. Without the key, the heartbeat won't run.
```bash
export OPENROUTER_API_KEY=sk-or-<your-key>
# Add to ~/.bashrc or ~/.hermes/.env for persistence
```

### 2. Point `TARGET_REPO` at a real repo
The loop does git worktree operations. Currently unset.
```bash
export TARGET_REPO=/path/to/your-project-repo
# For vault-only agentic ops: TARGET_REPO=E:/_Knowledge/ObsidianVault
```

### 3. Install Obsidian Local REST API Plugin
MCP-Obsidian integration requires the plugin:
- Obsidian Settings → Community Plugins → "Local REST API" → Install → Enable
- Copy API key → update `~/.hermes/mcp/mcp-obsidian.json`

### 4. Populate `0-raw/` with source material
The kb-compile skill has nothing to compile yet. Fill it with:
- Web-clipped articles
- Papers, transcripts, repos
- Any research material

### 5. Seed the trust ledger
Run skills manually a few times to build trust before auto mode:
```bash
cd E:/_Knowledge/ObsidianVault/agentic-os/loop
bash scripts/trust-log.sh kb-compile pass   # repeat 20x with 19 pass, 1 fail pattern
bash scripts/trust-log.sh --render
```

## How They Fit Together

```
CLIP (human) → 0-raw/       → kb-compile → wiki/concepts/ + wiki/entities/
                                  ↓
                            Obsidian Graph View (human reads)
                                  ↓
QUESTION (human)            → kb-report   → 06 - OUTPUTS/reports/
                                  ↓
                          kb-healthcheck  → 06 - OUTPUTS/healthchecks/
                            (cron: Mon 09:00)
                                  ↓
                          Agentic OS loop → trust ledger + standing goals
```

## First Run Commands

```bash
# 1. Compile knowledge base (one-time seed)
/obsidian kb-compile --limit 10

# 2. Generate a report
/obsidian kb-report "Based on my wiki, what are the key themes in Indian anti-caste movements?"

# 3. Dry-run health check
/obsidian kb-healthcheck --report-only

# 4. Start Agentic OS heartbeat (with OPENROUTER_API_KEY set)
cd E:/_Knowledge/ObsidianVault/agentic-os/loop && bash loop.sh

# 5. Verify standing goals
cd E:/_Knowledge/ObsidianVault/agentic-os/loop && bash verify-goals.sh
```

## For Claude Code / Future Session

This vault is now a Karpathy-style "living wiki maintained by LLM" with an Agentic OS layer that provides:
- **Trust tiers**: auto/queue/watch per skill
- **Budget cap**: $5/day, 50 ticks/day
- **Two ledgers**: trust (workers) and goals (work)
- **Three laws**: no self-grading, deterministic gates, numeric constraints
- **Compost**: weekly failure review → new laws/skills/goals

The full pipeline: clip → compile → browse → query → report → healthcheck → goals → trust.