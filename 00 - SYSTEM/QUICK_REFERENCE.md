# Obsidian Graph Analysis Quick Reference

## 🚀 Daily Commands

### Run Full Analysis
```bash
cd "/home/sunny77/Documents/Obsidian Vault"
python3 "00 - SYSTEM/vault_analyzer.py" .understand-anything/knowledge-graph.json .
```

### Quick Health Check
```bash
# Just update reports without full re-analysis (if you have recent data)
python3 "00 - SYSTEM/vault_analyzer.py" .understand-anything/knowledge-graph.json . --update
```

## 📁 File Locations

```
00 - SYSTEM/
├── vault_analyzer.py              # Main analysis script
├── 00_Master_MOC_God_Nodes.md     # Master MOC template
├── DATAVIEW_QUERIES.md            # Ready-to-copy Dataview queries
├── QUICK_REFERENCE.md             # This file
└── Graph Reports/
    ├── 01_god_nodes_dashboard.md
    ├── 02_orphaned_communities.md
    ├── 03_bridge_notes.md
    ├── 04_edge_confidence.md
    └── 05_master_action_plan.md
```

## 🏷️ Tagging Convention

| Tag | Meaning | When to Apply | Color Suggestion |
|-----|---------|---------------|------------------|
| `#god-node` | Top-connected concepts (now(), map(), error(), Task, Values()) | Auto-applied by analyzer or manual for similar concepts | 🔴 Red |
| `#bridge-note` | Connects technical ↔ non-technical domains | Notes with connections to both code and philosophy/politics/religion | 🟡 Yellow |
| `#orphan` | Very low connectivity (<5 connections) | Notes needing review, merging, or deletion | ⚫ Black |
| `#weak-link` | Inferred edge with low confidence (<0.6) | Individual links to review and strengthen | 🟠 Orange |
| `#review-monthly` | Needs monthly attention | Communities or concepts requiring regular review | 🔵 Blue |

## 📊 Key Metrics to Track

Update these in your MOC monthly:

- **God Node Count**: Notes with >1000 connections (target: maintain 5-8)
- **Bridge Note Ratio**: % of notes that connect domains (target: 15%+)
- **Orphan Reduction**: Notes with <5 connections (target: <5% of total)
- **Extracted Edge %**: Explicit wikilinks vs inferred (target: 70%+)
- **Community Health**: Avg connections per community (target: >20)

## 🔄 Maintenance Schedule

| Frequency | Action | Tool/Method |
|-----------|--------|-------------|
| **Daily** | Quick capture & linking | Obsidian daily note + wikilinks |
| **Weekly** (Fri AM) | Run full analysis + update reports | `vault_analyzer.py` |
| **Weekly** (Fri PM) | Review `#orphan` notes | Dataview orphan query |
| **Weekly** (Wed) | Strengthen 5 weak links | Dataview weak-link query |
| **Monthly** (1st Sun) | Community review & merging | Analyze communities report |
| **Monthly** | Update PARA+ folder mappings | Based on connection analysis |
| **Quarterly** | Full vault retrospective | Review action plan progress |

## 💡 Pro Tips

### Finding Hidden Connections
1. **Search for implied relationships**: Look for notes that mention God Node concepts without linking
   - Search: `now()` `map()` `error()` (without `[[` brackets)
   - Add missing links: Convert `now()` → `[[now()]]`

2. **Bridge building**: For each technical note, ask:
   - "What philosophical principle underlies this?"
   - "What political/social implication does this have?"
   - "How does this relate to my religious/spiritual studies?"

### Strengthening Weak Links
When you see a weak inferred link (confidence < 0.6):
1. **Verify**: Does the connection make sense?
2. **Evidence**: Add a sentence or two explaining WHY they're connected
3. **Explicit link**: Add `[[wikilink]]` in both directions
4. **Tag**: Consider `#weak-link` until confidence improves

### Working with the Task God Node
Since `Task` is a conceptual bridge:
- Keep a central `Tasks` note in `02 - AREAS/05 Knowledge Management`
- Use it as a hub connecting:
  - Technical: Async patterns, promises, workflow automation
  - Philosophical: Ethics of productivity, value of work
  - Practical: Project planning, GTD, habit systems
- Tag all task-related notes with `#task-system`

## 🛠️ Troubleshooting

### "Knowledge graph not found"
- Run Understand-Anything first: `cd .understand-anything && python3 -m understand_anything_plugin`
- Or point to correct path: `python3 vault_analyzer.py /full/path/to/knowledge-graph.json .`

### "Reports not updating"
- Check you're running from vault root: `/home/sunny77/Documents/Obsidian Vault`
- Ensure `.understand-anything/knowledge-graph.json` exists and is valid JSON
- Try with `--update` flag for incremental updates

### "Dataview queries not working"
- Ensure Dataview plugin is installed and enabled
- Some queries require Dataview JS API version (check plugin version)
- Simplify complex queries if needed

### "Too many orphans"
- Normal during active learning phases
- Focus on reducing orphans by 10-20% per week rather than elimination
- Archive truly obsolete notes to `09 - ARCHIVES` instead of deleting

## 🎯 Success Indicators

You know the system is working when:

1. **You discover unexpected connections** while following links in your vault
2. **Creating new notes feels faster** because you see relevant existing connections
3. **Your PARA+ folders show clear thematic clustering** in community analysis
4. **The Task node becomes your daily dashboard** for bridging ideas to action
5. **You spend less time searching** and more time creating/connecting

---

*Last updated: {{datetime.now().strftime('%Y-%m-%d')}}*  
*Keep this file in your 00 - SYSTEM folder for easy reference*