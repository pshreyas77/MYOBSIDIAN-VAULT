---
date: 2026-05-31
tags:
  - entity
  - project
  - git
  - ai
type: entity
status: active
---

# GitNexus

AI-powered Git repository analysis tool for code indexing, PR review, and architecture understanding.

## Overview

GitNexus is a TypeScript monorepo providing CLI and server tools for analyzing Git repositories using AI. It supports COBOL code indexing, PR review, architecture documentation, and more.

## Structure

```
GitNexus/
├── gitnexus/           # Core TypeScript package
│   ├── src/cli/        # CLI commands (analyze, index-repo, wiki, etc.)
│   ├── src/core/       # Core engine (augmentation, embeddings, graph, group, ingestion)
│   ├── src/server/     # MCP server
│   ├── src/mcp/        # MCP protocol
│   └── src/storage/    # Storage layer
├── gitnexus-web/       # Web interface
├── eval/               # Evaluation framework
├── docs/               # Documentation
│   ├── code-indexing/cobol/  # COBOL language support
│   ├── guides/         # User guides
│   └── superpowers/    # Feature specs
└── deploy/kubernetes/  # K8s deployment
```

## Key Features

- **Code Indexing**: Tree-sitter based parsing for multiple languages
- **COBOL Support**: Full COBOL language coverage (copy-expansion, regex-extraction, deep-indexing)
- **PR Review**: AI-powered pull request review
- **Graph Mode**: Knowledge graph building from code
- **Embeddings**: Vector-based code search and similarity
- **MCP Server**: Model Context Protocol server implementation

## Technologies

- TypeScript/Node.js
- Tree-sitter (code parsing)
- Docker
- Kubernetes
- MCP (Model Context Protocol)
- Vitest (testing)

## Related

- [[wiki/entities/tolaria]] — Tauri + React Obsidian-like app
- [[wiki/entities/genericagent]] — Python autonomous agent
- [[wiki/entities/graphify-repo]] — Knowledge graph extraction
- [[wiki/entities/temp_autoresearch]] — Karpathy's autonomous LLM training

## Source

`E:\_Knowledge\ObsidianVault\GitNexus\`