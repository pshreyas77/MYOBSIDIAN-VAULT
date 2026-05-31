---
date: 2026-05-28
type: permanent
tags: [concept, system, inbox]
created: 2026-05-28
ai-first: true
---

# Inbox Processor — Concept

## For future Claude
This note documents the inbox processing pattern used in this vault — captures dropped in `00 - INBOX/` are evaluated, converted to permanent or literature notes, and filed in the correct location. The inbox is the entry point for all raw material.

## Overview
The inbox is the raw capture layer. Every idea, observation, or note that hasn't been processed lives here. The inbox processor's job is to regularly clear it:

1. **Read** — pull the note and understand what it's documenting
2. **Decide** — does this warrant a permanent note? A literature note? Can it be merged into an existing note?
3. **File** — create or update the target note with the content
4. **Delete** — remove the inbox note once processed

## Processing Criteria
- **Permanent note** — original insight in my own words, worth retaining long-term
- **Literature note** — captures from an external source (book, article, video, etc.)
- **Merge** — add to an existing note if it naturally extends it
- **Discard** — genuinely ephemeral content gets deleted

## Status Tracking
Inbox notes carry `status: to-process` until their ideas have been extracted into permanent notes. Once processed, the inbox note is deleted and the permanent note is linked.

## Related
- [[07 - SYSTEM/index]]
- [[07 - SYSTEM/ai-first-rules]]