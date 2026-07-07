---
name: fix-lint-debt
description: Resolve outstanding lint warnings in the codebase.
when: lint warnings accumulate; triage flags "lint" actionable.
never:
  - edit lint config to lower the bar
  - rewrite code for style beyond the warning
done_when:
  - "npm run lint --if-present exits 0"
---
Steps:
1. Run `npm run lint --if-present`, capture warnings.
2. Fix one warning class at a time with small diffs.
3. Re-run lint; confirm 0 warnings for fixed class.
Verify against done_when; do not exceed 200 changed lines per commit.
