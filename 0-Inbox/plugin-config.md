# Obsidian Plugin Configuration — 50K-Node Second Brain

**Philosophy**: Minimal, stable, composable. Each plugin must earn its keep for a knowledge base of this scale.

---

## ✅ Kept (7 Community Plugins)

| Plugin | Purpose | Why for 50K nodes |
|--------|---------|-------------------|
| **Calendar** | Daily notes navigation | Native daily-notes integration; timeline view for journaling |
| **Dataview** | Query engine | The SQL of Obsidian — MOCs, project dashboards, automated indexes |
| **Tag Wrangler** | Tag management | Merge/rename/split tags at scale; essential for 50k-node hygiene |
| **Templater** | Advanced templates | Scriptable templates (JS), dynamic dates, prompting — beats core Templates |
| **QuickAdd** | Capture workflows | Macros, choice prompts, multi-step capture — frictionless input |
| **Excalidraw** | Visual thinking | Hand-drawn diagrams, architecture sketches, concept maps embedded in notes |
| **Style Settings** | Theme config | 200+ Minimal theme tweaks without CSS; live preview |

---

## ❌ Removed (and why)

| Plugin | Reason |
|--------|--------|
| **Advanced Canvas** | Core Canvas (disabled) covers basics; AC adds overhead for marginal gain |
| **Terminal** | Security risk in knowledge vault; use external terminal |
| **URL Webview Opener** | Browser does this better; reduces vault attack surface |
| **Smart Connections** | Vector search on 50k nodes = slow + resource-heavy; use MemPalace/Graphify instead |
| **AI Providers** | External API calls in vault = privacy risk; use local LLMs (Ollama) via external tools |
| **Smart Lookup** | Redundant with browser + Dataview queries |
| **Graph Presets** | Graph.json + hotkeys (see `graph-presets.md`) replaces this; one less plugin |

---

## 🔧 Core Plugins (14 enabled / 18 disabled)

### Enabled — Daily Drivers
- **File Explorer** — Navigation
- **Global Search** — `Ctrl+Shift+F` full-text
- **Switcher** — `Ctrl+O` quick open
- **Graph** — Global + Local view (color groups configured)
- **Backlinks** — Pane for incoming links
- **Outgoing Links** — Pane for outgoing links
- **Tag Pane** — Tag browser (with Tag Wrangler)
- **Properties** — Frontmatter UI
- **Page Preview** — `Ctrl+Hover` peek
- **Daily Notes** — `Ctrl+Shift+N` journal
- **Templates** — Core fallback (Templater primary)
- **Command Palette** — `Ctrl+P`
- **Editor Status** — Word count, position
- **Bookmarks** — Saved searches, frequent queries
- **Word Count** — Stats in status bar
- **Workspaces** — Layout presets (Research, Writing, Review)
- **File Recovery** — Safety net
- **Sync** — *Disabled* (you use git/Obsidian Sync externally)

### Disabled — Bloat Reduction
- **Canvas** — Visual but heavy; Excalidraw covers diagrams
- **Footnotes** — Rarely used; syntax works without plugin
- **Note Composer** — QuickAdd macros do this better
- **Slash Command** — Templater + QuickAdd cover insertion
- **ZK Prefixer** — Not a Zettelkasten; PARA structure used
- **Random Note** — Novelty only
- **Slides** — Export to Reveal.js/Pandoc instead
- **Audio Recorder** — External tool preferred
- **Markdown Importer** — One-time use only
- **Bases** — Experimental; Dataview covers tables
- **Web Viewer** — Security surface

---

## ⚙️ Recommended Plugin Settings

### Dataview
```yaml
# Settings → Dataview
enableInlineQueries: true
enableJsQueries: true  # For complex MOCs
cacheLength: 50000     # Full vault index
```

### Templater
```yaml
# Settings → Templater
templateFolder: "00 - SYSTEM/Templates"
triggerOnFileCreation: true
syntaxHighlighting: true
```

### QuickAdd
**Macros to create** (Settings → QuickAdd → Manage Macros):
1. **Daily Capture** → Append to daily note + tag `#capture`
2. **Literature Note** → Create in `01 - LITERATURE/` with YAML + prompt for citekey
3. **Project Spin-up** → Create project folder + MOC + tasks
4. **MOC Update** → Run Dataview query to refresh MOC

### Tag Wrangler
- **Auto-show count**: ON
- **Merge confirmation**: ON
- **Case sensitivity**: OFF (normalize to lowercase)

### Style Settings (Minimal Theme)
Key toggles (Settings → Style Settings → Minimal):
- **Typography** → Line width: `88%`, Line height: `1.7`
- **Headings** → Style: `Normal`, Weights: `600/600/500/500/500/400`
- **Focus Mode** → Type: `Paragraph`, Dim: `0.4`
- **Status Bar** → Show: `Word count`, `Character count`, `Reading time`
- **File Explorer** → Show: `Created time`, `Modified time`, `Word count`
- **Graph** → Node size multiplier: `1.3`, Line opacity: `0.7`

### Excalidraw
- **Default theme**: Dark
- **Embed PDFs**: ON
- **LaTeX**: ON (for math notes)
- **Mermaid**: ON (diagrams)

---

## 📦 Suggested Additions (Install as Needed)

| Plugin | Use Case |
|--------|----------|
| **Various Complements** | Autocomplete for tags/links/wikilinks — huge speedup |
| **Omnisearch** | Better search UX (regex, filters) |
| **Linter** | Auto-format markdown, fix frontmatter, enforce style |
| **Periodic Notes** | Weekly/monthly/quarterly reviews (builds on Daily Notes) |
| **Projects** | Kanban board from Dataview queries (if you want boards) |
| **Note Refactor** | Split/merge/extract notes safely |
| **Custom Frames** | Embed web tools (Notion, Figma, etc.) in notes |
| **Highlightr** | Better `==highlight==` colors per tag |

---

## 🛡️ Security & Performance Notes

1. **No network plugins** — All 7 kept plugins are fully local
2. **No background indexing** — Dataview caches on demand; no CPU drain
3. **No auto-sync** — You control git/Obsidian Sync externally
4. **Plugin folder cleaned** — Removed dirs moved to `plugins-removed/` (recoverable)

---

## 🔄 Maintenance

**Monthly**:
- Tag Wrangler: Review unused tags → merge/delete
- Dataview: Clear cache if stale (Settings → Dataview → Clear Cache)
- Templater: Update templates for workflow changes

**Quarterly**:
- Audit community plugins for updates/security
- Review QuickAdd macros for friction points
- Export Dataview MOCs as markdown for portability