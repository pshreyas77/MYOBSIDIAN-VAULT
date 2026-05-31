---
source_file: "genericagent/tests/test_minimax_integration.py"
type: "rationale"
community: "Community None"
location: "L87"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/Community_None
---

# Full pipeline: MiniMax response with tool_use block.

## Connections
- [[.test_full_pipeline_with_tool_call()]] - `rationale_for` [EXTRACTED]
- [[LLMSession]] - `uses` [INFERRED]
- [[ToolClient]] - `uses` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/Community_None