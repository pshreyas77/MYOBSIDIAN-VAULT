---
source_file: "GitNexus/gitnexus/test/fixtures/lang-resolution/python-class-attr-export-leak/mod.py"
type: "rationale"
community: "Community None"
location: "L1"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_None
---

# Class-body attribute (`User.MAX_USERS`) that MUST NOT leak into the module's exp

## Connections
- [[mod.rs]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_None