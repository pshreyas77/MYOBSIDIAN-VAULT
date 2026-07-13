---
title: "How to Use the Agentic OS"
category: system
date: 2026-07-13
tags: [agentic-os, guide, workflow]
related: ["AGENTS.md", "RUNBOOK.md", "Agentic-OS-Status-2026-07-13"]
---

# How to Use the Agentic OS

This is not a chatbot. It is a system that runs while you sleep.

---

## The Two Modes

### Mode 1: On-Demand (no setup required)
Use the kb-* skills directly. No API key, no loop, no cron. Just ask.

### Mode 2: Autonomous Loop (needs setup)
The heartbeat runs every weekday morning, compiles new raw material, checks health, and files reports — all without you.

---

## Mode 1: On-Demand Skills

### 1. Clip → Compile → Report → Healthcheck

```
You (human)                    System
─────────────────────────────────────────────────────
Clip web page to 0-raw/   →    (browser extension)

Ask: compile knowledge     →    kb-compile skill
                              creates wiki/concepts/ and wiki/entities/

Ask: research question    →    kb-report skill
                              writes report to 06 - OUTPUTS/reports/

Cron (Monday 9am)         →    kb-healthcheck skill
                              writes health report to 06 - OUTPUTS/healthchecks/
```

### Quick-Start Commands (say these to Claude)

```
"Compile all my raw sources into wiki pages — use kb-compile"

"Generate a research report on [topic] using only my wiki — use kb-report"

"Run a health check on my knowledge base — use kb-healthcheck"

"Use Obsidian to find all notes mentioning [topic] and summarize each"
```

### What Each Skill Does

| Skill | Input | Output |
|-------|-------|--------|
| `kb-compile` | `0-raw/*.md` | `wiki/concepts/*.md`, `wiki/entities/*.md`, updated `wiki/index.md` |
| `kb-report` | your question + `wiki/` | `06 - OUTPUTS/reports/YYYY-MM-DD-topic.md` |
| `kb-healthcheck` | full vault scan | `06 - OUTPUTS/healthchecks/healthcheck-YYYY-MM-DD.md` |

---

## Mode 2: Autonomous Loop

### One-Time Setup

**Step 1: Set your OpenRouter API key**

```bash
export OPENROUTER_API_KEY=sk-or-your-key-here
# Add to ~/.bashrc or ~/.hermes/.env to persist
```

**Step 2: Point at your vault (or any repo)**

```bash
export TARGET_REPO=E:/_Knowledge/ObsidianVault
```

**Step 3: Run the heartbeat once by hand**

```bash
cd E:/_Knowledge/ObsidianVault/agentic-os/loop
bash loop.sh
```

Expected output on a quiet day:
```
quiet
```
(Exit 0, costs ~$0 since hy3:free is used everywhere)

**Step 4: Check the state**

```bash
cat memory/STATE.md       # what happened last run
bash scripts/trust-log.sh --render   # skill tier table
bash verify-goals.sh      # standing goal check
bash scripts/cost-check.sh --report   # weekly spend
```

### Daily Operations (pick one)

```bash
make tick        # run the heartbeat once  (or: bash loop.sh)
make queue       # show queued/failed items
make trust       # render the trust ledger
make audit       # show this week's spend
make goals       # verify all standing goals
```

### The 30-Day Gradual Trust Schedule

| Week | What you do | Goal |
|------|-------------|------|
| 1 | Run `make tick` by hand every morning. Read STATE.md. | 3 runs route exactly as you would |
| 2 | Turn on cron. Review queue with coffee. Trust ledger feeds decisions. | 2 skills cross 20 logged runs |
| 3 | Let best-proven skill ship unattended. Watch audit match formula. | 1 week, zero interventions |
| 4 | Compost sign-off. Delete one rule or skill. | Nothing broke |

---

## The Skills in the Loop

The Agentic OS loop has 4 built-in skills. They start at **watch** tier and earn autonomy:

### Skill Tiers

| Tier | Meaning | What happens |
|------|---------|--------------|
| **watch** | <10 runs OR <90% pass | Draft only, queues for you |
| **queue** | 10+ runs, 90-95% pass | Queues for approval |
| **auto** | 20+ runs AND 95%+ pass | Ships unattended |

### Skills That Start in the Loop

| Skill | What it does | Earns trust by |
|-------|-------------|----------------|
| `kb-compile-skill` | Converts raw → wiki | compiling without errors |
| `kb-report-skill` | Answers from wiki | reports passing verify |
| `kb-healthcheck-skill` | Audits KB integrity | health reports accurate |
| `fix-lint-debt` | Cleans lint warnings | lint stays clean |
| `bump-deps` | Safe dependency bumps | deps stay stable |
| `fix-flaky-test` | Stabilizes CI flakiness | tests run clean |
| `triage-issues` | Labels and routes issues | issues properly labeled |

