---
date: 2026-05-31
tags:
  - entity
  - project
  - tauri
  - react
  - obsidian
type: entity
status: active
---

# tolaria

Tauri + React Obsidian-like note-taking application with example vault, design files, and full workflow configurations.

## Overview

tolaria is an in-development Obsidian-like note-taking app built with Tauri (Rust backend) and React (TypeScript frontend). It includes a demo vault, design mockups, and full GitHub workflow configurations.

## Structure

```
tolaria/
├── demo-vault-v2/       # Example Obsidian vault
│   └── .trash/         # Demo trash folder
├── design/             # Design files (.pen format)
├── .github/workflows/  # CI/CD configurations
├── .husky/             # Git hooks
├── AGENTS.md           # Shared agent instructions
├── CONTRIBUTING.md     # Contribution guidelines
├── CLAUDE.md           # Claude Code compatibility shim
└── src-tauri/          # Rust backend
```

## Related

- [[wiki/entities/GitNexus]] — AI Git analysis tool
- [[wiki/entities/genericagent]] — Python autonomous agent
- [[wiki/entities/graphify-repo]] — Knowledge graph extraction

## Source

`E:\_Knowledge\ObsidianVault\tolaria\`