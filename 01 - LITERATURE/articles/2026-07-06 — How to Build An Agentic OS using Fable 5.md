---
date: 2026-07-06
type: literature
tags:
  - article
  - ai
  - fable-5
  - agentic-os
  - productivity
  - builders-guide
source: "Twitter/X Post (Author Unknown)"
url: "https://x.com/[placeholder]/status/[placeholder]"
ai-first: true
confidence: high
---

## For future Claude
This is a comprehensive, technical builder's guide for creating an "Agentic OS" using Claude Fable 5. The article details an 8-build system (from configuration to autonomous operation) designed to manage tasks, verify work, and control costs. It is a high-level, strategic framework for leveraging advanced AI models as a virtual workforce.

## Core Concept: The Agentic OS
A system built on top of Claude Fable 5 to create a self-managing, autonomous workflow. The goal is to move beyond simple prompting to a structured, verifiable, and cost-controlled AI-driven operation.

## Key Principles
- **Laws, not tips:** Every rule is a number, a "never," or a checkable command.
- **Separation of Powers:** The planner (conductor), worker, verifier, and gate are four different parties.
- **Continuous Verification:** Nothing that passed once goes unwatched. Finished work becomes a re-verified invariant.

## The 8-Build System

### BUILD 0: Configure the Engine
- **Model:** `claude-fable-5`
- **Context/Output:** 1M tokens / up to 128k output
- **Price:** $10/M in, $50/M out
- **Thinking:** Adaptive, always on. `thinking: {type:"disabled"}` is REJECTED.
- **Effort:** `low`, `medium`, `high`, `xhigh`, `max`. `high` is the default.
- **Key Rules:**
  - `max_tokens` is a hard cap on thinking + response text. Must be set large (start at 64k) at `high` and `xhigh` effort.
  - Refusals are HTTP 200. Check for `stop_reason: "refusal"`.
  - Never ask Fable to echo its reasoning (triggers `reasoning_extraction` refusal).
  - Prompts must use official anti-overplanning, anti-gold-plating, and grounded progress claims language.

### BUILD 1: The Constitution (CLAUDE.md)
- A short, strict ruleset under 150 lines.
- Contains "NEVER" laws, a dispatch matrix for routing tasks to models, word definitions, and a definition of "done."

### BUILD 2: Walls and Gate (contract.md & verify.sh)
- **`contract.md`**: Defines what the AI can do autonomously (e.g., draft PRs), what it must queue for human approval (e.g., `auth`, `payments`), and what must wake the human (e.g., `verify` fails twice).
- **`verify.sh`**: A bash script that holds the final vote. It must exit 0. Example: runs `npm run typecheck`, `npm test`, and `npm run lint`.

### BUILD 3: The Heartbeat (loop.sh)
- The core autonomous loop.
- **`triage.md`**: A cheap AI reads recent commits/issues and outputs a one-line status (e.g., `actionable`, `quiet`).
- **`conductor.md`**: The expensive AI (Fable, `xhigh` effort) picks the single highest-value task. It does not execute, only plans and outputs a JSON work order.
- **`workers/implement.md`**: A cheap AI executes the work order.
- **`workers/verify.md`**: A fresh-context AI verifies the work against the specification. It gives a simple `PASS` or `FAIL`.

### BUILD 4: The Trust Ledger (trust-log.sh)
- A TSV file that tracks the pass/fail rate for each "skill" (a type of recurring task).
- **Tier System:**
  - **`auto`**: 20+ runs and 95%+ pass rate. Ships unattended.
  - **`queue`**: Verified drafts wait for human review.
  - **`watch`**: Under 10 runs or under 90% pass rate. Draft-only.
- Skills are defined in `loop/skills/<name>/SKILL.md`.

### BUILD 5: Standing Goals + Goal Ledger
- **`goals/<name>.md`**: A file for each finished task. It contains a machine-checkable `predicate` (a shell command).
- **`verify-goals.sh`**: Runs all predicates daily. If a "finished" task fails its predicate, its status is flipped to `VIOLATED`.
- **Key Idea:** A goal you only verify once is an assumption with a timestamp.

### BUILD 6: The Budget
- **`log-cost.sh`**: Logs the cost of each step to `memory/usage.log`.
- **`cost-check.sh`**: Checks daily spend against a `DAILY_BUDGET_USD`.
- **Cost Dynamics:** The quiet tick (triage) must cost cents, or the loop will cost a fortune.

### BUILD 7: The Optional Loops
- **Quorum:** Three cheap models vote before the expensive conductor is woken up.
- **Ratchet:** Monotonic improvement (e.g., reduce lint warnings to 0, never go up).
- **Sparring:** A "builder" writes code and a "breaker" writes tests to find weaknesses.
- **Compost:** A weekly review of failures to propose new laws or skills.

### BUILD 8: Ops
- **`Makefile`**: Provides simple commands like `make tick`, `make queue`, `make trust`, `make audit`.
- **Cron:** Schedules the `loop.sh` and `verify-goals.sh` to run automatically.

## The 30-Day Trust Schedule
A graduated plan to move from supervision to autonomy.

| Week | Level | You Do | Graduate When |
|---|---|---|---|
| 1 | L1 Report | Run by hand daily | 3 consecutive runs route exactly as you would |
| 2 | L2 Draft | Cron on; review queue | 2 skills cross 20 logged runs |
| 3 | L3 Ship | Best skill runs unattended | 1 week, zero interventions |
| 4 | L4 Grow | Compost; propose new skills | You remove something and nothing breaks |

## Key Takeaways
- **The model was never the hard part.** The hard part is building a system around it that stays honest when you stop watching.
- **Fable as conductor, not worker.** Using Fable for planning (10-20% of tokens) is orders of magnitude cheaper than using it for execution.
- **Deterministic gates.** A bash script (`verify.sh`) always holds the final vote, not the AI.
- **Autonomy is per-skill, not per-system.** A skill must earn the right to run unattended through a proven track record.

## Sources
- Original post on X (Twitter)
- Official Anthropic Fable 5 documentation (referenced inline)

## Related Concepts
- [[Claude Fable 5]]
- [[Agentic OS]]
- [[Autonomous Agents]]
- [[Cost Management]]
- [[Verification]]
- [[Trust Ledger]]
- [[Goal Stack]]

<!--
AI-FIRST VALIDATION:
- date: 2026-07-06
- type: literature
- tags: [article, ai, fable-5, agentic-os, productivity, builders-guide]
- source: Twitter/X Post
- ai-first: true
-->
