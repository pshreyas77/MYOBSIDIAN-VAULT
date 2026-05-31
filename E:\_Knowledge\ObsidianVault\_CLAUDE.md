# Obsidian Vault Configuration - Windows Setup
# Calibrated to actual folder structure: 04 - DAILY, wiki/analyses/meta/summaries, fleeting, inbox, etc.

## 📁 Folder Map & Purpose
- `04 - DAILY/` — Daily notes (YYYY-MM-DD.md)
- `03 - PROJECTS/` — Active projects and project notes
- `wiki/` — Evergreen knowledge base (internally linked)
  - `wiki/entities/` — People, companies, tools, organizations
  - `wiki/concepts/` — Ideas, frameworks, theories, mental models
  - `wiki/analyses/` — Analytical notes and insights
    - `wiki/analyses/meta/` — Meta-analysis about the vault itself
    - `wiki/analyses/meta/summaries/` — Summary notes and digests
  - `wiki/sources/` — Source summaries and literature notes
  - `wiki/comparisons/` — Versus and comparison analyses
- `fleeting/` — Temporary, in-process notes (auto-cleaned periodically)
- `inbox/` — Raw input before processing (to be reviewed and filed)
- `00 - SYSTEM/` — System files, templates, metadata
  - `00 - SYSTEM/Templates/` — Note templates
  - `00 - SYSTEM/MOCs/` — Maps of Content
- `Knowledge/` — Ingested long-form content (articles, transcripts, PDFs)
- `logs/` — Automation logs (nightly consolidation, etc.)

## 📄 Core Files
- `log.md` — Append-only log of every vault operation (automated)
- `index.md` — Catalog of all vault pages by category (auto-updated)
- `_CLAUDE.md` — This file (operating manual, persisted across sessions)

## 🏷️ Naming Conventions
- **Dated notes**: `YYYY-MM-DD — Title.md` (used in 04 - DAILY/, fleeting/, inbox/)
- **Evergreen notes**: `Title.md` (used in wiki/, Knowledge/, 03 - PROJECTS/)
- **Separators**: Use ` — ` (em dash) consistently
- **Filename safety**: Only alphanumerics, spaces, hyphens, and em dashes
- **No special characters**: Avoid : ? * " < > | in filenames

## 📋 Frontmatter Standards
All notes require YAML frontmatter at minimum:
```yaml
---
date: 2026-05-31
tags: [<note-type>]
---
```

**Note-type tags by folder**:
- `04 - DAILY/` → `daily`
- `03 - PROJECTS/` → `project`  
- `wiki/entities/` → `entity`
- `wiki/concepts/` → `concept`
- `wiki/analyses/` → `analysis`
- `wiki/sources/` → `source`
- `Knowledge/` → `knowledge`
- `fleeting/` → `fleeting`
- `inbox/` → `inbox`

## 🔄 Status Values (when applicable)
- **Projects**: `active` / `planning` / `completed` / `archived` / `on-hold`
- **Tasks** (in notes): `in-progress` / `done` / `waiting` / `cancelled`

## 🗂️ Kanban Board Format
If using kanban boards (in `03 - PROJECTS/` or `00 - SYSTEM/`):
- **Columns**: 
  - `## 📥 Backlog`
  - `## 🔨 In Progress` 
  - `## 📋 This Week` (≤7 days)
  - `## ✅ Done`
- **Card format**: 
  ```markdown
  - [ ] 🔴 **Title** · @{YYYY-MM-DD}
      Description [[Related Note]]
  ```
- **Completed**: `- [x] ~~**Title**~~ ✅ YYYY-MM-DD`

## 💾 Auto-Save Behavior (Obsidian Second Brain)
The system automatically saves conversation insights when it detects:
- ✅ **Decisions made** → Append to relevant project's `## Key Decisions`
- ✅ **People mentioned** → Create/update in `wiki/entities/` or `People/`
- ✅ **Tasks identified** → Add to kanban (`📋 This Week` if due ≤7 days, else `📥 Backlog`)
- ✅ **Projects started** → Create/update in `03 - PROJECTS/`
- ✅ **Learnings captured** → Save to `Knowledge/` or `wiki/concepts/`
- ✅ **Ideas generated** → Save to `fleeting/` or `inbox/` for review, then `wiki/concepts/`

