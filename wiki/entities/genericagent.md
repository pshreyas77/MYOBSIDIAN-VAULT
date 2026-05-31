---
date: 2026-05-31
tags:
  - entity
  - project
  - python
  - autonomous-agent
type: entity
status: active
---

# genericagent

Python autonomous agent loop with multiple frontend integrations (desktop pet, Qt, Streamlit, DingTalk, QQ, filesystem).

## Overview

genericagent is a Python autonomous agent framework featuring a `BaseHandler` class with `dispatch()`, `tool_before_callback()`, `tool_after_callback()`, and a generator-based turn loop. Exports `agent_runner_loop()`.

## Structure

```
genericagent/
├── agent_loop.py          # Core agent loop (BaseHandler, agent_runner_loop)
├── agentmain.py           # Main entry point
├── desktop_pet.pyw        # Desktop pet frontend
├── qtapp.py               # Qt application frontend
├── stapp.py               # Streamlit frontend
├── dingtalkapp.py         # DingTalk integration
├── qqapp.py               # QQ integration
├── fsapp.py               # Filesystem frontend
├── assets/                # Demo images, sys prompts, tools_schema.json
└── SETUP_FEISHU.md        # Feishu/Lark integration guide
```

## BaseHandler Class

```python
class BaseHandler:
    dispatch()               # Handle agent commands
    tool_before_callback()    # Pre-tool hook
    tool_after_callback()     # Post-tool hook
    # Generator-based turn loop
```

## Related

- [[wiki/entities/GitNexus]] — TypeScript AI Git analysis
- [[wiki/entities/graphify-repo]] — Knowledge graph extraction
- [[wiki/entities/tolaria]] — Tauri + React app

## Source

`E:\_Knowledge\ObsidianVault\genericagent\`