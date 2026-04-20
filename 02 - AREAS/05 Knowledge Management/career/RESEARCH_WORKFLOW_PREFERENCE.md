# Research Workflow Preference

**Date:** 2026-04-14
**Status:** Active Workflow Rule

## User Instruction

> "What we research, always store it in my 'ClaudeVault' and link it with related information all over the vault"

## Workflow Protocol

### 1. Research Storage Location
- **Primary:** `ClaudeVault/` (vault root)
- **Naming:** Use `YYYY-MM-DD_descriptive-title.md` format
- **Tags:** Add relevant tags e.g., `#research`, `#claude-generated`, `#claudevault`

### 2. Cross-Linking Requirement
For every research file stored in ClaudeVault:
- Link to relevant topic files in `07 - Topics/`
- Link to related Area files in `02 - Areas/`
- Update `MASTER LINK INDEX.md` if significant finding
- Add backlinks from destination files to ClaudeVault

### 3. Link Format Examples
```markdown
## Connections
- See related: [[Buddhism vs Hinduism Analysis]] (ClaudeVault)
- Linked to: [[00_Buddhism_and_Hinduism_MOC]]
- Cross-ref: [[Temple Comparison Research]] (ClaudeVault)
- Source notes: [[2026-04-14_research-session]] (ClaudeVault)
```

### 4. Template for New Research
```markdown
---
created: {{date}}
source: ClaudeVault
aliases: []
tags: [research, claude-generated, topic-tag]
---

# {{title}}

{{research content}}

## Related Information
- Links to vault:
  - [[related-topic-MOC]]
  - [[related-area-file]]
- See also in ClaudeVault:
  - [[similar-research-file]]

## Graph Connections
```
Suggested graph connections based on content...
```

---
*Stored in ClaudeVault per user workflow preference*
```

## Example Active Links
| ClaudeVault Research | Linked Topics/Areas |
|---------------------|---------------------|
| Temple Comparison Research | Buddhism & Hinduism, Ancient Civilizations |
| IVC-Buddha Meditation Evidence | Buddhism & Hinduism, Religion & Cosmology |

---
*This document defines the standard workflow for all future research*
