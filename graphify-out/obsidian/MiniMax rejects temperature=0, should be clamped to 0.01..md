---
source_file: "genericagent/tests/test_minimax.py"
type: "rationale"
community: "Community None"
location: "L43"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/Community_None
---

# MiniMax rejects temperature=0, should be clamped to 0.01.

## Connections
- [[.test_minimax_temp_zero_clamped()]] - `rationale_for` [EXTRACTED]
- [[LLMSession]] - `uses` [INFERRED]
- [[MockResponse]] - `uses` [INFERRED]
- [[NativeOAISession]] - `uses` [INFERRED]
- [[NativeToolClient]] - `uses` [INFERRED]
- [[ToolClient]] - `uses` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/Community_None