---
title: "Agentic OS — Quick Reference Card"
category: system
date: 2026-07-13
tags: [agentic-os, cheatsheet]
---

# Agentic OS — Quick Reference Card

## Daily Commands

```bash
# Run the heartbeat (triage → conduct → execute → verify → gate)
cd E:/_Knowledge/ObsidianVault/agentic-os/loop && bash loop.sh

# Check what happened
cat memory/STATE.md

# Show trust tiers
bash scripts/trust-log.sh --render

# Check standing goals
bash verify-goals.sh

# Weekly cost audit
bash scripts/cost-check.sh --report
```

## Skill Tiers

| Runs | Pass Rate | Tier | What happens |
|------|-----------|------|--------------|
| <10 runs | any | **watch** | Draft only, waits for you |
| 10+ runs | 90-95% | **queue** | Queues for approval |
| 20+ runs | 95%+ | **auto** | Ships unattended |

## Exit Codes

| Code | Meaning | What to do |
|------|---------|------------|
| 0 | quiet or done | nothing to do |
| 1 | iter cap hit | check STATE.md |
| 2 | reroute | don't iterate on bad output |
| 3 | budget/tick cap | normal — budget working |
| 6 | refusal | simplify the prompt |

## The 5 Promises the System Makes

1. **Laws, not suggestions** — rules are numbers or `never`
2. **Nothing grades its own homework** — maker ≠ verifier
3. **Nothing goes unwatched** — standing goals run daily
4. **Cost is a design input** — tick cap keeps bill flat
5. **Autonomy is per-skill** — trust earned, not granted

## Karpathy + Agentic OS

```
Clip (browser) → 0-raw/ → kb-compile (skill)
                              ↓
                     wiki/concepts/ + wiki/entities/
                              ↓
              ← kb-report (on-demand) ← YOU ASK
              ← kb-healthcheck (cron Mon 9am)
                              ↓
                 Agentic OS loop.sh
                 (trust ledger + standing goals)
```

## Quick Skill Commands

```bash
# Log a pass
bash scripts/trust-log.sh kb-compile pass

# Log a failure (triggers ALERT if demoted)
bash scripts/trust-log.sh kb-compile fail

# Get tier for a skill
bash scripts/trust-log.sh --tier kb-compile

# Render full ledger
bash scripts/trust-log.sh --render
```