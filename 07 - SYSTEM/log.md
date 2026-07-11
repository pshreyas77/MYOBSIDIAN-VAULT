## [2026-07-11] night-shift-rebuild | Night Shift pipeline rebuilt as Hermes cron jobs — 4 durable jobs replacing dead Windows Task Scheduler pipeline

### Pipeline Status (Before)
- Night Shift dead since 2026-06-25 (16 days)
- PowerShell scheduled tasks lost/unreachable
- Only surviving cron: vault-auto-commit (10 PM IST)

### New Hermes Cron Architecture
| Job | Schedule | ID | Status |
|-----|----------|-----|--------|
| Scout Run | 23:30 IST daily | b60bd1a2ba42 | 🟢 Scheduled |
| Refinery Run | 03:00 IST daily | e5fa48dbb046 | 🟢 Scheduled |
| Editor Run | 06:00 IST daily | 8e3ee9ca65d5 | 🟢 Scheduled |
| Audit Run | 22:00 IST Sundays | 5981bc3a96fd | 🟢 Scheduled |

### Manual Run (Immediate)
- Scout: Processed 1 INBOX item — India Urban Flooding Report → quarantined (no sources) to `1-desk/article/2026-07-11 — India Urban Flooding Report (Quarantined — No Sources).md`
- Morning Brief: Generated `BRIEFINGS/2026-07-11 — Morning Brief.md` — vault status, project tracker, action items

### Next Runs
- Scout: Tonight 23:30 IST (2026-07-11)
- Refinery: Tomorrow 03:00 IST (2026-07-12) — will process 4 unprocessed July literature notes
- Editor: Tomorrow 06:00 IST (2026-07-12) — will link extracted atoms + generate morning brief
- Audit: Sunday 22:00 IST (2026-07-12)

### Known Gaps
- 20+ broken wikilinks unresolved (Batman Philosophy Archive, Philosophy Links Tracker, Knowledge Hub, etc.)
- 15+ orphans from Jul 8 analysis unfixed
- History Watchdog overdue (Week 1 deliverable Jul 14 missed)
- Health Dashboard stale since Apr 23 — "Modern Revival and Application" section (6 frameworks) appended to existing note:
  - 02 - PERMANENT/concepts/Justice Party.md (Social Justice/Reservation, Rationalism, Gender Equality, Educational Outreach, Cultural Transformation/Self-Respect, State Autonomy/Federalism + Mass Movement Insight)

## [2026-06-05] obsidian-save | Justice Party Periyar–Ambedkar Enhancement — Periyar's path from Congress (1925), Self-Respect Movement, 1938/1939 Party Presidency from prison, 1944 Salem DK transformation; Ambedkar–Periyar 1954 Rangoon meeting added to existing note

## [2026-06-05] obsidian-save | Justice Party Regional Legacy — "Regional Legacy Across Dravidian States" section appended to existing note:
  - 02 - PERMANENT/concepts/Justice Party.md (Tamil Nadu, Andhra Pradesh, Karnataka, Kerala breakdowns + constitutional legacy)

## [2026-06-05] obsidian-save | Ethno-Religious Nationalism Synthesis — comparative analysis of 5 ideologies saved to vault:
  - 02 - PERMANENT/concepts/Ethno-Religious-Nationalism-Synthesis.md (full comparative analysis)

## [2026-07-09] vault-cleanup | Waste audit + comprehensive fixes executed

### RED (Deleted — zero knowledge loss)
- `graphify-out/obsidian/` — 50+ auto-generated tool descriptor .md files (not user notes)
- `wiki/hot.md` — dead cache file, never populated
- `wiki/sources/Test_Article_for_LLM_Wiki_Ingestion.md` — test artifact
- `wiki/index.md` — 13-line empty skeleton
- `02 - PERMANENT/concepts/Inbox Processor.md` — 2026-05-28 test note
- `wiki/comparisons/How_does_the_LLM_wiki_pattern.md` — auto-gen stub, broken wikilinks
- `wiki/comparisons/What_is_the_LLM_wiki_pattern.md` — same
- Empty wiki folders removed: `comparisons/`, `sources/`, `summaries/`, `decisions/`

