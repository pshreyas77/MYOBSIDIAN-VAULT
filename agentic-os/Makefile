# Makefile (BUILD 8) — ops surface for the Agentic OS.
# Windows/git-bash: `make` may not exist; use `.` + the scripts directly,
# or run via WSL. Commands map 1:1 to the guide.

tick:            ; ./loop/loop.sh
queue:           ; @grep -E "review:|queued:|FAILED:|rerouted" loop/memory/STATE.md || echo empty
trust:           ; @./loop/scripts/trust-log.sh --render
audit:           ; @./loop/scripts/cost-check.sh --report
goals:           ; @./loop/verify-goals.sh
clean-worktrees: ; @git -C "$(TARGET_REPO)" worktree list 2>/dev/null | awk '/wt-/{print $$1}' | xargs -rn1 git worktree remove --force 2>/dev/null || true
