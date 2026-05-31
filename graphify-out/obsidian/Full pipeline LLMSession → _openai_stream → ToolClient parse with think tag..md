---
source_file: "genericagent/tests/test_minimax_integration.py"
type: "rationale"
community: "Community None"
location: "L41"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/Community_None
---

# Full pipeline: LLMSession → _openai_stream → ToolClient parse with <think> tag.

## Connections
- [[.test_full_pipeline_with_think_tag()]] - `rationale_for` [EXTRACTED]
- [[LLMSession]] - `uses` [INFERRED]
- [[ToolClient]] - `uses` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/Community_None