**Never ask where to save** — infer from context. Only ask if genuinely ambiguous (e.g., unnamed person with no context).

## 🔗 Linking Rules
- **Always use**: `[[Note Name]]` for internal links
- **Link generously**: People, projects, jobs, tools, key concepts
- **External links**: Use standard Markdown `[Text](URL)`
- **Block references**: `^block-id` for specific paragraphs
- **File embeds**: `![[Note Name]]` for transclusion

## 🧰 Special Handling by Note Type
### People Notes (`wiki/entities/` or `People/`)
- Frontmatter: `date`, `tags: [entity]`, plus optional `role`, `company`, `location`
- **Timeline**: Use `timeline:` array for historical positions (never overwrite)
- **Interaction log**: Link from daily notes when met/contacted

### Project Notes (`03 - PROJECTS/`)
- Frontmatter: `date`, `tags: [project]`, `status: active`, optional `goal`, `deadline`
- **Key Decisions**: `## Key Decisions` section with dated entries
- **Recent Activity**: Link from dev logs and daily notes
- **Kanban**: Add card to appropriate column

### Concept Notes (`wiki/concepts/`)
- Frontmatter: `date`, `tags: [concept]`, optional `status: active/superseded`
- **Structure**: Summary → Details → Examples → Sources → Related
- **Updates**: Rewrite with new context (don't just append); preserve evolution

### Daily Notes (`04 - DAILY/`)
- **Sections**: 
  - `## ⚡ Focus Today` (pulled from overdue/today-due tasks)
  - `## 📥 Inbox / Captures` (processed items from inbox/)
  - `## 🧠 AI Conversations` (links to saved conversations)
  - `## 📊 Progress` (task/checklist tracking)
  - `## 🔍 Observations` (fleeting thoughts)
  - `## 🔗 Linked Notes` (manually related)
  - `## 📚 Today's Learnings` (auto-populated from consolidation)
  - `## End of Day` (added nightly: 3-5 bullet summary)

### Fleeting & Inbox (`fleeting/` and `inbox/`)
- **Processing rule**: Review daily; file, archive, or delete within 48 hours
- **Fleeting**: Working notes, drafts, half-formed ideas
- **Inbox**: Raw input requiring triage (voice memos, quick captures, forwarded items)

## 📈 Maintenance & Housekeeping
### Daily (Manual or Automated)
- Process `inbox/` → file to appropriate locations
- Review `fleeting/` → promote to evergreen or delete
- Complete end-of-day reflection in daily note

### Nightly (Automated via Obsidian Nightly Consolidation)
At 22:00 daily, runs this 5-phase process:
1. **Close the day**: Read today's daily note → append `## End of Day` (3-5 bullet summary)
2. **Reconcile**: 
   - Scan `wiki/entities/` for outdated roles/companies conflicting with recent notes
   - Scan `wiki/concepts/` for claims contradicted by recently ingested sources
   - Auto-resolve clear winners; flag ambiguities in `wiki/decisions/`
3. **Synthesize**: 
   - Scan sources from last 2 days → find concepts in 2+ unrelated sources
   - If found → create `wiki/concepts/Synthesis — Title.md` with evidence + interpretation
4. **Heal**: 
   - Find notes created today with 0 incoming links → add links from relevant existing pages
   - Check entity pages for old timeline entries missing "until" dates → close them
   - Rebuild `index.md` to reflect all changes
5. **Log**: Append to `log.md`: `## [YYYY-MM-DD] nightly | End of day + X reconciled, Y synthesized, Z orphans linked`

## 🛠️ Skills Configuration
- **Obsidian Second Brain**: Primary automation skill (this setup)
- **graphify**: Knowledge graph visualization (`/graphify` command)
- **mempalace**: Local AI memory system (`/mempalace` commands)
- **Custom scripts**: obsidian-nightly.ps1 (runs nightly consolidation via Task Scheduler)

## 🕐 Scheduled Automation (Windows Task Scheduler)
- **ObsidianNightly**: Daily at 22:00 → Runs the 5-phase consolidation pass above
  - Action: `powershell -ExecutionPolicy Bypass -File "E:\_Knowledge\ObsidianVault\obsidian-nightly.ps1"`
  - Task State: Ready