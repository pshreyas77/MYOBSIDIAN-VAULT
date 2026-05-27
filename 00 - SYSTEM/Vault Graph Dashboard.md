# Vault Graph Dashboard

[Open Analyzer](http://localhost:8080/00%20-%20SYSTEM/Tools/vault_analyzer.html)

*Drop your `.understand-anything/knowledge-graph.json` into the browser window*

## 📊 Quick Access to Current Analysis

### God Node Dashboard
See your current God nodes and connections: [[00 - SYSTEM/01_KNOWLEDGE_HUB.md]]

### Exploration Queries
Ready-to-use Dataview queries: [[00 - SYSTEM/Graph Exploration Queries.md]]

### Maintenance Reference
Quick reference for tags, schedules, and troubleshooting: [[00 - SYSTEM/QUICK_REFERENCE.md]]

### Analysis Reports
Latest generated reports: [[00 - SYSTEM/Graph Reports/]]

## 🔄 How to Update

1. **Generate fresh knowledge graph**:
   ```bash
   cd /home/sunny77/.understand-anything/repo
   bash install.sh codex  # if not already installed
   ~/.agents/skills/understand/resources/run.sh /home/sunny77/Documents/Obsidian Vault --no-viz
   ```

2. **Update visualization**:
   - The local server at http://localhost:8080/00%20-%20SYSTEM/Tools/vault_analyzer.html will automatically use the latest knowledge-graph.json
   - Or manually copy: `cp .understand-anything/knowledge-graph.json /home/sunny77/Documents/Obsidian Vault/00 - SYSTEM/Tools/`

3. **Run full analysis toolkit**:
   ```bash
   /home/sunny77/Documents/Obsidian Vault/00 - SYSTEM/run_analysis.sh
   ```

## 💡 Pro Tips

- The analyzer works best with the latest knowledge-graph.json from Understand-Anything
- You can drag-and-drop the JSON file directly into the browser window to load different analyses
- The visualization shows:
  - Node size = connection count (God nodes appear larger)
  - Node color = community membership
  - Edge thickness = connection strength/confidence
  - Interactive exploration: drag nodes, zoom, click for details

## 🎯 Current Focus Areas

Based on your latest analysis:
- **Top God Nodes**: now() (2,311), map() (1,944), error() (1,056), Values() (1,026)
- **Key Bridge**: Task node (697 edges) connects technical and conceptual domains
- **Community Structure**: 352 communities detected
- **Edge Quality**: 52% extracted (your wikilinks), 48% inferred (AI-discovered), 0.75 avg confidence