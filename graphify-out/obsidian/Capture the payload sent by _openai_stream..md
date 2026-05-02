---
source_file: "genericagent/tests/test_minimax.py"
type: "rationale"
community: "Community None"
location: "L16"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/Community_None
---

# Capture the payload sent by _openai_stream.

## Connections
- [[._make_stream_call()]] - `rationale_for` [EXTRACTED]
- [[LLMSession]] - `uses` [INFERRED]
- [[MockResponse]] - `uses` [INFERRED]
- [[NativeOAISession]] - `uses` [INFERRED]
- [[NativeToolClient]] - `uses` [INFERRED]
- [[ToolClient]] - `uses` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/Community_None