### YELLOW (Repositioned — content preserved)
- `wiki/Ancient Civilizations Educational Resources.md` → `01 - LITERATURE/articles/2026-05-24 — ...`
- `04 - DAILY/TS-EAMCET-Shortlist-Workflow.md` → `03 - PROJECTS/TS-EAMCET-Shortlist-Workflow.md`

### GREEN (Cleaned)
- `log.md` (root, Night Shift logs) renamed → `night-shift-log.md`
- `CRITICAL_FACTS.md` — removed `[fill in]` placeholders, synced with IDENTITY.md
- `index.md` (root) — 308-line stale index replaced with thin redirect to `07 - SYSTEM/index.md`
- `07 - SYSTEM/index.md` — updated references: removed `BUDDHA/`, `graphify-out/`; added `IDENTITY.md`, `Hermes-Skill-Integration-Analysis.md`, `night-shift-log.md`

### NEW
- **Contrarian Loop concept saved:** `02 - PERMANENT/concepts/Contrarian Loop — Vault That Argues With Itself.md`
- Linked into `05 - MAPS/Agentic Systems MOC.md` and `05 - MAPS/Digital Garden MOC.md`

### NEW
- **LLM Wiki Full Synthesis saved:** `01 - LITERATURE/articles/2026-07-09 — LLM Wiki Pattern — Full Synthesis.md`
- Cross-linked from `01 - LITERATURE/2026-07-08 — LLM Wiki Pattern — Karpathy.md`

Net result: ~65 waste files removed, 4 empty folders removed, 4 orphaned notes repositioned, 2 indexes cleaned, 2 new permanent/literature notes added.

## [2026-06-05] obsidian-save | Ethno-Religious Nationalism + Secularism — Relationship with Secularism section added to existing note

## [2026-06-05] obsidian-save | Ethno-Religious Nationalism Counter-Strategies — "Countering Ethno-Religious Nationalist Groups" section (5 frameworks) appended to existing synthesis note

## [2026-06-02] obsidian-save | Caveman political analysis — BJP political geography + South India saved to vault — 8 notes created/linked:
  - Research/2026-06-02 — BJP Political Geography & South India Analysis.md (main briefing)
  - 02 - PERMANENT/people/K. Annamalai.md
  - 02 - PERMANENT/people/Vijay.md
  - 02 - PERMANENT/people/Rajeev Chandrasekhar.md
  - 02 - PERMANENT/people/E. Sreedharan.md
  - 02 - PERMANENT/concepts/Liberal in Indian Political Context.md
  - 02 - PERMANENT/concepts/BJP Dominance Map — Indian States.md
  - 06 - OUTPUTS/analyses/Caveman Analysis — TVK vs BJP Tamil Nadu.md

## [2026-05-29] vault-propagate | Research on Justice Party (1916–1944) and Non-Brahmin Movement saved to vault — 7 new/updated notes created:
  - 01 - LITERATURE/articles/2026-05-29 — Justice Party & Non-Brahmin Movement Research Synthesis.md (200+ line research synthesis)
  - 02 - PERMANENT/concepts/Justice Party.md (core distillation)
  - 02 - PERMANENT/concepts/Dravidar Kazhagam.md (core distillation)
  - 02 - PERMANENT/people/T. M. Nair.md
  - 02 - PERMANENT/people/P. Theagaraya Chetty.md
  - 02 - PERMANENT/people/C. Natesa Mudaliar.md
  - wiki/entities/Periyar E. V. Ramasamy.md (updated: 1938–1944 Justice Party leadership added)
  - wiki/concepts/Indian Atheism, Rationalism, and Anti-Caste Struggle.md (updated: Justice Party + Dravidar Kazhagam added to movement timeline)

## [2026-05-28] migrate | Karpathy second brain layer added — 8 new folders created, _CLAUDE.md updated, 0 files moved

## [2026-05-28] vault-init | Non-destructive migration to Karpathy framework — existing notes untouched

## [2026-05-28] inbox-test | Inbox Processor verified — test note processed into [[02 - PERMANENT/concepts/Inbox Processor]], test file deleted