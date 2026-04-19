---
title: "Obsidian Graph Settings - AI Context Configuration"
tags: [obsidian, graph-view, settings, configuration, ai-context]
category: meta
created: 2026-04-11
related: [[00_Index]]
---

# Obsidian Graph Settings: AI Context Configuration

> **Preset Name:** `AI Context`  
> **Purpose:** Optimized for knowledge graph analysis with AI-assisted research  
> **Created:** 2026-04-11

---

## 🔷 Global Graph Settings

### Visual Parameters

| Setting | Value | Purpose |
|---------|-------|---------|
| **Node Size Multiplier** | 0.5 (small) | High density visibility - see more nodes at once |
| **Line Size Multiplier** | 0.4 | Thin links reduce visual clutter |
| **Text Fade Threshold** | 0.4 | Text labels fade at this zoom level |
| **Show Arrow** | ✅ ON | Directional flow for knowledge relationships |

### Force Physics

| Setting | Value | Effect |
|---------|-------|--------|
| **Repel Strength** | 12 | Keeps nodes spread but not too far |
| **Center Strength** | 0.4 | Moderate gravity toward center |
| **Link Strength** | 1.0 | Full link force for structure |
| **Link Distance** | 220 | Optimal spacing between connected nodes |

---

## 🔷 Color Groups (Hex → RGB Conversion Applied)

### Group Definitions

| # | Rule | Color | Hex | RGB Value | Purpose |
|---|------|-------|-----|-----------|---------|
| 1 | `path:MOCs` | Coral Red | #FF6B6B | `16738235` | 🔴 Hub/MOC notes - highest visibility |
| 2 | `tag:#ai-generated` | Teal | #4ECDC4 | `5157118` | 🟢 AI-created content |
| 3 | `tag:#status/stub` | Gray | #95A5A6 | `9803158` | ⚪ Empty/placeholder notes |
| 4 | `tag:#status/mature` | Green | #2ECC71 | `13161158` | 🟢 Finished/completed notes |
| 5 | `tag:#concept` | Purple | #9B59B6 | `10184958` | 🟣 Abstract ideas/concepts |
| 6 | `path:Projects` | Orange | #F39C12 | `15956070` | 🟠 Active work items |
| 7 | `path:"Daily Notes"` | Blue | #3498DB | `3440568` | 🔵 Daily journal entries |

### Visual Hierarchy
```
HUBS (Red) → PROJECTS (Orange) → AI-CONTENT (Teal) → ACTIVE (Green/Blue) → CONCEPTS (Purple) → INCOMPLETE (Gray)
```

---

## 🔷 Filters (Applied)

```
search: -path:attach -path:template -path:Attachments
showAttachments: false
showTags: true
```

**Hidden:**
- `path:attach` - Attachment folders
- `path:template` - Template folders  
- `path:Attachments` - All attachment directories

**Shown:**
- Tags displayed on nodes
- Orphan notes visible
- Unresolved links shown

---

## 🔷 Local Graph Settings ("AI Context" Preset)

**Depth:** 2 levels of connection
**Neighbor Links:** OFF (cleaner local view)
**Attachments:** Hidden
**Tags:** Visible

### Use Cases for Local Graph

1. **Research Context** - See 2 hops of related research
2. **Writing Connection** - Find related notes while writing
3. **Concept Clustering** - View concept neighborhood
4. **Gap Analysis** - Identify missing connections

---

## 🔷 File Locations

| Config | Path |
|--------|------|
| **Global Graph** | `.obsidian/graph.json` |
| **AI Context Preset** | `.obsidian/plugins/graph-presets/data.json` |

---

## 🔷 Manual Hex to RGB Conversion (for reference)

If you need to convert hex colors for `rgb` field in Obsidian:

```python
def hex_to_obsidian_rgb(hex_color):
    """Convert #RRGGBB to Obsidian's decimal RGB format"""
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r << 16) + (g << 8) + b

# Examples:
# #FF6B6B → 16738235
# #4ECDC4 → 5157118
# #95A5A6 → 9803158
# #2ECC71 → 3105828
# #9B59B6 → 10184958
# #F39C12 → 15956070
# #3498DB → 3440568
```

---

## 🔷 Reset Commands

If you need to restore Obsidian's defaults:

**Global Graph:** Open Graph View → Settings (gear icon) → Restore Defaults

Or manually edit `.obsidian/graph.json`:

```json
{
  "collapse-filter": true,
  "search": "",
  "showTags": false,
  "showAttachments": true,
  "hideUnresolved": false,
  "showOrphans": true,
  "collapse-color-groups": true,
  "colorGroups": [],
  "collapse-display": true,
  "showArrow": false,
  "textFadeMultiplier": -0.2,
  "nodeSizeMultiplier": 1,
  "lineSizeMultiplier": 1,
  "collapse-forces": true,
  "centerStrength": 0.5,
  "repelStrength": 10,
  "linkStrength": 1,
  "linkDistance": 30,
  "scale": 0.5,
  "close": false
}
```

---

## 🔷 Tips for AI Context Usage

### Best Practices

1. **MOCs in Red** - Make your Maps of Content visually prominent
2. **Stubs in Gray** - Quick identification of notes needing expansion  
3. **Mature notes in Green** - Completed research ready for citation
4. **Projects in Orange** - Active work clearly distinguished
5. **Concepts in Purple** - Abstract theories stand out

### Workflow Integration

```
1. Create note → Add #status/stub (Gray)
2. Draft with AI → Add #ai-generated (Teal)  
3. Review/completion → Change to #status/mature (Green)
4. Link to MOC → Appears in Red hub network
5. Connect concepts → Purple nodes cluster
```

---

## 📊 Visual Summary

```
┌─────────────────────────────────────────────────────────────┐
│                    COLOR HIERARCHY                           │
├─────────────────────────────────────────────────────────────┤
│  🔴 RED    → Hubs/MOCs (most important navigation points)    │
│  🟠 ORANGE → Projects (active work)                        │
│  💚 GREEN  → Mature content (complete)                     │
│  🟢 TEAL   → AI-generated (from Claude)                    │
│  🔵 BLUE   → Daily notes (temporal context)               │
│  🟣 PURPLE → Concepts (abstract ideas)                     │
│  ⚪ GRAY   → Stubs (need work)                           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                   PHYSICS SETTINGS                          │
├─────────────────────────────────────────────────────────────┤
│  Repel: 12         → Good spread without chaos             │
│  Center: 0.4       → Moderate gravity                       │
│  Distance: 220     → Readable spacing                       │
│  Show Arrows: ON   → Directional relationships visible     │
└─────────────────────────────────────────────────────────────┘
```

---

*Configuration applied: 2026-04-11*
*Files modified: graph.json, plugins/graph-presets/data.json*
