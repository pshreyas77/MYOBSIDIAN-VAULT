---
source_file: "genericagent/tests/test_minimax.py"
type: "rationale"
community: "Community None"
location: "L48"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/Community_None
---

# Negative temperature should be clamped to 0.01.

## Connections
- [[.test_minimax_temp_negative_clamped()]] - `rationale_for` [EXTRACTED]
- [[LLMSession]] - `uses` [INFERRED]
- [[MockResponse]] - `uses` [INFERRED]
- [[NativeOAISession]] - `uses` [INFERRED]
- [[NativeToolClient]] - `uses` [INFERRED]
- [[ToolClient]] - `uses` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/Community_None