## graphify

This vault has a graphify knowledge graph at graphify-out/.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- For cross-module "how does X relate to Y" questions, prefer `graphify query "<question>"`, `graphify path "<A>" "<B>"`, or `graphify explain "<concept>"` over grep — these traverse the graph's EXTRACTED + INFERRED edges instead of scanning files
- After modifying code files in this session, run `graphify update E:/_Knowledge/ObsidianVault` to keep the graph current (AST-only, no API cost)

## mempalace

MemPalace source lives at `E:/_Dev_Tools/mempalace/`. Entities file at `E:/_Knowledge/ObsidianVault/entities.json`.

Rules:
- Use `mempalace search "<query>"` for finding content in the mined palace
- Before inserting new knowledge into vault notes, check: `mempalace wake-up` prints contextual memory (people/projects relevant to current session)
- New verbatim content → `mempalace mine E:/path/to/new/content` to add to the palace
- Don't run `mempalace init` again on this vault (already initialized — 15 people, 9 projects)
- Palace storage: `E:/_Dev_Tools/mempalace/palace/` (ChromiumDB backend)