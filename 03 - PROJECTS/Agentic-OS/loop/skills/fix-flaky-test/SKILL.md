---
name: fix-flaky-test
description: Identify and fix flaky tests that fail intermittently.
when: when a test fails non-deterministically
never:
  - do not simply retry the test
  - do not remove assertions
done_when:
  - test passes 10 times in a row
