# 🔧 OBSIDIAN SETUP GUIDE
## Optimized Configuration for Research & Knowledge Management

---

## ✅ CURRENT STATUS

### Theme: Minimal
- **Best for:** Clean, distraction-free research
- **Why over ITS Theme:** Better typography, native Obsidian integration, faster
- **Font:** Inter (interface), JetBrains Mono (code)
- **Accent Color:** Blue (#4a9eff)

### Installed Plugins: 12
| Plugin | Purpose | Status |
|--------|---------|--------|
| Calendar | Daily notes & journaling | ✅ Active |
| Dataview | Database queries & tables | ✅ Active |
| Terminal | Command-line access | ✅ Active |
| Copilot | AI assistance | ✅ Active |
| Claude Code | Claude integration | ✅ Active |
| AI Providers | Multiple AI models | ✅ Active |
| Smart Connections | Semantic search | ✅ Active |
| Tag Wrangler | Tag management | ✅ Active |
| Smart Lookup | Related notes | ✅ Active |
| BRAT | Beta plugin manager | ✅ Active |
| Advanced Canvas | Enhanced canvases | ✅ Active |
| URL Webview | Web pages in notes | ✅ Active |

### Recommended Additional Plugins
Install these via Settings → Community Plugins → Browse:

| Plugin | Purpose | Why Recommended |
|--------|---------|-----------------|
| **Minimal Theme** | (Already set) | Clean, fast, professional |
| **Breadcrumbs** | Visual navigation | Navigate hierarchy easily |
| **Supercharged Links** | Enhanced links | Color-code by folder |
| **Templater** | Advanced templates | Dynamic note creation |
| **QuickAdd** | Quick commands | Fast capture |
| **Excalidraw** | Hand-drawn diagrams | Visual thinking |
| **DB Folder** | Database views | Dataview alternative UI |
| **Hover External Link** | Link previews | See URLs without clicking |
| **Paste Image Rename** | Image organization | Auto-rename pasted images |
| **Image Adjuster** | Image sizing | Resize images in editor |

---

## 🎨 APPEARANCE SETTINGS (Already Applied)

### Theme Configuration
```json
{
  "theme": "obsidian",
  "cssTheme": "Minimal",
  "accentColor": "#4a9eff",
  "baseFontSize": 16,
  "interfaceFontFamily": "Inter, sans-serif",
  "textFontFamily": "Inter, Georgia, serif",
  "monospaceFontFamily": "JetBrains Mono, monospace",
  "highlightCurrentLine": true
}
```

### Color-Coded Folders (Graph View)
| Folder | Color | Hex Code |
|--------|-------|----------|
| BUDDHA/ | Gold/Yellow | #f4d03f |
| OLDEST CIVILIZATION/ | Blue | #3498db |
| COSMOLOGY/ | Purple | #9b59b6 |
| QwenVault/ | Green | #27ae60 |
| KIMI VAULT/ | Red | #e74c3c |

---

## 📐 GRAPH VIEW SETTINGS (Already Applied)

### Optimized for Research:
- ✅ Tags visible
- ✅ Arrows enabled (shows directionality)
- ✅ Text fade: Moderate (-0.5)
- ✅ Node size: Balanced (1.3x)
- ✅ Line size: Visible (0.8x)
- ✅ Show orphans: Yes (isolated nodes visible)
- ✅ Hide unresolved: Yes (cleaner view)
- ✅ Link distance: 35px (readable spacing)

### How to Access:
1. Press `Ctrl/Cmd + G` (or click Graph icon in left sidebar)
2. Click "Settings" (gear icon) for additional options
3. Filters let you exclude folders from view

---

## 🎯 RECOMMENDED WORKSPACE LAYOUT

### Split-Pane Research Setup:
```
┌──────────────────┬─────────────────┐
│                  │                 │
│   Current Note   │   Linked Notes  │
│   (Main Pane)    │  (Backlinks/    │
│                  │   Graph View)    │
│                  │                 │
├──────────────────┴─────────────────┤
│       Canvas / Overview            │
│    (Optional third pane)           │
└────────────────────────────────────┘
```

### To Set Up:
1. Open a note
2. Drag the "Backlinks" tab to the right side
3. Drag the "Global Graph" or a canvas to the bottom
4. Save as workspace: `Ctrl/Cmd + P` → "Workspaces: Manage"

---

## 🔑 KEYBOARD SHORTCUTS CUSTOMIZATION

Add these in Settings → Hotkeys:

| Action | Recommended Key |
|--------|-----------------|
| Open Graph View | `Ctrl/Cmd + G` (default) |
| Quick Switcher | `Ctrl/Cmd + O` (default) |
| Command Palette | `Ctrl/Cmd + P` (default) |
| Toggle Left Sidebar | `Ctrl/Cmd + Shift + L` |
| Toggle Right Sidebar | `Ctrl/Cmd + Shift + R` |
| New Note | `Ctrl/Cmd + N` |
| Insert Template | `Ctrl/Cmd + T` |
| Daily Note | `Ctrl/Cmd + Shift + D` |
| Canvas: New | `Ctrl/Cmd + Shift + C` |

---

## 📋 RESEARCH WORKFLOW TIPS

### For Note-Taking:
1. Use `[[wiki-links]]` liberally — they power the graph
2. Add `tags: [research-topic]` in frontmatter
3. Use Dataview tables for structured data
4. Create canvas links for visual navigation

### For Large Vaults (~450+ files):
1. Use folders for broad categories (BUDDHA/, OLDEST CIVILIZATION/)
2. Use tags for cross-cutting themes (#temple-destruction, #archaeology)
3. Use MOCs (Master Link Index, RESEARCH HUB) for navigation
4. Pin frequently used notes to sidebar

### Graph View Best Practices:
1. Filter out templates and daily notes (too noisy)
2. Color-code by folder/theme
3. Show arrows to understand connections
4. Click-drag to reorganize nodes
5. Use "Local Graph" (left sidebar) for focused view

---

## 🔧 TROUBLESHOOTING

### Slow Performance?
- Disable live preview for large files
- Use "Readable line length" setting
- Limit plugins (you have good amount: 12)
- Turn off "Spellcheck" if not needed

### Graph Too Cluttered?
- Filter out daily notes (`-path:"Daily Notes"`)
- Filter out attachments (`-file:.png -file:.jpg`)
- Group by color (already set up)

### Mobile Sync?
- Enable Obsidian Sync ($8/month) or use free alternatives:
  - Git + Working Copy (iOS)
  - Git + FolderSync (Android)
  - Syncthing (self-hosted)

---

## 🚀 CUSTOM CSS SNIPPETS (Already Applied)

File: `.obsidian/snippets/research-enhancements.css`

### Features Applied:
- ✅ Better tables for research data
- ✅ Color-coded graph groups
- ✅ Enhanced sidebar styling
- ✅ Wiki-link visual improvements
- ✅ Canvas optimizations

---

## 📦 BACKUP STRATEGY

### Recommended:
1. **Git + GitHub** (free, versioned)
   ```bash
   cd "/home/sunny77/Documents/Obsidian Vault"
   git init
   git add .
   git commit -m "Initial vault backup"
   ```

2. **Obsidian Official Sync** (paid, easiest)

3. **Local Backup** (Safest alongside cloud)
   - Weekly: Copy vault to external drive
   - Monthly: Archive old versions

---

## ✨ NEXT STEPS

### Immediate Actions:
1. ✅ **Theme switched to Minimal** (cleaner)
2. ✅ **Graph view color-coded** by folder
3. ✅ **CSS snippets applied** for research
4. ⏳ Install recommended plugins (optional)
5. ⏳ Customize hotkeys (optional)

### Recommended Obsidian Settings to Change:
- Settings → Files & Links → **New link format**: `Shortest path`
- Settings → Files & Links → **Default location for new attachments**: `In the folder specified below`
- Settings → Files & Links → **Attachment folder path**: `Assets`
- Settings → Editor → **Line wrap**: `Soft wrap`
- Settings → Appearance → **Translucent window**: `Off` (performance)
- Settings → Appearance → **Show inline title**: `On`

---

## 📊 YOUR VAULT METRICS

| Stat | Current |
|------|---------|
| Total files | ~451 |
| Markdown files | ~350+ |
| Canvas files | 4+ |
| Connected themes | 7 |
| Bidirectional links | ~100+ |
| Plugins active | 12 |

---

*Setup optimized: 2026-04-09*
*Recommended theme: Minimal*
*Graph coloring: Active*
