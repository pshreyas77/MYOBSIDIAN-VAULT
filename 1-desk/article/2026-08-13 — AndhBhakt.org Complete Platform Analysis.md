---
date: 2026-08-13
type: literature
subtype: article
source: https://andhbhakt.org/
author: AndhBhakt.org (civic transparency platform)
status: to-process
ai-first: true
tags: [literature, article, civic-tech, transparency, india, governance, accountability, civic-platforms]
---

## For future Claude
This is an article (platform analysis) of andhbhakt.org extracted on 2026-08-13. It documents the platform's architecture, methodology, scoring systems, and the broader civic-tech pattern of comparing official claims against independent audit findings. Companion document to the 57-schemes dataset.

## Source
https://andhbhakt.org/

## Summary
AndhBhakt.org is described as a civic transparency platform that compares official PIB press releases against independent CAG audit findings for schemes launched during the BJP era (2014–present). The platform's tagline is "Public data, publicly accountable."

**Platform sections (per source):**
1. Central Data Dashboard — PM profile, 71 cabinet ministers, accountability ratings (radial visualization)
2. National Indicators — 6 domains scored: Economy 53, Education 61, Employment 46, Health 53, Safety 34 (Critical), Environment 29 (Critical)
3. Central Schemes Tracker — 57 schemes (full dataset)
4. CAG Audit Findings 2025–26 — 44 findings (18 Critical, 25 Major, 1 Minor)
5. BJP Election Promises (2014–2024) — 170 promises across 3 manifestos (33 Implemented, 79 Partial, 9 Not Fulfilled)
6. Term Governance Rating (2014–2026) — Implementation 56, Transparency 36, Accountability 40

**Accountability verdict scale (per source):**
- **On Track** — Score > 75, claims mostly match reality
- **Off Track** — Score 40–75, significant gaps
- **Critical** — Score < 40, severe accountability issues
- **Unaudited** — No CAG audit available yet

**Data sources (all public records, per source):**
- PIB (Press Information Bureau) — government's official claims
- CAG (Comptroller and Auditor General) — independent audit
- ECI Affidavits via ADR/myneta.info — candidate declarations
- NFHS-5, NCRB, MOSPI, ASER 2023 — development indicators

**Strengths noted (per source):**
- Transparent methodology, primary sources only, bilingual (English/Hindi)
- Explicitly non-partisan, structured data, time-series 2014→2026

**Limitations noted (per source):**
- 404 pages on `/cabinet-ministers`, `/cag-findings`, `/promises`
- No API/CSV export — data trapped in UI
- No state-level data (central schemes only)
- Static scores (no historical trend per scheme)

## Key Claims
- Accountability ratings: Transparency 36, Legal Integrity 51, Governance 40 — all "Concerning" (as of 2026-08, stated on source)
- National indicators worst: Safety 34, Environment 29 — both Critical (as of 2026-08, stated on source)
- 170 BJP promises across 2014/2019/2024 manifestos — 33 Implemented, 79 Partial, 9 Not Fulfilled (as of 2026-08, stated on source)
- Term governance rating 2014–2026: Implementation 56 (Moderate), Transparency 36 (Concerning), Accountability 40 (Concerning) (as of 2026-08, stated on source)
- 2024 "Modi Ki Guarantee": 35 promises — 3 Implemented, 27 In Progress, 1 Not Fulfilled (as of 2026-08, stated on source)

## For Refinery
- Extract atom on civic transparency platform design pattern (PIB vs CAG gap scoring)
- Extract atom on accountability verdict scale (On Track / Off Track / Critical / Unaudited)
- Extract atom on election-promise-to-implementation tracking (170 promises, 18% Implemented rate)
- Extract atom on national indicator dashboard pattern (6 domains, radial scoring)
- Related/comparison: [[2026-08-13 — AndhBhakt.org 57 Central Schemes Dataset]] — raw data companion
- Note: source analysis was compiled via Playwright browser automation; cross-reference `/tmp/andhbhakt_schemes_full.txt` for raw 17K-char dataset
