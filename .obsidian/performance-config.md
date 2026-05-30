# Performance Optimization for Low-End Systems
## 8GB RAM / CPU Only / No GPU

---

## ⚡ QUICK FIXES (Do These First)

### 1. Disable Heavy Plugins
These plugins consume the most resources:

| Plugin | Impact | Action |
|--------|--------|--------|
| **Smart Connections** | 🔴 Very High | Disable or limit to small folders only |
| **Dataview** | 🟡 Medium-High | Reduce query complexity, disable auto-refresh |
| **Copilot** | 🔴 High | Disable when not actively using |
| **Smart Lookup** | 🟡 Medium | Disable if not needed |
| **Tag Wrangler** | 🟢 Low | Keep if needed |
| **Calendar** | 🟢 Low | Keep if needed |

### 2. Graph View Settings (Already Optimized)
Your graph.json is configured for performance:
- `nodeSizeMultiplier: 0.76` (reduced)
- `linkDistance: 30` (lower = less calculation)
- `repelStrength: 20` (reduced)
- `centerStrength: 1` (balanced)

---

## 🔧 APP SETTINGS (app.json - Applied)

### Disabled Features:
- ❌ Line highlighting
- ❌ Link auto-updates (manual only)
- ❌ Spellcheck
- ❌ PDF page preview
- ❌ Backlinks (use manual instead)
- ❌ Outgoing links panel
- ❌ Daily notes
- ❌ Word count
- ❌ Editor status bar
- ❌ File recovery (manual backups instead)
- ❌ Sync (disabled)

### Enabled for Performance:
- ✅ Fold headings (collapsible)
- ✅ Fold indents (collapsible)
- ✅ Markdown links (faster than wiki-links)
- ✅ Live preview (lighter than full preview)

---

## 🌐 GRAPH VIEW OPTIMIZATION

### In-Obsidian Settings:
1. Open Graph View
2. Click **Filter** (funnel icon)
3. Enable:
   - ✅ "Hide unresolved" (reduces node count)
   - ✅ "Collapse filter"
4. Disable:
   - ❌ "Show tags" (adds clutter)
   - ❌ "Show attachments"
   - ❌ "Show orphans"

---

## 🧠 SMART CONNECTIONS OPTIMIZATION

If you keep it, configure for low resource use:

```json
{
  "api_key": "",
  "excluded_directories": [
    "QwenVault",
    "ObsidianVault",
    "ClaudeVault",
    "KIMI VAULT"
  ],
  "embeddings_model": "text-embedding-3-small",
  "max_file_size": 100000,
  "excluded_extensions": [".canvas", ".png", ".jpg", ".pdf"]
}
```

**Recommendation:** Disable Smart Connections entirely for 8GB RAM.
It loads AI models into memory.

---

## 💾 DATAVIEW OPTIMIZATION

### Reduce Query Load:
1. Avoid `TABLE` queries on large folders
2. Use `LIMIT` in all queries:
   ```dataview
   TABLE file.mtime
   FROM "BUDDHA"
   LIMIT 50
   ```
3. Disable automatic refresh:
   - Settings → Dataview → "Automatic refresh interval: 0"
   - Manual refresh only (Ctrl+Shift+R)

---

## 📁 FILE MANAGEMENT

### Reduce Vault Size:
- Move `ObsidianVault/` files to external storage
- Compress old PDFs
- Delete unused images
- Archive completed projects

### Current Vault Status (~450 files):
- Keep under 500 files for smooth performance
- Split into multiple vaults if grows larger

---

## 🔥 CRITICAL: DISABLE THESE

### Plugin Management:
Settings → Community Plugins →
- ❌ Disable **Smart Connections**
- ❌ Disable **Copilot** (when not using)
- ❌ Disable **AI Providers**
- ❌ Disable **Terminal** (if not needed)
- ❌ Disable **URL Webview Opener**
- ❌ Disable **Obsidian42 BRAT**

### Core Plugin Cleanup:
Settings → Core Plugins →
- ❌ Backlinks
- ❌ Outgoing links
- ❌ Page Preview (huge memory hog)
- ❌ Daily Notes
- ❌ Word Count
- ❌ Editor Status
- ❌ Audio Recorder
- ❌ Web Viewer

---

## 🎨 APPEARANCE SETTINGS

### Theme Optimization:
- Use default Obsidian theme (lightest)
- Or minimal theme like "Minimal"
- Disable translucent windows (already off)
- Disable animations if possible

### CSS Snippet Impact:
Your `pro-graph-view.css` is optimized - no changes needed.

---

## 🚀 IMMEDIATE PERFORMANCE GAINS

### 1. Close Background Processes
In Obsidian:
- Don't leave graph view open constantly
- Close unused sidebars (Ctrl+\ to toggle)

### 2. Search Optimization
- Use quick switcher (Ctrl+O) instead of global search
- Global search refreshes entire vault index

### 3. File Loading
- Split view only when necessary
- Close tabs you aren't using
- Use "Close all other tabs" option

---

## 📊 MONITORING

### Check Resource Usage:
```bash
# In terminal, check Obsidian memory use:
ps aux | grep obsidian
```

Target: Obsidian using < 1GB RAM

---

## ✅ VERIFICATION CHECKLIST

After applying settings:
- [ ] Restart Obsidian completely
- [ ] Graph view loads in < 3 seconds
- [ ] Switching files has no lag
- [ ] Sidebar opens/closes smoothly
- [ ] Search results appear instantly
- [ ] No "Not responding" warnings

---

*Applied: 2026-04-10*
*Optimized for: 8GB RAM / CPU / No GPU*
