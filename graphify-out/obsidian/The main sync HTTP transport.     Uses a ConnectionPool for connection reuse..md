---
source_file: "graphify-repo/worked/httpx/raw/transport.py"
type: "rationale"
community: "Community None"
location: "L60"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/Community_None
---

# The main sync HTTP transport.     Uses a ConnectionPool for connection reuse.

## Connections
- [[ConnectError]] - `uses` [INFERRED]
- [[HTTPTransport]] - `rationale_for` [EXTRACTED]
- [[Request_1]] - `uses` [INFERRED]
- [[Response_1]] - `uses` [INFERRED]
- [[TimeoutException]] - `uses` [INFERRED]
- [[TransportError]] - `uses` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/Community_None