---

## The Trust Ledger

Every skill run is logged. After each run:

```bash
bash scripts/trust-log.sh <skill-name> pass   # skill succeeded
bash scripts/trust-log.sh <skill-name> fail    # skill failed
```

After 20 passes + 95% rate → **auto** tier (ships without asking)

Example — seed the kb-compile skill:

```bash
# Simulate 20 runs with 1 failure (19/20 = 95% → auto tier)
for i in $(seq 1 19); do bash scripts/trust-log.sh kb-compile pass; done
bash scripts/trust-log.sh kb-compile fail    # one failure
bash scripts/trust-log.sh kb-compile pass    # back to pass
bash scripts/trust-log.sh --tier kb-compile  # should say "auto"
```

---

## Standing Goals

These are invariants that are checked **every single day, forever**.

Currently active:

| Goal | Predicate | What it watches |
|------|-----------|----------------|
| `loop-pipeline-green` | `bash guardrails/verify.sh` exits 0 | The gate itself stays green |

Add a new standing goal — create `goals/my-goal.md`:

```markdown
predicate: test -f "E:/_Knowledge/ObsidianVault/06 - OUTPUTS/reports/$(date +%Y-%m)*.md"
born: 2026-07-13
status: satisfied
on-violation: wake me. Do not auto-fix.
retire-when: the research project ends.
```

The sentinel (`verify-goals.sh`) runs daily and alerts if anything is VIOLATED.

---

## The Contract (What the Loop Can and Cannot Do)

**Acts alone (no approval needed):**
- Draft branches
- Fix lint/test debt
- Update STATE.md
- Label issues
- Compile raw → wiki

**Queues for you:**
- Auth, payments, migrations
- Anything touching secrets
- Any diff >400 lines
- Any skill not at **auto** tier

**Wakes you up immediately:**
- A check fails twice on the same item
- The router swapped models mid-run
- Daily budget breached
- A standing goal is violated
- Anything asks for a secret

---

## The Memory Files

| File | What it tracks |
|------|---------------|
| `memory/STATE.md` | Last run output, decisions made |
| `memory/trust.tsv` | Per-skill runs/pass/tier |
| `memory/goal-ledger.tsv` | Daily goal check results |
| `memory/usage.log` | Cost per seat per day |
| `memory/ticks.today` | Tick count vs daily cap |

---

## Making the Loop Work on Your Vault

The loop reads TARGET_REPO and does git operations there. Set it to your vault:

```bash
export TARGET_REPO=E:/_Knowledge/ObsidianVault
```

Since your vault already has raw/, wiki/, and 06 - OUTPUTS/, the loop's kb-compile-skill will work directly.

---

## The karpathy Method Integration

The Agentic OS and the Karpathy Method are complementary:

```
KARPATHY METHOD (human writes, LLM compiles)
  Clip → 0-raw/ → kb-compile → wiki/ → kb-report → reports/
                                    ↓
                              kb-healthcheck
                                    ↓
AGENTIC OS (LLM runs, human monitors)
  loop.sh → kb-compile-skill → trust ledger → standing goals
```

The Karpathy method is the **input layer** — filling raw/ with content.
The Agentic OS is the **automation layer** — running kb-compile and health checks on schedule.

---

## Common Tasks

**Start using the system today (no setup):**
1. Clip interesting articles to `0-raw/` using the Obsidian Web Clipper
2. Ask Claude: "Compile my raw sources using kb-compile"
3. Ask Claude: "Generate a report on [your topic] using kb-report"
4. Done — answers are saved as files, not chat bubbles

**Graduate to autonomous mode (after filling raw/):**
1. `export OPENROUTER_API_KEY=sk-or-...`
2. `export TARGET_REPO=E:/_Knowledge/ObsidianVault`
3. `cd .../agentic-os/loop && bash loop.sh`
4. Watch STATE.md fill up

**Add a new skill:**
1. Create `loop/skills/my-skill/SKILL.md` with frontmatter (name, description, never, done_when)
2. The conductor reads skills from that directory automatically
3. Log passes/fails with `scripts/trust-log.sh my-skill pass|fail`
4. After 20 runs at 95% → auto tier

**Fix a failing skill:**
1. `cat memory/STATE.md | grep FAILED` — find what broke
2. `bash scripts/trust-log.sh --render` — check the tier
3. Read the skill's last 3 failures from STATE.md
4. Fix the spec in SKILL.md
5. Resume logging