---
source_file: "genericagent/tests/test_minimax_integration.py"
type: "rationale"
community: "Community None"
location: "L124"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/Community_None
---

# Verify the actual HTTP request has clamped temperature for MiniMax.

## Connections
- [[.test_temperature_enforced_in_request()]] - `rationale_for` [EXTRACTED]
- [[LLMSession]] - `uses` [INFERRED]
- [[ToolClient]] - `uses` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/Community_None