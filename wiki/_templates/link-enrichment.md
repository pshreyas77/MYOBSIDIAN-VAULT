# Link Enrichment Template

## Purpose
Add valuable contextual links between related concepts without modifying existing content.

## Methods

### Method 1: Contextual "See Also" Sections
```markdown
## See Also
- [[Related Concept 1]] - Brief explanation of why these are connected
- [[Related Concept 2]] - Brief explanation of connection
```
*Added at end of note or in appropriate logical location*

### Method 2: Inline Contextual Enhancement
```markdown
As explored in greater detail in [[Related Topic]], this principle applies to [[Application Area]] by [explanation].
```
*Added where contextually appropriate, never replacing existing text*

### Method 3: Frontmatter Enhancement (for plugins that support it)
```markdown
---
# These additions don't alter core content, only metadata
related: [[Concept A]], [[Concept B]]
see_also: [[Concept C]], [[Concept D]]
graph_group: "Knowledge Domain"
---
```
*Only adds to existing frontmatter, never removes*

### Method 4: Structural Connection Blocks
```markdown
---
## Knowledge Connections
### Field Connections
- [[Field:Philosophy]] [[Buddhism]] [[Epistemology]]
- [[Field:Technology]] [[LLM]] [[Knowledge-Representation]]
### Topic Bridges
- [[Ancient Wisdom]] [[Modern AI]] [[Ethical Frameworks]]
---
```
*Added as footer or sidebar content*