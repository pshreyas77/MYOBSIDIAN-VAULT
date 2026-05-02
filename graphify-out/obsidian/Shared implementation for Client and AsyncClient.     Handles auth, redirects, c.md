---
source_file: "graphify-repo/worked/httpx/raw/client.py"
type: "rationale"
community: "Community None"
location: "L32"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/Community_None
---

# Shared implementation for Client and AsyncClient.     Handles auth, redirects, c

## Connections
- [[AsyncHTTPTransport]] - `uses` [INFERRED]
- [[Auth]] - `uses` [INFERRED]
- [[BaseClient]] - `rationale_for` [EXTRACTED]
- [[BaseTransport]] - `uses` [INFERRED]
- [[BasicAuth]] - `uses` [INFERRED]
- [[Cookies]] - `uses` [INFERRED]
- [[HTTPTransport]] - `uses` [INFERRED]
- [[Headers]] - `uses` [INFERRED]
- [[InvalidURL]] - `uses` [INFERRED]
- [[Request_1]] - `uses` [INFERRED]
- [[Response_1]] - `uses` [INFERRED]
- [[TooManyRedirects]] - `uses` [INFERRED]
- [[URL]] - `uses` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/Community_None