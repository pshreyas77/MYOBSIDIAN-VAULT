---
date: 2026-08-13
type: literature
subtype: article
source: https://andhbhakt.org/schemes
author: AndhBhakt.org (civic transparency platform)
status: to-process
ai-first: true
tags: [literature, article, civic-tech, transparency, india, governance, pib, cag]
---

## For future Claude
This is an article (structured dataset) extracted from andhbhakt.org on 2026-08-13. It catalogs 57 central government schemes launched during the BJP era (2014–present), cross-referencing official PIB claims against independent CAG audit findings. Severity rated Critical / Major / Minor / Unaudited based on the gap between political claims and audit reality.

## Source
https://andhbhakt.org/schemes

## Summary
AndhBhakt.org is a civic transparency platform that compares Press Information Bureau (PIB) claims against Comptroller and Auditor General (CAG) findings for major central schemes. This dataset captures all 57 tracked schemes with structured fields: ministry, year launched, PIB claim count, CAG finding count, predecessor scheme, and severity rating.

**Severity methodology (from source):**
- **Critical** — Major fund diversions, fraudulent claims, or complete scheme failure (gap > 50%)
- **Major** — Significant delays, partial fund diversion, misleading claims (25–50% gap)
- **Minor** — Process issues, documentation gaps (gap < 25%)
- **Unaudited** — PIB claims exist but no CAG audit yet (scheme too new or pending)

**Counts (per source):**
- Total tracked: 57 schemes
- Critical: 16
- Major: 24
- Unaudited: 15

**Top schemes by PIB claim count (per source):**
1. PM Kisan Samman Nidhi — 25 PIB / 6 CAG (Critical, Agriculture, 2018)
2. Swachh Bharat Mission (Urban) — 23 PIB / 16 CAG (Critical, Housing, 2014)
3. PMAY Urban — 19 PIB / 5 CAG (Critical, Housing, 2015)
4. PM Ujjwala Yojana — 17 PIB / 2 CAG (Critical, Petroleum, 2016)
5. Jal Jeevan Mission — 17 PIB / 6 CAG (Critical, Jal Shakti, 2019)

**Top schemes by CAG findings count (per source):**
1. Swachh Bharat Mission (Urban) — 16 CAG / 23 PIB
2. Saubhagya — 9 CAG / 12 PIB (Critical, Power, 2017)
3. Jal Jeevan Mission — 6 CAG / 17 PIB
4. PM Kisan Samman Nidhi — 6 CAG / 25 PIB
5. PM Kaushal Vikas Yojana — 6 CAG / 17 PIB (Major, Skill Dev, 2015)

## Key Claims
- 57 central schemes tracked across 3 Lok Sabha terms (2014→2026) (as of 2026-08, stated on source)
- Severity classification based on gap between PIB and CAG, not absolute failure (as of 2026-08, stated on source)
- Unaudited schemes skew newer (Startup India 2016, Stand Up India 2016) — audit pipeline lags (as of 2026-08, stated on source)
- Housing & Urban Affairs ministry has highest scheme count (5+) (as of 2026-08, stated on source)

## For Refinery
- Extract atoms on PIB vs CAG methodology (gap-based scoring, not absolute failure)
- Extract atoms on top-scoring schemes (Swachh Bharat Urban, PM Kisan, Saubhagya)
- Extract atom on transparency-platform design pattern (severity tiers, unaudited category)
- Skip ministry breakdown — too fine-grained for permanent notes
- Note: raw dataset is truncated (15+ schemes marked "[see full text]") — full text was extracted to `/tmp/andhbhakt_schemes_full.txt` per source note
