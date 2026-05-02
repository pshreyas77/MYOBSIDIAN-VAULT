---
source_file: "genericagent/tests/test_minimax.py"
type: "rationale"
community: "Community None"
location: "L13"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/Community_None
---

# Test MiniMax temperature clamping in _openai_stream.

## Connections
- [[LLMSession]] - `uses` [INFERRED]
- [[MockResponse]] - `uses` [INFERRED]
- [[NativeOAISession]] - `uses` [INFERRED]
- [[NativeToolClient]] - `uses` [INFERRED]
- [[TestMiniMaxTemperatureClamping]] - `rationale_for` [EXTRACTED]
- [[ToolClient]] - `uses` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/Community_None