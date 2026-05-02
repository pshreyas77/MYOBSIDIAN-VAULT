---
source_file: "genericagent/llmcore.py"
type: "rationale"
community: "Community None"
location: "L60"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_None
---

# 把 user 消息里的 tool_result 块改写成纯文本，避免孤立引用。     history 统一使用 Claude content-block 格式

## Connections
- [[_sanitize_leading_user_msg()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_None