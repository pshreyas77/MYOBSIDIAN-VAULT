# INTELLIGENCE Layer — CLAUDE.md

## Purpose
This folder is where Claude deposits outputs that exist nowhere else in the vault.
Connection reports. Topic syntheses. Pattern detections. These are the products of
Claude reading _across_ notes and finding what individual notes cannot see alone.

## Subfolders

### connection-reports/
Weekly connection analyses. Generated every Sunday.
Naming: `YYYY-MM-DD-connections.md`
Format: Each connection names both notes, describes specifically how they connect,
and explains what reading them together reveals that neither reveals alone.
Standard: Only "strong" connections — two notes that illuminate each other.
Weak connections (same topic, no dialogue) are skipped.

### syntheses/
Topic-level syntheses when a topic accumulates 10+ permanent notes.
Naming: `YYYY-MM-DD-[topic-name].md`
Format: Central claim, key tension, most influential note, answered open question,
new question raised. Must say something no individual note says — otherwise it's
a summary, not a synthesis.

### patterns/
Monthly pattern detections across permanent notes from different domains.
Naming: `YYYY-MM-DD-patterns.md`
Format: Each pattern is named explicitly, cited with specific notes, explained for
what it reveals that no individual note shows, with one suggested implication.
A pattern is structural — not a shared topic but the same dynamic appearing
in different contexts.

## When to Generate

| Report | Trigger |
|--------|---------|
| connection-reports | Every Sunday |
| syntheses | When a topic has 10+ notes |
| patterns | Monthly |

## Quality Bar
- connection-reports: non-obvious > obvious. If the connection is immediately
  apparent, dig deeper until it's not.
- syntheses: if it only summarizes existing notes, it's not done. Must add insight.
- patterns: structural similarity across domains, not topic overlap.

## Log all outputs
Every report generated: append to `log.md` with date, type, and topic.