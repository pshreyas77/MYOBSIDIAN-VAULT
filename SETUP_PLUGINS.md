# Obsidian Plugins Setup

## Required Obsidian Plugins — Install These

Open Obsidian → Settings → Community Plugins → Browse

### Must Install:
- **Smart Connections** — semantic search across vault (AI-powered)
- **Dataview** — query notes like a database
- **Templater** — note templates with dynamic content
- **QuickAdd** — fast capture from anywhere
- **Calendar** — daily notes navigation
- **Obsidian Web Clipper** — browser extension, clips articles to vault

### Already Installed (verify):
- calendar, dataview, terminal, advanced-canvas, tag-wrangler
- templater-obsidian, quickadd, excalidraw, smart-connections

### Smart Connections Config:
1. Settings → Smart Connections → Set vault path
2. Enable: "Show connections in sidebar"
3. This gives semantic linking WITHOUT needing extra API calls.

### Web Clipper (browser extension):
1. Install from: https://obsidian.md/clipper
2. Set save folder to: `raw-sources/`
3. Set template to include: URL, date, title, content as markdown
4. After clipping: run `/ingest` in Claude Code