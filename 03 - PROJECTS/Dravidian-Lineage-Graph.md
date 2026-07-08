---
date: 2026-07-08
type: project
tags: [project, dravidian-lineage, knowledge-graph, visualization, indian-politics, digital-garden]
status: active
ai-first: true
---

# Dravidian Lineage Knowledge Graph — Political Garden

**For future Claude:** Interactive knowledge graph of Dravidian political lineage (Justice Party → DK → DMK → AIADMK → splits) with caste coalitions, policy diffusion, election data. Explorable digital garden. Part of Cross-Domain Idea Synthesis Top 3 priority.

---

## Overview

**Problem**: `Indian Political History MOC` has the lineage as linear text. Digital gardens thrive on non-linear exploration. Your `graphify-repo` + `obsidian_graph.html` infrastructure exists but isn't applied to this domain.

**Solution**: Interactive knowledge graph (D3.js/Cytoscape.js) with:
- **Nodes**: Parties, leaders, policies, elections, caste coalitions, legislation
- **Edges**: "split from", "merged into", "allied with", "opposed", "policy continuity", "caste base overlap"
- **Exploration Modes**: Timeline slider, caste coalition heatmap, policy diffusion tracing, counterfactual "what-if"

---

## Data Model

### Node Types

| Type | Examples | Attributes |
|------|----------|------------|
| **Party** | Justice Party, DK, DMK, AIADMK, MDMK, PMK, TVK, DMDK | name, founded, dissolved, ideology, current_status |
| **Leader** | Periyar, Annadurai, Karunanidhi, MGR, Jayalalithaa, Stalin, EPS, OPS, Vijay | name, birth/death, role, tenure, faction |
| **Policy** | Communal G.O. 3136, 69% Reservation, Anti-Hindi, Land Reform, Midday Meal | name, year, party, impact, status |
| **Election** | 1967 TN Assembly, 2021 TN Assembly, 2024 LS | year, type, results, turnout, key issues |
| **Caste Coalition** | Non-Brahmin, MBC, SC/ST, Thevar, Gounder, Vanniyar | name, region, parties, loyalty_shift |
| **Event** | Vaikom Satyagraha, Anti-Hindi Agitation, MGR Death, Jayalalithaa Death | date, description, impact |

### Edge Types

| Type | Source → Target | Weight | Meaning |
|------|-----------------|--------|---------|
| `split_from` | DMK → DK | 1.0 | Organizational split |
| `merged_into` | MGR faction → AIADMK | 1.0 | Merger |
| `allied_with` | DMK ↔ Congress (2004) | 0.7 | Electoral alliance |
| `opposed` | DMK ↔ AIADMK | 1.0 | Primary rivalry |
| `policy_continuity` | Justice Party G.O. 3136 → DMK 69% | 0.8 | Policy lineage |
| `caste_base_overlap` | PMK ↔ AIADMK (Vanniyar) | 0.6 | Shared caste support |
| `mentored_by` | Stalin → Karunanidhi | 0.9 | Leadership succession |
| `founded_by` | Karunanidhi → DMK | 1.0 | Founder relationship |

---

## Exploration Modes

### 1. Timeline Slider (1916 → Present)
- Horizontal slider filters nodes/edges by year
- Parties appear/disappear at founding/dissolution
- Leaders appear at political entry, fade at death/retirement
- Policies appear at enactment
- **Play button**: Auto-animate through decades

### 2. Caste Coalition Heatmap
- Matrix: Parties (rows) × Caste Groups (columns)
- Cell color = support strength (0-1)
- Animate over time: watch Vanniyar shift PMK→AIADMK→DMK
- Click cell → highlight relevant party/caste nodes in graph

### 3. Policy Diffusion Tracer
- Select a policy (e.g., "69% Reservation")
- Trace backward: Justice Party G.O. 3136 (1921) → DMK 1971 → 69% Act 1994
- Trace forward: Which parties adopted/opposed/amended
- Show "policy ancestors" and "policy descendants"

