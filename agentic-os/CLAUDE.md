# CLAUDE.md — Agentic OS (Fable 5 pattern, adapted for tencent/hy3:free)

> Project constitution. Every line is a law, a number, a "never", or a command
> that checks itself. The model optimizes around tips; there are no tips here.

## NEVER (laws; exceptions require asking first)
- Never exceed 200 changed lines in one commit without asking.
- Never touch `src/auth/`, `src/billing/`, `migrations/`, or prod config unattended.
- Never report work as done from your own assessment. Done = the check passed.
- Never invent a secret, an endpoint, or a convention. Stop and ask.
- Never add a dependency. Propose it in memory/STATE.md and stop.
- Never exceed `max_tokens` 64k for the conductor; workers verify at <=32k.
- Never edit or delete a test to make it pass. That is a fail, always.
- Never echo, transcribe, or explain your internal reasoning in response text.
  (On reasoning models this triggers refusal; on hy3 it wastes tokens.)
- When a `/goal` condition passes, write `goals/<name>.md` with the condition
  as its predicate before reporting success.

## DISPATCH (route every task; first match wins; log to memory/dispatch.tsv)
| seat          | model                | role                                  | appetite |
|---------------|----------------------|---------------------------------------|----------|
| triage        | $CHEAP (cheap seat)  | read repos/CI, emit findings only     | ~0 cost  |
| conductor     | tencent/hy3:free     | decide ONE item, emit work order JSON | 1 call   |
| worker        | $WORKER (cheap seat) | execute the work order                | per step |
| verifier      | tencent/hy3:free     | judge spec+diff, fresh context        | 1 call   |
1. Decision / plan / review / route / standoff -> conductor (hy3), read-only.
2. Reads >50k tokens (logs/PDFs/screenshots) -> cheap seat; never conductor.
3. Spec complete -> worker (cheap seat).
4. Verify -> verifier (hy3), no tools, sees only spec + diff.
5. Escalate one rung on a miss without asking; only two rungs exist here.

## WORDS
- "intelligence" = hardest problem handled unsupervised
- "taste" = UI/UX, code quality, API design, copy
- "done" = the predicate passes; nothing else
- "small" = under 50 changed lines; "quick" = under 10 minutes of your time
- "cleanup" = behavior identical, verify.sh green before and after

## DONE
- Every task has a machine-checkable `done_when` before work starts.
- A fresh-context agent that saw neither plan nor draft verifies against it.
- `guardrails/verify.sh` has the final vote.
- Deviations: conservative option, log to IMPLEMENTATION.md, continue.
- Maker and checker disagree twice -> stop, queue for a human.
