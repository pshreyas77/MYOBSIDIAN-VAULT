# Graph Presets — Hotkey-Driven (No Plugin Needed)

Since Graph Presets plugin was removed, use these **Command Palette** workflows or **hotkeys** to switch graph views instantly.

---

## Preset 1: Global Overview (Default)
**Graph Settings**:
- Color Groups: **ON** (23 groups from `graph.json`)
- Show Tags: **ON**
- Show Attachments: **OFF**
- Hide Unresolved: **ON**
- Show Orphans: **OFF**
- Collapse Color Groups: **OFF**
- Physics: Center 0.6, Repel 15, Link 0.8, Distance 180
- Arrows: **ON**

**Hotkey**: `Ctrl+G` → already configured

---

## Preset 2: Local Graph (Current Note)
**Action**: Click graph icon in note toolbar (or `Ctrl+Shift+G`)
**Settings**: Inherits global but scoped to current note's neighborhood
**Use for**: Exploring connections from active note

---

## Preset 3: Tag Exploration
**Search Query**: `tag:#ai` (or `#dravidian`, `#moc`, `#index`, `#ancient-civilization`)
**Color Groups**: ON (tags have their own colors)
**Use for**: Seeing all AI notes, all Dravidian notes, all MOCs clustered

---

## Preset 4: Folder Deep-Dive
**Search Query**: `path:/02 - AREAS/03 Ancient Civilizations`
**Color Groups**: OFF (single folder = single color)
**Use for**: Focused view of one area

---

## Preset 5: Orphan Hunt (Cleanup)
**Settings**:
- Show Orphans: **ON**
- Hide Unresolved: **OFF**
- Color Groups: **OFF**
- Search: (empty)
**Use for**: Finding unlinked notes to connect or delete

---

## Preset 6: MOC / Index Map
**Search Query**: `tag:#moc OR tag:#index`
**Color Groups**: ON (MOC = white, Index = light gray)
**Physics**: Higher repel (20), lower link strength (0.5)
**Use for**: Navigation map of your knowledge structure

---

## Preset 7: Daily/Journal Timeline
**Search Query**: `path:/04 - DAILY`
**Color Groups**: OFF
**Physics**: Linear layout — Center 0.2, Repel 5, Link Distance 300
**Use for**: Temporal view of daily notes

---

## Preset 8: Project Radar
**Search Query**: `path:/03 - PROJECTS/Active`
**Color Groups**: ON (Active=amber, Completed=lime, People=indigo, Questions=teal)
**Use for**: Active project landscape

---

## Quick-Switch Workflow

1. **Open Graph**: `Ctrl+G`
2. **Type Search**: Click search box → paste query (e.g., `tag:#ai`)
3. **Toggle Settings**: Right sidebar → Display → toggle Color Groups, Tags, Orphans
4. **Save as Workspace**: `Ctrl+P` → "Workspaces: Save current workspace" → name it "Graph: AI Cluster"
5. **Load Workspace**: `Ctrl+P` → "Workspaces: Open workspace" → pick saved graph view

**Pro tip**: Create 3-4 workspaces for your most-used graph views:
- `Graph: Global` (default)
- `Graph: MOC Map` (`tag:#moc OR tag:#index`)
- `Graph: Orphans` (Show Orphans ON)
- `Graph: Active Projects` (`path:/03 - PROJECTS/Active`)

---

## Hotkey Suggestions (Settings → Hotkeys)

| Action | Suggested Key |
|--------|---------------|
| Open Global Graph | `Ctrl+G` (default) |
| Open Local Graph | `Ctrl+Shift+G` (default) |
| Focus Graph Search | `Ctrl+Shift+F` (in graph view) |
| Toggle Color Groups | *Custom* — assign via "Graph View: Toggle color groups" |
| Toggle Orphans | *Custom* — assign via "Graph View: Toggle show orphans" |
| Toggle Tags | *Custom* — assign via "Graph View: Toggle show tags" |

---

## Graph.json Backup Locations

| File | Purpose |
|------|---------|
| `.obsidian/graph.json` | Active config (auto-saved by Obsidian) |
| `.obsidian/graph.json.backup.permanent` | Your curated 23-group config — **source of truth** |
| `.obsidian/graph-color-config.md` | Human-readable documentation |
| `.obsidian/restore-graph-colors.sh` | One-command restore script |

**If colors vanish**: Run `bash .obsidian/restore-graph-colors.sh` then reload Obsidian (`Ctrl+R`).