---
source_file: "genericagent/tests/test_minimax.py"
type: "rationale"
community: "Community None"
location: "L63"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/Community_None
---

# Temperature > 1.0 should be clamped to 1.0.

## Connections
- [[.test_minimax_temp_above_one_clamped()]] - `rationale_for` [EXTRACTED]
- [[LLMSession]] - `uses` [INFERRED]
- [[MockResponse]] - `uses` [INFERRED]
- [[NativeOAISession]] - `uses` [INFERRED]
- [[NativeToolClient]] - `uses` [INFERRED]
- [[ToolClient]] - `uses` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/Community_None