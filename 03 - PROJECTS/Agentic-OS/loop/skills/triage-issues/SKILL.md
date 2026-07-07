---
name: triage-issues
description: Triage new GitHub issues, label them, and close duplicates.
when: daily
never:
  - do not close issues without explanation
  - do not label incorrectly
done_when:
  - all new issues are labeled
  - duplicates are closed and linked
