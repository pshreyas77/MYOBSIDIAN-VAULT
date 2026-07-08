---
date: 2026-07-08
type: system
tags: [system, graph-view, obsidian, configuration, color-groups]
status: active
ai-first: true
---

# Obsidian Graph View — Professional Color Configuration

**For future Claude:** This note documents the professional color-coded graph view configuration applied to your vault. The `.obsidian/graph.json` file has been updated with 19 category-based color groups.

---

## 🎨 Color Groups Applied

| # | Category | Emoji | Color | Query Basis |
|---|----------|-------|-------|-------------|
| 1 | **MOCs (Maps of Content)** | 🗺️ | `#4E79A7` (Blue) | `tag:#moc OR path:05 - MAPS` |
| 2 | **Active Projects** | 🚀 | `#A0C4E8` (Light Blue) | `path:03 - PROJECTS` (excl. refs) |
| 3 | **Daily Notes** | 📅 | `#6BA4D6` (Sky Blue) | `path:04 - DAILY` |
| 4 | **Politics & Governance** | 🏛️ | `#E15759` (Red) | Indian politics, TVK, BJP, RSS |
| 5 | **Philosophy & Philosophy & Religion** | 🧠 | `#B07AA1` (Purple) | Anti-caste, rationalism, Indian philosophy |
| 6 | **History & Civilizations** | 📜 | `#9C755F` (Brown) | Ancient civs, archaeology, IVC |
| 7 | **Population Genetics** | 🧬 | `#76B7B2` (Teal) | aDNA, admixture, ANI/ASI |
| 8 | **Historical Linguistics** | 📝 | `#59A14F` (Green) | Comparative method, PIE, Mitanni |
| 9 | **Epigraphy & Evidence** | 🏺 | `#EDC948` (Gold) | Inscriptions, evidence grading |
| 10 | **AI & Technology** | 🤖 | `#F28E2B` (Orange) | Agents, MCP, Ollama, local LLMs |
| 11 | **Health & Fitness** | 💪 | `#FF9DA7` (Pink) | 12-week protocol, supplements |
| 12 | **PKM & Digital Garden** | 🌱 | `#4E79A7` (Blue) | Progressive summarization, publishing |
| 13 | **Historical Figures** | 👤 | `#E15759` (Red) | wiki/entities (people) |
| 14 | **Organizations & Movements** | 🏛️ | `#F28E2B` (Orange) | Parties, DK, DMK, RSS, TVK |
| 15 | **Concepts & Theories** | 💭 | `#B07AA1` (Purple) | wiki/concepts, abstract ideas |
| 16 | **Literature Notes** | 📚 | `#76B7B2` (Teal) | 01-LITERATURE, papers, articles |
| 17 | **Outputs & Essays** | ✨ | `#EDC948` (Gold) | 06-OUTPUTS, finished work |
| 18 | **System & Templates** | ⚙️ | `#BAB0AC` (Gray) | 00/07-SYSTEM, templates |
| 19 | **Inbox & Fleeting** | 📥 | `#BAB0AC` (Gray) | 00-INBOX, fleeting, QUEUE |

---

## ⚙️ Graph View Settings (Optimized)

```json
{
  "collapse-filter": false,
  "showTags": true,
  "showAttachments": false,
  "hideUnresolved": true,
  "showOrphans": true,
  "collapse-color-groups": true,
  "collapse-display": true,
  "showArrow": true,
  "textFadeMultiplier": 0,
  "nodeSizeMultiplier": 1.2,
  "lineSizeMultiplier": 1,
  "centerStrength": 0.35,
  "repelStrength": 8.5,
  "linkStrength": 0.85,
  "linkDistance": 220,
  "scale": 0.02
}
```

### Key Optimizations:
- **`showTags: true`** — Tags visible on nodes
- **`collapse-color-groups: true`** — Collapsible legend in sidebar
- **`nodeSizeMultiplier: 1.2`** — Slightly larger nodes for readability
- **`linkDistance: 220`** — Better spacing for large vault
- **`repelStrength: 8.5`** — Prevents overcrowding
- **`showArrow: true`** — Directional edges (wikilinks have direction)

---

## 🎯 How to Use

### In Obsidian:
1. **Open Graph View** — `Ctrl/Cmd + G` or sidebar icon
2. **Open Sidebar** (right panel) — Shows color legend
3. **Click any category** — Toggles visibility (dimmed = hidden)
4. **Search box** — Filter nodes by name
5. **Hover node** — Shows connections, metadata
6. **Click node** — Opens note, centers graph

### Pro Tips:
- **Filter by tag**: Type `#moc` in search to see only MOCs
- **Filter by path**: Type `path:03 - PROJECTS` for projects only
- **Community detection**: Communities auto-colored in graphify HTML export
- **Canvas export**: Run `graphify to_canvas` for infinite canvas layout

---

## 🔧 Regenerate Colors

If you add new categories or change structure:

```bash
cd E:/_Knowledge/ObsidianVault
python scripts/generate_graph_colors.py
```

This script (`scripts/generate_graph_colors.py`) contains the full configuration and can be modified to add/remove categories.

---

## 📊 Color Design Principles

| Principle | Implementation |
|-----------|----------------|
| **Semantic grouping** | Related domains share hue families (politics=reds, philosophy=purples) |
| **Dark theme native** | All colors tested on `#0f0f1a` / `#1a1a2e` backgrounds |
| **Colorblind safe** | Distinct hues, not just saturation shifts |
| **Hierarchy clarity** | Structural (blue) → Domain (warm) → Entity (saturated) → Note type (muted) |
| **Scalable** | 19 groups fit in sidebar; collapsible for focus |

---

## 🔗 Related Files

| File | Purpose |
|------|---------|
| `.obsidian/graph.json` | Live graph view config (auto-generated) |
| `scripts/generate_graph_colors.py` | Generator script (source of truth) |
| `graphify-repo/graphify/export.py` | graphify HTML/Canvas export with community colors |
| `obsidian_graph.html` | Static HTML export (from graphify) |

---

*Generated: 2026-07-08 | Script: `scripts/generate_graph_colors.py` | Groups: 19 | Vault: 5,785+ markdown files*