---
date: 2026-07-11
type: permanent
tags: [concept, karpathy-method, second-brain, llm-wiki, gap-analysis]
ai-first: true
source: "Karpathy LLM Wiki method (viral post Apr 2026) + existing vault architecture"
related: ["01 - LITERATURE/2026-07-08 — LLM Wiki Pattern — Karpathy", "01 - LITERATURE/articles/2026-07-09 — LLM Wiki Pattern — Full Synthesis", "InfiniteBrain", "07 - SYSTEM/index"]
---

# Karpathy Method — Gap Analysis Against Our Vault

## For future Claude
This note maps the Karpathy LLM Wiki method (the viral "second brain that compounds" approach) against what our vault already has. The conclusion: we're 90%+ ahead of the article's recommendations, with a richer architecture. The one real gap is INGEST as a unified trigger command — and even that is functionally covered by our Scout → Refinery pipeline.

---

## Structure Comparison

| Karpathy's Setup | Our Equivalent | Status |
|------------------|----------------|--------|
| `/raw` — unprocessed sources | `00 INBOX/` + `0-raw/` | ✅ Ahead (two-stage intake with quarantine) |
| `/wiki` — AI-processed atomic pages | `wiki/` (entities + concepts) + `02 - PERMANENT/` + `2-atoms/` | ✅ Ahead (three-tier atomic system) |
| `index.md` — page catalog | `07 - SYSTEM/index.md` (canonical) + `index.md` (root redirect) | ✅ Ahead (dual-index with layer structure) |
| `log.md` — ingest chronology | `07 - SYSTEM/log.md` (operations) + `night-shift-log.md` (agent runs) | ✅ Ahead (separate human + agent logs) |
| `CLAUDE.md` — schema/rules | `_CLAUDE.md` (280 lines, operating manual) + `07 - SYSTEM/ai-first-rules.md` (note spec) + `house-rules.md` (Prime Directive + Night Shift constitution) | ✅ Ahead (three-tier rule architecture) |

---

## Operations Comparison

### INGEST
**Karpathy:** "ingest this" → AI reads source, extracts atoms, links to wiki, updates index/log, archives source.

**Our equivalent:** Scout Run (23:00) classifies raw intake → Refinery Run (03:00) extracts atoms → Editor Run (06:00) links atoms + updates index + generates brief. **Four-stage pipeline, not one command.** Additional: Prime Directive gate (no source = quarantine), [FRICTION] detection, confidence markers.

**Gap:** We don't have a unified "ingest this" trigger phrase in CLAUDE.md. The pipeline handles ingestion autonomously on schedule, but there's no single command a human can say to Claude to force-feed a specific source right now. The Scout's playbook covers this functionally — it reads INBOX and processes everything — but a `ingest [URL/file]` shortcut would be useful for immediate feeds.

**Verdict:** ⚠️ Minor gap — pipeline is richer but lacks an ad-hoc ingest trigger.

### QUERY
**Karpathy:** "what do I know about X?" → AI searches wiki, cites pages, surfaces conflicts, files answer as new page.

**Our equivalent:** `_CLAUDE.md` section "The 6 Claude Integrations" — #3 Question Answerer ("search vault first before external knowledge") + #6 Synthesis Generator ("produces output that only emerges from reading all of them together"). Plus 4 MOCs (05 - MAPS/) that pre-compile answers for major domains.

**Verdict:** ✅ Covered — MOCs make query answers faster than ad-hoc search.

### LINT
**Karpathy:** "lint the wiki" → find contradictions, outdated claims, orphans, gaps. Report everything, don't auto-delete.

**Our equivalent:** Audit Run (Sun 22:00) — full health scan: duplicates, orphans, broken links, missing frontmatter, stale claims (6+ months), quality sampling (spot-check 10-15 atoms), weekly synthesis. **Automated weekly, not manual.** Plus [FRICTION] detection runs daily in Editor Run. Plus Prime Directive enforcement (unsourced notes → quarantined).

