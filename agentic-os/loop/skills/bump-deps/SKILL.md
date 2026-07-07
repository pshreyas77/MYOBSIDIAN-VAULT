---
name: bump-deps
description: Update a dependency to a safe minor/patch within range.
when: a dependency has a security advisory or a safe update available.
never:
  - bump across a major version unattended
  - skip the test run after bumping
done_when:
  - "npm install succeeds and npm test --if-present exits 0"
---
Steps:
1. Read package.json; pick the target dependency.
2. `npm install <dep>@<range>` (patch/minor only).
3. Run verify.sh; commit only if green.
