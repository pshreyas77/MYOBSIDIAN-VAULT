# Your 2nd Brain — Wiki Home

**Integrated System:** claude-obsidian + mempalace + obsidian-vault  
**Last Updated:** 2024-04-17  
**Total Indexed:** 21,228 drawers (mempalace)

---

## 📁 Wiki Structure

```
wiki/
├── entities/           # People, places, organizations (tag: #entity)
│   ├── Buddha.md
│   ├── Socrates.md
│   └── ...
├── concepts/           # Ideas, theories, doctrines (tag: #concept)  
│   ├── Nirvana.md
│   └── ...
├── sources/           # Documents, books, references (tag: #source)
├── meta/
│   └── hot.md         # Session persistence cache
├── _templates/
│   ├── entity.md      # Template for entity pages
│   └── concept.md     # Template for concept pages
└── WIKI_HOME.md       # This file
```

---

## 🎨 Graph View Colors

| Query | Color | Meaning |
|-------|-------|---------|
| `path:wiki/entities` | 🟠 Orange | People, Places, Organizations |
| `path:wiki/concepts` | 🔵 Blue | Ideas, Doctrines, Theories |
| `path:wiki/sources` | 🟢 Green | Documents, Books, References |
| `path:wiki/meta` | ⚫ Gray | System/Meta files |
| `path:ClaudeVault` | 🔷 Teal | AI Research |
| `path:QwenVault` | 🔷 Light Blue | Quick Research |
| `path:DeepseekVault` | 🟣 Purple | Deep Analysis |
| `path:BUDDHA` | 🟤 Brown | Buddhism Research |

---

## 🚀 Quick Commands

In any Claude session, use these patterns:

### 1. Ask with Context
```
/mempalace wake-up --wing obsidian_vault
"What do I know about [topic]?"
```

### 2. Create Entity Page
Create new file in `wiki/entities/` with:
- Frontmatter with `#entity` tag
- Relations section
- See Also section with `[[links]]`

### 3. Create Concept Page
Create new file in `wiki/concepts/` with:
- Frontmatter with `#concept` tag
- Definition section
- Contradiction callouts (!)
- See Also section

### 4. Hot Cache
Check `wiki/meta/hot.md` for session context.

---

## 📊 Current Stats

**Mempalace Index:**
- Total Drawers: 21,228
- Wing: obsidian_vault
- Rooms: 11
- Status: ✅ Active

**Graph View:**
- Color-coded by type
- Arrows show direction
- Filtered to wiki + vault folders

---

## 🔧 Maintenance

**Auto-Linting (run weekly):**
1. Check for orphans (notes with no backlinks)
2. Check for dead links (broken `[[references]]`)
3. Find missing cross-references
4. Update `hot.md` with recent activity

**Manual Tasks:**
- Mine new content: `mempalace mine "/path/to/files" --wing obsidian_vault`
- Search: `mempalace search "query"`
- Status: `mempalace status`

---

## 🎯 Next Steps

1. ✅ Wiki structure created
2. ✅ Hot cache enabled
3. ✅ Graph colors configured
4. ✅ Sample entities (Buddha, Socrates)
5. ✅ Sample concept (Nirvana)
6. 🔄 Ready for: Automatic entity extraction
7. 🔄 Ready for: Contradiction flagging
8. 🔄 Ready for: Batch ingestion

---

## 🤖 Claude Integration

Every session now starts with context from:
1. **Mempalace wake-up** - Recent research
2. **Hot cache** - Session continuity
3. **Wiki pages** - Structured knowledge
4. **Graph view** - Visual connections

**Auto-features enabled:**
- Entity linking
- Concept cross-referencing
- Contradiction flagging
- Source attribution
- Color-coded graph view

---

*This is your self-organizing AI brain. Knowledge compounds like interest.*