**Gap:** Karpathy's "lint" is manual — you say it, Claude runs it. Ours is automated cron. The **trigger phrase** is missing from CLAUDE.md, but the operation runs autonomously every Sunday. If you wanted to run it NOW, you'd have to describe the operation rather than say a memorized command.

**Verdict:** ⚠️ Minor gap — operation exists (richer, automated), but trigger phrase missing from schema.

---

## What We Have That Karpathy Doesn't

| Feature | Karpathy Method | Our Vault |
|---------|-----------------|-----------|
| **Maps of Content (MOCs)** | Not mentioned | 6 MOCs: Philosophy & Religion, Indian Political History, AI & Tech, Health & Fitness, Digital Garden, Agentic Systems |
| **Prime Directive** (no source = no note) | Not mentioned | `house-rules.md` — enforced at Scout gate. Unsourced items → quarantined. |
| **[FRICTION] system** (contradiction flagging) | "find contradictions" manually | Automated daily in Editor Run. Structured [FRICTION] blocks with resolution templates. |
| **Confidence markers** | Not mentioned | `stated | high | medium | speculation` on every claim |
| **Recency markers** | Not mentioned | "(as of YYYY-MM, source.com)" required on time-sensitive claims |
| **Cross-domain synthesis** | Not mentioned | Jul 8 session: 4 MOCs analyzed → 8 cross-domain project ideas generated |
| **Graph visualization** | Not mentioned | `graphify-repo/` — interactive knowledge graphs, community detection, god node identification |
| **Smart Connections** (.smart-env/) | Not mentioned | Semantic embedding layer running in background — finds conceptual links beyond exact wikilinks |
| **24/7 automation** | Article recommends VPS + cron | ✅ Already built — 4 Hermes cron jobs (Scout 23:30, Refinery 03:00, Editor 06:00, Audit Sun 22:00) running continuously |
| **Morning Brief pipeline** | Not mentioned | Auto-generated daily briefings in `BRIEFINGS/` summarizing Scout + Refinery + Editor output |
| **Project hubs** | Not mentioned | 8 active projects catalogued in `03 - PROJECTS/` with specs, stacks, roadmaps |
| **8-layer Karpathy structure** | 3 folders (/raw, /wiki, root files) | 8 layers (00 INBOX → 07 SYSTEM) + legacy PARA aliases + topic folders + tooling spaces |

---

## The One Gap Worth Closing

The article's model has simplicity: three trigger phrases (`ingest this`, `query X`, `lint the wiki`) that a human says and Claude executes immediately. Our equivalent operations exist and are richer — but spread across 4 cron jobs, 3 rule files, and 5 playbooks. 

**Recommendation:** Add a "Quick Commands" section to `_CLAUDE.md` mapping Karpathy-style triggers to our richer equivalents:

```
When I say "ingest [source]":
→ Drop it in 00 - INBOX/, then run Scout + Refinery + Editor manually.
  Or: wait for tonight's Scout Run (23:30 IST) to pick it up automatically.

When I say "query [topic]":
→ Read the relevant MOC in 05 - MAPS/ first (pre-compiled answer).
  Then search wiki/, 02 - PERMANENT/, and Research/.
  Cite every note. File synthesis as new output in 06 - OUTPUTS/.

When I say "lint the wiki":
→ Execute Audit Run immediately (same protocol as Sunday cron).
  Report: contradictions, stale claims, orphans, broken links, gaps.
  Never delete — flag for my review.
```

This preserves our richer architecture while adding the convenience triggers Karpathy's method relies on.

---

## Bottom Line

We didn't need to build Karpathy's method from scratch. We already had a superset of it — running autonomously, with richer quality gates, deeper structure, and more automation. The article's value for us is the **trigger-phrase simplicity** — three memorizable commands that bridge the gap between "the system runs on schedule" and "I can force it right now."

**Confidence:** high (verified against both Karpathy's gist and our vault structure as of 2026-07-11)