### 4. Counterfactual "What-If" Mode
- Click a node → "Remove this node" (e.g., "What if MGR never entered politics?")
- Simulate: AIADMK doesn't form, DMK dominates longer, different caste alignments
- Show divergent paths with confidence scores (based on historical analogies)
- **Note**: Speculative — clearly labeled

---

## Tech Stack

| Component | Technology | Your Existing Assets |
|-----------|------------|---------------------|
| **Graph Engine** | Cytoscape.js (JS) or NetworkX → JSON | `graphify-repo/graphify/`, `professional_vault_graph.py` |
| **Visualization** | D3.js force-directed + Cytoscape.js | `obsidian_graph.html` (static) |
| **Interactivity** | Vanilla JS / Alpine.js | New |
| **Data Source** | YAML/JSON in vault | `wiki/entities/`, research notes |
| **Export** | Standalone HTML for `06-OUTPUTS/` | Your existing HTML export pattern |
| **Embedding** | Obsidian iframe or standalone | `05 - MAPS/Indian Political History MOC.md` link |

---

## Data Sources (Vault)

### Entities (wiki/entities/)
- `Periyar E. V. Ramasamy`
- `Annadurai` (need to create)
- `Karunanidhi` (need to create)
- `MGR` (need to create)
- `Jayalalithaa` (need to create)
- `Stalin` (need to create)
- `EPS` / `OPS` (need to create)
- `Vijay` / `TVK` (need to create)

### Research Notes
- `05 - MAPS/Indian Political History MOC.md` — Lineage, regional legacies, electoral evolution
- `02 - PERMANENT/concepts/Justice Party.md` — Communal G.O. 3136
- `Research/2026-06-02 — BJP Political Geography & South India Analysis.md` — BJP challenge context
- `Research/Articles/2026-06-09 — RSS Funding Mechanisms Analysis.md` — Opposition context

### Election Data (to compile)
- Tamil Nadu Assembly: 1952, 1957, 1962, 1967, 1971, 1977, 1980, 1984, 1989, 1991, 1996, 2001, 2006, 2011, 2016, 2021
- Lok Sabha TN seats: 1984 onward
- Vote shares, seat counts, alliances

---

## Agent Configuration (genericagent SOP)

```yaml
agent:
  name: dravidian-graph-builder
  schedule: "monthly 1st saturday 10:00"  # Rebuild with new data
  max_runtime_minutes: 60
  
stages:
  collect:
    - parse: wiki/entities/*.md → nodes (party, leader)
    - parse: 05-MAPS/Indian Political History MOC.md → edges (lineage, alliances)
    - parse: Research/2026-06-02 — BJP Political Geography... → BJP context nodes
    - load: election_data.yaml (manual curation)
    - load: caste_coalitions.yaml (manual curation)
    
  build:
    - tool: python (graphify-repo)
      script: build_dravidian_graph.py
      output: "E:/_Knowledge/ObsidianVault/03 - PROJECTS/Dravidian-Graph/data/graph.json"
      
  visualize:
    - tool: python
      script: render_interactive_html.py
      template: dravidian_template.html (D3+Cytoscape)
      output: "E:/_Knowledge/ObsidianVault/06 - OUTPUTS/Dravidian-Lineage-Graph.html"
      
  validate:
    - check: all MOC entities have nodes
    - check: no orphan nodes (except intentional)
    - check: timeline continuity (no gaps >5 years without party)
    
  deploy:
    - copy: 06-OUTPUTS/Dravidian-Lineage-Graph.html → vault
    - update: 05-MAPS/Indian Political History MOC.md with new link
    - log: build log with node/edge counts, new additions
```

---

## First Sprint Deliverable (2026-07-28)

- [ ] `data/nodes.yaml` — All parties, leaders, policies, caste groups (~40 nodes)
- [ ] `data/edges.yaml` — All relationships (~60 edges)
- [ ] `data/elections.yaml` — TN Assembly 1967-2021, LS 1984-2024
- [ ] `build_dravidian_graph.py` — NetworkX → Cytoscape.js JSON
- [ ] `render_interactive_html.py` — D3 force-directed + timeline slider
- [ ] `06 - OUTPUTS/Dravidian-Lineage-Graph.html` — Working interactive graph
- [ ] Project hub: `03 - PROJECTS/Dravidian-Lineage-Graph.md`
- [ ] Linked from `05 - MAPS/Indian Political History MOC.md`
- [ ] Added to `05 - MAPS/AI & Technology MOC.md` (graph viz project)

