# Graph View Color Configuration

## Quick Setup Instructions

Since Obsidian overwrites `graph.json` automatically, you need to manually configure color groups in Obsidian:

### Step 1: Open Graph View
1. Press `Ctrl+G` (or Cmd+G) to open **Global Graph**
2. Or open a file and click the graph icon for **Local Graph**

### Step 2: Configure Color Groups

Click **"Display"** → **"Color Groups"** → Toggle **ON**

Add these color groups in order:

#### AI Agent Vaults
| Query | Color | Purpose |
|-------|-------|---------|
| `path:/ClaudeVault` | #DC2626 🔴 Red | Claude research |
| `path:/QwenVault` | #0D9488 🟢 Teal | Qwen research |
| `path:/DeepseekVault` | #EAB308 🟡 Amber | Deepseek research |
| `path:/KIMI_VAULT` | #EC4899 🩷 Pink | Kimi chats |

#### Areas (Research Topics)
| Query | Color | Purpose |
|-------|-------|---------|
| `path:/02 - Areas/Ancient Civilizations` | #F97316 🟠 Orange | Archaeology |
| `path:/02 - Areas/Buddhism & Hinduism` | #EF4444 🔴 Red | Religion |
| `path:/02 - Areas/Religion & Cosmology` | #A855F7 🟣 Purple | Theology |
| `path:/02 - Areas/Political Analysis` | #3B82F6 🔵 Blue | Politics |
| `path:/02 - Areas/AI Research & Agents` | #8B5CF6 💜 Violet | AI |

#### Topics
| Query | Color | Purpose |
|-------|-------|---------|
| `path:/07 - Topics/Ancient_Civilizations` | #EA580C 🔶 Orange | Ancient |
| `path:/07 - Topics/Buddhism_and_Hinduism` | #B91C1C 🩸 Dark Red | Religion |
| `path:/07 - Topics/Religion_and_Cosmology` | #A855F7 🟣 Purple | Cosmology |
| `path:/07 - Topics/Politics_and_Governance` | #3B82F6 🔵 Blue | Politics |
| `path:/07 - Topics/AI_and_Machine_Learning` | #8B5CF6 💜 Violet | AI/ML |
| `path:/07 - Topics/Science_and_Space` | #0EA5E9 🩵 Sky | Science |
| `path:/07 - Topics/Technology_and_Development` | #10B981 🟢 Emerald | Tech |
| `path:/07 - Topics/Philosophy_and_Ethics` | #7C3AED 💜 Violet | Philosophy |
| `path:/07 - Topics/Finance_and_Economics` | #059669 🟢 Green | Finance |

#### Special Tags
| Query | Color | Purpose |
|-------|-------|---------|
| `tag:#MOC` | #000000 ⬛ Black | Maps of Content |
| `tag:#research` | #B91C1C 🔴 Research marker | Research files |
| `tag:#index` | #111827 ⬛ Dark | Index files |

### Step 3: Enable CSS Enhancements
1. Open Obsidian → Settings → Appearance
2. Under **CSS Snippets**, enable:
   - ✅ `enhanced-graph-colors.css`
   - ✅ `optimized-graph-view.css`

### Step 4: Graph View Settings (Recommended)

In Graph View → **Display** settings:
- ✅ Show tags
- ✅ Hide unresolved (no target notes)
- ❌ Show orphans (reduce clutter)
- ✅ Color Groups (turnded ON)

**Forces & Layout:**
- Center force: 0.6
- Repel force: 15
- Link force: 0.3
- Link distance: 180

---

## Auto-Restore Script

Run this to restore colors if they disappear:
```bash
bash "/home/sunny77/Documents/Obsidian Vault/.obsidian/apply-graph-colors.sh"
```

Note: This only works when Obsidian is closed.

