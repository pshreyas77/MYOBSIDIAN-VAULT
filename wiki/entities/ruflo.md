---
date: 2026-05-31
tags:
  - entity
  - project
  - mcp
  - ruflo
  - memory
  - task-execution
type: entity
status: referenced
---

# ruflo

MCP (Model Context Protocol) integration project with memory, task-execution, and shared components.

## Overview

ruflo is a project referenced in the vault that provides MCP integration with components for memory management and task execution.

## Structure

```
ruflo/v3/src/
├── memory/          # Memory management layer
├── shared/          # Shared utilities
└── task-execution/  # Task execution engine
```

## Integration

Connected to Claude Code via:
- `npx @claude-flow/cli@latest` commands
- MCP tools: memory_store, memory_search, swarm_init, agent_spawn
- Hooks: hooks_route, hooks_post-task, hooks_worker-dispatch

## Related

- [[wiki/entities/GitNexus]] — AI Git analysis tool
- [[wiki/entities/graphify-repo]] — Knowledge graph extraction
- [[wiki/concepts/AI-First-Workflow]] — AI-first vault methodology

## Source

`E:\_Knowledge\ObsidianVault\ruflo\`