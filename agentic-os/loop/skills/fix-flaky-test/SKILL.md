---
name: fix-flaky-test
description: Stabilize a test that intermittently fails.
when: a test fails nondeterministically in CI; triage flags "flaky".
never:
  - delete or skip the test to make it pass
  - add sleeps longer than 50ms without justification
done_when:
  - "the test passes 10 consecutive runs in isolation"
---
Steps:
1. Identify the flake source (timing, order, shared state).
2. Fix at the root; prefer deterministic setup/teardown.
3. Run the test 10x; confirm all green.
