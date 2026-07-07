---
name: fix-lint-debt
description: Fix lint warnings and errors in the codebase.
when: weekly or when lint count > 0
never:
  - do not ignore lint rules
  - do not skip tests
done_when:
  - npm run lint exits 0
