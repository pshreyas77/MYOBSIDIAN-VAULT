# How to Run 1,000 AI Agents Overnight From Your Phone - Complete Course

> **Author**: Boris Cherny (Claude Code builder)  
> **Source**: Course/article on scalable agent architecture  
> **Stored**: 2026-08-14  
> **Tags**: #ai-agents #orchestration #scaling #vernal-architecture #mobile-triggering

---

## The Honest Framing

Nobody needs literally 1,000 agents for most real work. The number isn't the point. What matters is the **architecture** that makes running any large number of agents unattended, overnight, triggered from a phone, actually **safe rather than reckless**. Once you have that architecture, scaling from 10 → 100 → 1,000 is mostly a matter of how much genuinely parallelizable work you have.

---

## The Four Pieces That Make This Possible

### 1. Mobile Triggering
Real interface for **starting, checking, redirecting** work from phone — not just notifications.
- **Claude Dispatch** = continuous conversation with Cowork from phone
- **Test**: "Check status of my current sessions. For each, tell me what it's working on, progress, and whether it needs anything from me."
- Must support: start new task, check detailed status, send redirect/correction

### 2. Isolated Parallel Execution
Two layers:
- **Sub-agent isolation**: Main agent spawns sub-agents in own contexts (hundreds per session)
- **Git worktrees**: Independent sessions on separate branches/directories
- **Decision rule**: Real-time dependency → sub-agents; genuinely independent → separate sessions/worktrees

**Decomposition prompt**:
> "Break this task into independent pieces that can be worked on in parallel. For each piece, define scope clearly enough that a sub-agent doesn't need to know what other pieces are doing. Flag any piece that depends on another's output."

### 3. Verification You Can Trust While Asleep
**Core principle**: Never let an agent grade its own work.
- **Builder** does the task
- **Judge** (separate, with independent evidence: test results, requirements doc, execution output) verifies against real evidence

**Verification template**:
> "Before reporting complete, verify against [test suite / requirements / success criteria]. Do not report success based on own assessment. Cite specific evidence confirming each requirement. If cannot verify, say so explicitly."

**High-stakes**: Add second independent verification pass (fresh session, no memory of production).

### 4. Hard Stop Conditions & Cost Ceilings
Every unattended task needs three hard limits:
1. **Max time/iterations** → stop and report state
2. **Max cost ceiling** → calculated worst-case tokens × agents
3. **Explicit scope boundaries** → never deploy, delete, spend, communicate without approval

**Stop condition template**:
> "Maximum runtime: [X hours]. Maximum cost: [$Y]. If limit reached, stop immediately, do not attempt 'just one more step.' Prepare summary of completed/remaining for morning review.
> Never take these actions without explicit approval: [list boundaries]."

**Calculate worst-case cost BEFORE first overnight run**.

---

## Putting It Together: First Real Overnight Run

1. Define 5–20 genuinely independent tasks (small enough to review all results in morning)
2. Apply verification template + stop condition template to each
3. Launch as sub-agents or separate sessions/worktrees
4. Sleep
5. **Morning review from phone** — check verification evidence, not just "success" reports
6. Repeat until verification layer is trusted

---

## Scaling: 20 → 200 → 1,000

- Scale only when you have **genuinely independent work** justifying it
- Track **escalation-rate** and **cost-ceiling-trigger rate**
- If growing share of agents hit limits without completing → fix task scoping/limits first
- Cherny's thousands happen on **deep research/exploration** with many independent paths

---

## Worked Example: 100-Agent Overnight Research

**Task**: Evaluate 100 potential business partners against criteria
- Each evaluation fully independent
- Define criteria, verification standard, per-agent cost ceiling **once as template**
- Launch 100 sessions (one per partner), isolated contexts, identical instructions
- Each agent: researches → evaluates → verifies against cited sources → reports completed eval OR "insufficient information" flag
- Morning: review 100 structured evaluations from phone; uncertain ones get attention first

---

## Common Mistakes That Undermine Scale

| Mistake | Consequence |
|---------|-------------|
| Scaling agents before verification tested | Scaling on hope, not evidence |
| Stop conditions as formality | System doesn't halt when it should |
| Dependent tasks forced parallel | Inconsistent, hard-to-debug results |
| Skipping morning review | Drift in verification standards, cost creep |
| Vague task setup → vague mobile status | Mobile check-ins useless |

---

## Troubleshooting Real Problems

| Problem | Root Cause | Fix |
|---------|------------|-----|
| Agents report success, output wrong | Verification gap (Judge lacks independent evidence) | Give Judge actual test results/source docs |
| Mobile shows vague status | No structured progress reporting requested | Add explicit progress format instruction |
| Cost exceeds ceiling despite stops | Soft prompt instruction, not hard code-level check | Enforce limits mechanically |
| Inconsistent results for identical criteria | Template instructions vary subtly between agents | Copy template identically across batch |
| Works at 10, breaks at 100 | Hidden dependency between tasks | Check for missed sequencing needs |

---

## Real Cost Economics

- **Cost per agent** scales with model choice — route routine tasks to cheaper models
- **Calculate from real test batch** (5–10 agents), not documentation estimates
- **Buffer for limit-hit tasks** — incomplete tasks still cost money
- High incomplete rate → loosen limit or tighten scope, don't accept inefficiency

---

## What This Actually Buys You

Not the impressive number. **Specific hours returned**:
- Days of manual research → overnight run reviewed in 20 minutes over coffee
- Backlog of independent tasks handled while asleep, verified, waiting for quick review

> **Cherny's framing**: "We're only 1% done." This architecture evolves with tools. Build the four pieces properly at honest scale for your work today.

---

## Implementation Notes for Free/Cheap Start

| Approach | Scale | Cost |
|----------|-------|------|
| Local models (Ollama, llama.cpp) | 1–5 parallel on consumer GPU | Free after hardware |
| Free API tiers (OpenRouter, Groq, Cerebras) | 10–50 agents/day | Free (rate-limited) |
| GitHub Actions / GitLab CI | 20–50 concurrent | Free minutes/month |
| Self-hosted orchestration + local LLMs | Dozens overnight | Electricity only |

**The architecture is free. The inference at 1,000-agent scale is not.** Start with 5–10 agents on local models or free tiers, verify verification works, then decide if ROI justifies API spend.

---

*Stored for reference in second brain. Original article by Boris Cherny (Claude Code builder).*