---
name: triage-issues
description: Label, route, and summarize open issues.
when: open issue count grows or a triage finding is actionable.
never:
  - close an issue without a resolution
  - change issue severity labels without evidence
done_when:
  - "every open issue has a label and an owner or 'needs-triage' tag"
---
Steps:
1. List open issues (`gh issue list`).
2. Assign labels by component; flag contract-sensitive ones as queued.
3. Append a one-line summary per issue to STATE.md.
