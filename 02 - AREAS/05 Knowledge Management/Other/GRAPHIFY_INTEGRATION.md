# Graphify Integration for Obsidian Vault

## Overview
Graphify is an AI-powered knowledge graph generator that analyzes your Obsidian vault to build an interactive graph of concepts and relationships.

## Installation

Graphify is already installed. To verify:
```bash
graphify --help
```

## Usage

### Quick Start

Run the provided script from your vault root:
```bash
bash graphify-vault.sh
```

### Manual Usage

Analyze the entire vault:
```bash
cd "/home/sunny77/Documents/Obsidian Vault"
graphify . --output graphify-out/
```

Analyze a specific folder:
```bash
graphify "07 - Topics/Ancient_Civilizations" --output graphify-out/
```

### Output Files

After running graphify, you'll find:

1. **graphify-out/graph.html** - Interactive HTML graph (open in browser)
2. **graphify-out/GRAPH_REPORT.md** - Analysis report with insights and suggestions
3. **graphify-out/graph.json** - Structured graph data for queries
4. **graphify-out/cache/** - Cached analysis for faster re-runs

### Query the Graph

Ask questions about your vault:
```bash
graphify query "What are the key concepts in Buddhism research?" \
  --graph graphify-out/graph.json
```

Find connections between topics:
```bash
graphify query "How does Ancient Civilizations connect to Philosophy?" \
  --graph graphify-out/graph.json --budget 3000
```

## Obsidian Integration

### View Interactive Graph

1. Run: `bash graphify-vault.sh`
2. Open `graphify-out/graph.html` in your browser
3. Or use the **Web Viewer** plugin in Obsidian to view it inline

### View Report in Obsidian

The `GRAPH_REPORT.md` can be opened directly in Obsidian for reading.

### Regular Updates

Add to your workflow:
- Run graphify weekly to update your vault's knowledge graph
- Review `GRAPH_REPORT.md` for new connections and insights
- Use `graphify query` to ask questions about your research

## Configuration

### .graphifyignore

Edit `.graphifyignore` to exclude specific folders/files from analysis.
Current exclusions:
- `.obsidian/` - System files
- `Attachments/` - Media files
- `graphify-out/` - Previous outputs
- `copilot/` - AI chat history

### Claude Code Integration

Graphify can integrate with Claude Code via the `/graphify` command:
```bash
graphify install --platform claude
```

## Tips

1. **First run is slow** - Graphify analyzes all files and builds the graph
2. **Subsequent runs are fast** - Only changed files are re-analyzed (cached)
3. **Focus on folders** - Analyze specific research areas instead of the whole vault
4. **Review reports** - `GRAPH_REPORT.md` often reveals connections you missed

## Troubleshooting

If you get permission errors:
```bash
chmod +x graphify-vault.sh
```

To clear cache and re-analyze everything:
```bash
rm -rf graphify-out/cache/
graphify . --output graphify-out/
```

---

**Note:** Graphify was developed by Safi Shamsi. See the full documentation at:
https://github.com/safishamsi/graphify