---

## Vault Integration

```
03 - PROJECTS/
├── Cross-Domain Idea Synthesis.md
├── History-Watchdog.md
├── Health-Autopilot.md
├── Dravidian-Lineage-Graph.md              ← This project hub
└── Dravidian-Lineage-Graph/
    ├── data/
    │   ├── nodes.yaml                      ← Parties, leaders, policies, castes
    │   ├── edges.yaml                      ← Relationships
    │   ├── elections.yaml                  ← Election results
    │   └── caste_coalitions.yaml           ← Caste-party support matrix
    ├── scripts/
    │   ├── build_dravidian_graph.py        ← NetworkX → JSON
    │   └── render_interactive_html.py      ← JSON → HTML (D3+Cytoscape)
    ├── templates/
    │   └── dravidian_template.html         ← Base HTML with JS libs
    ├── output/
    │   └── graph.json                      ← Cytoscape.js format
    └── logs/
        
06 - OUTPUTS/
├── Dravidian-Lineage-Graph.html            ← Deployed interactive graph
└── Dravidian-Lineage-Graph-YYYY-MM-DD.html ← Versioned snapshots

05 - MAPS/
├── Indian Political History MOC.md         ← Links to graph
└── AI & Technology MOC.md                  ← Links as graph viz project
```

---

## Interactive Features Spec

### Timeline Slider
```javascript
// Cytoscape.js + noUiSlider
// Filter: cy.elements().filter(ele => ele.data('start_year') <= currentYear && (!ele.data('end_year') || ele.data('end_year') >= currentYear))
// Animate: requestAnimationFrame loop, 1 year/500ms
```

### Caste Heatmap
```javascript
// D3.js matrix
// Rows: parties (sorted by founding)
// Columns: caste groups (sorted by population)
// Cells: support 0-1, color scale Viridis
// Hover: tooltip with %, year range
// Click: highlight party+caste nodes in main graph
```

### Policy Tracer
```javascript
// BFS from policy node following 'policy_continuity' edges
// Direction: both (ancestors + descendants)
// Visual: highlight path, dim others
// Panel: show policy chain with years, parties, key provisions
```

### Counterfactual
```javascript
// Remove node + incident edges
// Recalculate: connected components, centrality shifts
// Heuristic: if party removed, its caste_base_overlap edges redistribute to nearest ally
// Display: side-by-side "Actual" vs "Counterfactual" mini-graphs
```

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Nodes represented | 40+ (parties, leaders, policies, castes, elections) |
| Edges represented | 60+ (all types) |
| Timeline coverage | 1916-2026 continuous |
| Interactive modes working | 4/4 |
| Load time (HTML) | <3 seconds |
| Mobile responsive | Yes (stacked layout) |
| Vault integration | Linked from MOC, openable in Obsidian |

---

## Related Notes

- [[Cross-Domain Idea Synthesis]] — Parent idea
- [[05 - MAPS/Indian Political History MOC]] — Primary domain map
- [[05 - MAPS/AI & Technology MOC]] — Tech project map (graph viz)
- [[graphify-repo/graphify/]] — Graph generation library
- [[professional_vault_graph.py]] — Your graph scripts
- [[obsidian_graph.html]] — Static graph reference
- [[genericagent/memory/autonomous_operation_sop.md]] — Agent framework
- [[house-rules.md]] — Night Shift rules
- [[2-atoms/Digital Garden.md]] — Digital garden philosophy
- [[2-atoms/Combinatorial Growth — Ideas Connect Non-Linearly.md]] — Non-linear exploration

---

*Created: 2026-07-08 | Status: Ready to implement | Priority: #3 of Cross-Domain Top 3 | First Sprint: 2026-07-28*