---
source_file: "genericagent/tests/test_minimax.py"
type: "rationale"
community: "Community None"
location: "L256"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/Community_None
---

# NativeToolClient should extract <think> tags from MiniMax responses.

## Connections
- [[.test_native_tool_client_think_tag()]] - `rationale_for` [EXTRACTED]
- [[LLMSession]] - `uses` [INFERRED]
- [[MockResponse]] - `uses` [INFERRED]
- [[NativeOAISession]] - `uses` [INFERRED]
- [[NativeToolClient]] - `uses` [INFERRED]
- [[ToolClient]] - `uses` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/Community_None