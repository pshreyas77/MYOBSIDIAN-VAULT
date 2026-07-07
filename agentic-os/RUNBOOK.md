# Agentic OS — Runbook (BUILD 8)

Adapted from the Fable 5 Builder's Guide for **tencent/hy3:free** and a
Windows/git-bash environment. All 8 builds are present under `loop/`.

## Setup (one time)
1. `export OPENROUTER_API_KEY=sk-or-...` (your OpenRouter key, hy3:free).
2. `export TARGET_REPO=/path/to/your-repo` (the repo the loop will work on).
3. `chmod +x loop/*.sh loop/scripts/*.sh`
4. Edit `loop/guardrails/verify.sh` to match your test stack.

## The model reality
- The guide assumes `claude-fable-5` (a future/credits model). We use
  **tencent/hy3:free** everywhere via `loop/call.sh` (OpenRouter + curl + python3).
- `claude` subagent CLI and `llm` CLI are NOT required. `jq` is NOT required
  (python3 parses JSON). `gh` is optional (PR creation skips gracefully).

## Daily ops
- `make tick`        (or `bash loop/loop.sh`)  — run the heartbeat once by hand
- `make queue`       — review items queued/failed
- `make trust`       — render the trust ledger
- `make audit`       — usage report (ticks)
- `make goals`       — verify all standing goals
- `make clean-worktrees` — remove stale worktrees

## Scheduling (no cron on git-bash)
- Windows Task Scheduler: trigger `bash loop/loop.sh >> loop/memory/cron.log 2>&1`
  Mon–Fri 07:00; `bash loop/verify-goals.sh >> loop/memory/cron.log 2>&1` daily 07:30.
- Or WSL cron if available:
    `0 7 * * 1-5  cd /e/_Knowledge/ObsidianVault/agentic-os/loop && ./loop.sh >> memory/cron.log 2>&1`
    `30 7 * * *   cd /e/_Knowledge/ObsidianVault/agentic-os/loop && ./verify-goals.sh >> memory/cron.log 2>&1`

## 30-day trust schedule (graduate one level at a time)
| Week | Level       | You do                              | Graduate when                          |
|------|-------------|-------------------------------------|----------------------------------------|
| 1    | L1 report   | builds 1-6; tick by hand daily      | 3 runs route as you would              |
| 2    | L2 draft    | cron on; reviews feed the ledger    | 2 skills cross 20 logged runs          |
| 3    | L3 ship     | audit vs budget; best skill unattended | 1 week, zero interventions          |
| 4    | L4 grow     | compost sign-offs; approve 1 skill  | you removed something, nothing broke   |

## Alarm map
| Signal                | Meaning                              | Action                                  |
|-----------------------|--------------------------------------|-----------------------------------------|
| exit 2 (reroute)      | safeguard swapped models / empty out | re-run item; never iterate on bad output |
| REFUSAL (exit 6)      | safety classifier declined           | simplify the skill prompt; re-route      |
| exit 3 (budget/tick)  | daily tick cap or USD budget hit     | `make audit`; check what grew            |
| ALERT demoted         | skill dropped below 90%              | read its last 3 fails                    |
| goal VIOLATED         | finished thing stopped being true    | sentinel gives suspects; fix via pipeline |
| maker/checker x2      | neither presumed right               | you decide, or third fresh reviewer      |
| verify-goals timeout  | predicate too expensive              | that is a violation; cheapen the predicate |

## The rules (print this)
- Laws, not tips: a number, a never, or a command that checks it.
- Conductor plans, workers execute, neither verifies. --allowedTools enforces it.
- Agents talk in work orders. done_when = spec + stop + future invariant.
- Spend effort where the loop branches. Cheap seats do the quiet ticks.
- Goals graduate; they do not close. verify-goals.sh runs daily, forever.
- Autonomy per skill: 20 runs, 95%, auto. Demotion automatic and loud.
- Two ledgers: trust (workers) and goals (work). Read both.
- Sentinel detects; pipeline fixes.
- One graduation criterion at a time. Every month, delete something.
