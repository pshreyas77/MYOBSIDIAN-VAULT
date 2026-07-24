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

## Dead Community Links Auto-Fix (added 2026-07-24)

### The bug

Every cluster-analysis rerun (`graphify cluster-only`) regenerates a
`## Community Hubs (Navigation)` block in `graphify-out/GRAPH_REPORT.md`
containing ~2,500 wiki-links like `[[_COMMUNITY_Community N|Community N]]`
that point to files **graphify never creates**. In Obsidian, clicking any of
those links opens a blank page.

### The fix

Three pieces, layered for resilience:

#### 1. Post-processor script

`E:/_Dev_Tools/graphify/scripts/fix-community-links.py` rewrites the
dead-link block as Obsidian in-file anchors to the `### Community N - ...`
headings that **are** generated inline elsewhere in the same report.

Idempotent. Atomic write via `os.replace`. Backups at
`GRAPH_REPORT.md.pre-fix-<YYYYMMDDTHHMMSS>` next to the report.

```bash
"C:/Users/shrey/AppData/Local/Programs/Python/Python314/python.exe" \
  E:/_Dev_Tools/graphify/scripts/fix-community-links.py \
  --report E:/_Knowledge/ObsidianVault/graphify-out/GRAPH_REPORT.md
```

#### 2. Wrapper

`E:/_Dev_Tools/graphify/scripts/graphify-with-fix.py` chains the fix after
any graphify invocation. Use it instead of calling `graphify` directly:

```bash
"C:/Users/shrey/AppData/Local/Programs/Python/Python314/python.exe" \
  E:/_Dev_Tools/graphify/scripts/graphify-with-fix.py cluster-only .
```

The wrapper continues to apply the fix even if graphify itself errors out.

#### 3. Cron hook

The `vault-maintenance` cron (job_id `8c79d585c3b5`, runs nightly at 02:00
IST) now invokes the wrapper instead of bare graphify. After this commit,
dead community links **cannot reappear** without manual intervention.

### What used to happen

Up to 2026-07-23, every graphify regen (typically daily via the Night Shift
runs) re-emitted ~2,500 dead links. The previous fix had to be applied
manually after each regen; we missed the Jul-23 regen and the report had
been broken for ~30 hours before this round was applied + automated.

### Status

Confirmed working as of 2026-07-24:
- 2,507 dead `_COMMUNITY_` wiki-links removed
- 1,121 in-file anchors generated
- 1,121 of those resolve to real `### Community N - ...` headings
- 0 unresolvable numbered communities (the 1 unmatched link is a thin
  community graphify deliberately skipped)
- File size: 366 KB -> 354 KB
