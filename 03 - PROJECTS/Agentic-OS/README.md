# Agentic OS

A system for autonomous AI-driven development using Claude Fable 5.

## Quick Start

1.  **Configure:** Edit `CLAUDE.md` and `loop/contract.md` for your project.
2.  **Verify:** Run `chmod +x loop/guardrails/verify.sh` and confirm it passes.
3.  **Tick:** Run `make tick` to start the first loop.
4.  **Trust:** Run `make trust` to view the trust ledger.

## Structure

- `CLAUDE.md`: The constitution.
- `loop/`: The heartbeat.
  - `contract.md`: Autonomy boundaries.
  - `triage.md`: Cheap signal reader.
  - `conductor.md`: Expense decision maker.
  - `workers/`: Skill definitions.
  - `guardrails/`: Deterministic gates.
  - `scripts/`: Trust and cost ledgers.
  - `skills/`: Per-skill configurations.
  - `memory/`: Runtime state.
  - `goals/`: Standing invariants.
- `Makefile`: Simple commands.

## 30-Day Trust Schedule

| Week | Level | Goal |
|---|---|---|
| 1 | L1 Report | Run by hand, verify routing |
| 2 | L2 Draft | Cron on, review queue |
| 3 | L3 Ship | Best skill runs unattended |
| 4 | L4 Grow | Compost, propose new skills |
