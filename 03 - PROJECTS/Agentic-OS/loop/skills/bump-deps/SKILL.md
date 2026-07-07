---
name: bump-deps
description: Update project dependencies to their latest compatible versions.
when: monthly or when security advisory is published
never:
  - do not update major versions without testing
  - do not ignore lockfile changes
done_when:
  - npm audit exits 0
  - npm test exits 0
