---
date: 2026-07-08
type: map
tags: [moc, digital-garden, pkm, knowledge-graph, progressive-summarization, publishing]
priority: practical
status: completed
ai-first: true
---

# Digital Garden & Knowledge Graph Methodology MOC

**For future Claude:** Your vault has 8+ atoms on digital gardens but no unifying map. This documents your actual practice and the graph construction methodology behind `graphify-repo` and `professional_vault_graph.py`.

---

## 1. Digital Garden MOC

### Core Concepts

| Concept | Definition | Your Practice |
|---------|------------|---------------|
| **Garden vs Stream** | Garden = evergreen, interlinked, non-chronological; Stream = chronological, ephemeral (blogs, social media) | Vault is a garden; daily notes are stream-like but integrated |
| **Progressive Summarization** | Layer 1 (raw notes) → Layer 2 (bold key points) → Layer 3 (highlights) → Layer 4 (mini-summary) → Layer 5 (remixed essay) | Applied in Research/ notes; MOCs are Layer 4-5 |
| **Link Density** | Healthy garden has >3 backlinks per note; orphan notes indicate gaps | Your analysis found 15+ orphans; target is 0 |
| **Publishing pipelines** | Obsidian → Quartz (static site), Digital Garden (Netlify), Obsidian Publish | Not yet implemented; `06 - OUTPUTS/` is manual |

### Your Vault's Garden Structure

| Layer | Folder | Purpose | Maturity |
|-------|--------|---------|----------|
| **Raw** | `00 - INBOX/`, `1-desk/`, `fleeting/` | Capture | Stream-like |
| **Literature** | `01 - LITERATURE/` | External source notes | Layer 2-3 |
| **Atomic** | `2-atoms/`, `02 - PERMANENT/` | Evergreen concepts | Layer 3-4 |
| **Project** | `03 - PROJECTS/` | Active work | Layer 3-4 |
| **Map** | `05 - MAPS/` | Synthesis/orientation | Layer 4-5 |
| **Output** | `06 - OUTPUTS/` | Finished essays | Layer 5 |

---

## 2. Knowledge Graph Construction Methodology

Your `graphify-repo` and `professional_vault_graph.py` need methodology documentation:

| Stage | Method | Tool Options | Your Choice |
|-------|--------|--------------|-------------|
| **Entity Extraction** | NER (spaCy) vs LLM (GPT-4/Qwen) | spaCy for speed; LLM for accuracy | Python scripts + LLM |
| **Relation Extraction** | Pattern matching vs LLM prompting | Regex for known relations; LLM for discovery | Hybrid |
| **Schema Design** | Ontology (rigid) vs Folksonomy (flexible) | Start folksonomy; migrate to ontology | Folksonomy (tags + wikilinks) |
| **Graph DB** | Neo4j (property graph) vs Kuzu (embedded) vs DuckDB (relational) | Kuzu for local; Neo4j for web | NetworkX → JSON → D3/Cytoscape |
| **Visualization** | Cytoscape (desktop), D3 (web), Graphistry (GPU) | D3 for custom; Cytoscape for analysis | `obsidian_graph.html` (D3) |
| **Evaluation** | Precision/recall on links; manual spot-checking | Essential; no automated metric is sufficient | Manual audit (149 notes scanned) |

---

## 3. Your Graph Pipeline (Documented)

```python
# professional_vault_graph.py - conceptual pipeline
1. Scan vault for *.md files
2. Extract frontmatter (tags, type, date, links)
3. Parse wikilinks [[...]] as edges
4. Extract entities from content (NER/LLM)
5. Build NetworkX graph
6. Compute centrality, communities, orphans
7. Export: Cytoscape.js JSON + obsidian_graph.html
8. Generate report: VAULT_REORGANIZATION_REPORT.md
```

---

## 4. Vault Updates Required

- [ ] Create `05 - MAPS/Digital Garden MOC.md` with this content
- [ ] Create `Research/PKM/Knowledge-Graph-Construction-Methodology.md` (detailed)
- [ ] Link from `InfiniteBrain.md` project hub
- [ ] Link from `graphify-repo` documentation
- [ ] Update `house-rules.md` with garden maintenance rules

---

## 5. Sources

| Source | Type |
|--------|------|
| Your vault atoms (2-atoms/Digital Garden*.md) | Internal |
| `graphify-repo/graphify/` | Code |
| `professional_vault_graph.py` | Code |
| `obsidian_graph.html` | Output |
| `VAULT_REORGANIZATION_REPORT.md` | Analysis |

---

*Report 17 of 20 | Generated: 2026-07-08 | Priority: 🟢 Practical | Domain: PKM*