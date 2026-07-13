# Agentic OS Constitution

**Version:** 1.0
**Vault:** `E:/_Knowledge/ObsidianVault`
**Principles:** Laws, not suggestions · Deterministic gates · Nothing grades its own homework

---

## Three Immutable Laws

### Law 1: Laws, Not Suggestions
> Any rule that cannot be expressed as a number, a hard "never", or a verifiable command **does not exist**.
> - Vague guidance ("be thorough", "think carefully") is ignored.
> - Every constraint must have a `verify.sh` that exits 0 on pass, non-zero on fail.
> - The model cannot negotiate with a bash exit code.

### Law 2: Nothing Grades Its Own Homework
> The component that produces output **never** validates it.
> - `execute.sh` writes → `verify.sh` reads → `gate.sh` decides.
> - No shared memory, no in-context self-critique, no "let me check my work".
> - Separate processes, separate contexts, separate token budgets.

### Law 3: Deterministic Gates Over Probabilistic Judgment
> If a check can be a script, it **must** be a script.
> - LLM-as-judge only where no script can exist (semantic equivalence, tone, creativity).
> - Every LLM judge has a fallback script that is stricter.
> - Token budget for verification is capped and tracked.

---

## System Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  TRIAGE     │────▶│  CONDUCT    │────▶│  EXECUTE    │────▶│  VERIFY     │
│  (router)   │     │  (planner)  │     │  (worker)   │     │  (gate)     │
└─────────────┘     └─────────────┘     └─────────────┘     └──────┬──────┘
                                                                     │
                    ┌─────────────┐     ┌─────────────┐              │
                    │  GATE       │◀────│  TRUST      │◀─────────────┘
                    │  (promote/  │     │  LEDGER     │
                    │   demote)   │     │  (tiers)    │
                    └─────────────┘     └─────────────┘
```

### Component Responsibilities

| Component | Role | Verification | Trust Tier |
|-----------|------|--------------|------------|
| **triage.sh** | Classifies incoming work: `auto` / `queue` / `watch` / `reject` | Output schema validation | N/A (router) |
| **conduct.sh** | Produces execution plan with explicit checkpoints | `verify-plan.sh` checks schema + constraints | Auto |
| **execute.sh** | Runs the plan, emits artifacts to `workers/<id>/` | None (producer) | Queue/Watch |
| **verify.sh** | Runs all `verify-*.sh` scripts, aggregates results | Exit code = 0 → PASS | Auto |
| **gate.sh** | Promotes/demotes worker in trust ledger | Trust ledger append-only | N/A (arbiter) |

---

## Trust Tiers (Immutable)

| Tier | Name | Autonomy | Verification | Max Budget/Run |
|------|------|----------|--------------|----------------|
| **T0** | `auto` | Full loop: triage → conduct → execute → verify → gate | `verify.sh` only | $0.50 |
| **T1** | `queue` | Conduct → Execute → Verify (human gates triage) | `verify.sh` + human approve | $2.00 |
| **T2** | `watch` | Execute only (human conducts) | `verify.sh` + human approve | $5.00 |
| **T3** | `reject` | No autonomy | N/A | $0.00 |

**Promotion:** 5 consecutive PASS at current tier → eligible for next tier
**Demotion:** 1 FAIL → immediate demotion to previous tier
**New workers** start at `watch` (T2)

---

## Budget Enforcement (Hard Limits)

| Limit | Value | Enforcement |
|-------|-------|-------------|
| **Daily token cap** | 500,000 tokens | `budget/daily.sh` kills loop on breach |
| **Per-run cap (T0)** | 50,000 tokens | `budget/per-run.sh` in execute |
| **Per-run cap (T1)** | 200,000 tokens | `budget/per-run.sh` in execute |
| **Per-run cap (T2)** | 500,000 tokens | `budget/per-run.sh` in execute |
| **Monthly $ cap** | $50.00 | `budget/monthly.sh` cron at 00:00 |

**No exceptions.** When cap hits, loop exits with code 42 (BUDGET_EXCEEDED).

---

## Standing Goals (The "Employee" Contract)

The system maintains **standing goals** — persistent objectives that survive sessions.
Each goal has:
- `id`: unique slug
- `spec.md`: success criteria (machine-checkable where possible)
- `verify.sh`: exits 0 iff goal is satisfied
- `cadence`: `daily` | `weekly` | `event-driven`
- `tier`: minimum trust tier required

**Daily verification:** `goals/verify-all.sh` runs at 06:00, logs to `memory/goals.log`
**Drift detection:** `goals/drift-check.sh` compares current state vs. spec, alerts on divergence.

---

## Memory Model

| Store | Path | Purpose | Retention |
|-------|------|---------|-----------|
| **Working** | `workers/<id>/` | Per-run artifacts, logs, plan | 7 days |
| **Trust Ledger** | `trust/ledger.jsonl` | Append-only promotion/demotion log | Permanent |
| **Goals** | `goals/<id>/` | Standing goal specs + verification | Permanent |
| **Budget** | `budget/usage.jsonl` | Token/$ usage per run | 90 days |
| **Drift** | `memory/drift.log` | Goal drift alerts | 30 days |

**No shared context between runs.** Each run gets fresh context + relevant memory reads.

---

## Loop Protocol (The Heartbeat)

```
while true; do
  work=$(triage.sh)                    # → {id, tier, spec, budget}
  [[ -z "$work" ]] && sleep 60 && continue
  
  plan=$(conduct.sh "$work")           # → plan.json (validated)
  verify-plan.sh "$plan" || exit 1
  
  execute.sh "$plan"                   # → artifacts in workers/<id>/
  verify.sh "$work" "$plan"            # → PASS/FAIL + evidence
  
  gate.sh "$work" "$plan"              # → updates trust ledger
  
  budget/daily.sh check || exit 42
done
```

**Checkpoint after each stage.** If any stage fails, loop iteration ends, worker stays at current tier.

---

## Forbidden Patterns (Enforced by verify.sh)

| Pattern | Detection | Penalty |
|---------|-----------|---------|
| "I'll be thorough" / "comprehensive" | grep in plan | FAIL |
| No explicit success criteria in plan | `verify-plan.sh` schema | FAIL |
| Execute without verified plan | Missing `plan.json` | FAIL |
| Verify without evidence artifacts | `verify.sh` checks file exists | FAIL |
| Self-evaluation in execute output | grep "I verified" | FAIL |
| Budget untracked | `budget/per-run.sh` missing | FAIL |

---

## Quick Reference: Commands

```bash
# Start the loop (background)
make run

# One-shot: process next work item
make once

# Check trust ledger
make trust

# Verify all standing goals
make goals

# Budget status
make budget

# View drift log
make drift

# Emergency stop
make stop
```

---

## Amendment Protocol

This constitution can only be amended by:
1. Human writes proposed change to `AGENTS.proposed.md`
2. `verify-constitution.sh` validates no law violations
3. Human approves → `mv AGENTS.proposed.md AGENTS.md`
4. `make reset-trust` (all workers demoted to `watch`)

**No self-amendment.** The system cannot modify its own laws.