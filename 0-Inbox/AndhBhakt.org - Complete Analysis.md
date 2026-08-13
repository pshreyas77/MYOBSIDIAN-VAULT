# AndhBhakt.org — Complete Analysis

**Source:** https://andhbhakt.org/  
**Analyzed:** August 2026  
**Status:** Fully accessible via browser (Cloudflare-protected, requires JS)

---

## 🎯 What Is AndhBhakt.org?

> **Andhbhakt.org is a civic transparency platform that compares official government claims (PIB press releases) against independent audit findings (CAG reports) for major schemes launched during the BJP era (2014–present).**

**Tagline:** *"Public data, publicly accountable."*

**Core Mission:** Track the gap between political promises and ground reality — what the government said versus what auditors actually found.

---

## 📊 Platform Architecture

### Data Sources (All Public Records)
| Source | Purpose |
|--------|---------|
| **PIB (Press Information Bureau)** | Government's official claims — "what the government wants you to know" |
| **CAG (Comptroller and Auditor General)** | Constitutional auditor findings — independent examination of spending/implementation |
| **ECI Affidavits** | Candidate asset/criminal declarations via ADR/myneta.info |
| **NFHS-5, NCRB, MOSPI, ASER 2023** | National development indicators |
| **Wikipedia** | Supplementary reference |

---

## 🏗️ Site Structure & Key Sections

### 1. **Central Data Dashboard** (Homepage)
- **Prime Minister Profile** — Narendra Modi: Education 80, Legal Integrity 100, Asset growth 21% (2019→2024)
- **Cabinet Ministers (71)** — Clickable list with individual scores
- **Accountability Ratings** (Radial visualization):
  - Transparency: 36 → *Concerning*
  - Officials' Legal Integrity: 51 → *Concerning*
  - Governance: 40 → *Concerning*

### 2. **National Indicators** (6 domains, radial scores)
| Domain | Score | Verdict |
|--------|-------|---------|
| Economy | 53 | Concerning |
| Education | 61 | Moderate |
| Employment | 46 | Concerning |
| Health | 53 | Concerning |
| Safety | 34 | **Critical** |
| Environment | 29 | **Critical** |

### 3. **Central Schemes Tracker** — **57 Schemes Tracked** ✅ *Full data captured*
| Severity | Count |
|----------|-------|
| Critical | 16 |
| Major | 24 |
| Minor | ? |
| Unaudited | 15 |

**Top Critical Schemes:**
- PM Kisan Samman Nidhi (25 PIB / 6 CAG)
- Jal Jeevan Mission (17 PIB / 6 CAG)
- Namami Gange (9 PIB / 3 CAG)
- PMAY Urban (19 PIB / 5 CAG)
- PM Ujjwala Yojana (17 PIB / 2 CAG)
- Swachh Bharat Urban (23 PIB / 16 CAG)
- Smart Cities Mission (2 PIB / 5 CAG)
- Saubhagya (12 PIB / 9 CAG)

**Unaudited (PIB claims only, no CAG audit yet):**
- Startup India (15 PIB / 0 CAG)
- Stand Up India (4 PIB / 0 CAG)

### 4. **CAG Audit Findings (2025–26)**
- 44 findings across 2025–26
- 18 Critical, 25 Major, 1 Minor
- Page `/cag-findings` returns 404 — may be integrated in schemes view

### 5. **BJP Election Promises (2014–2024)**
- 170 key promises across 3 manifestos
- 33 Implemented, 79 Partial, 9 Not Fulfilled
- **"Modi Ki Guarantee" (2024):** 35 promises — 3 Implemented, 2 Partial/CAG Flagged, 27 In Progress, 1 Not Fulfilled, 2 Pending

### 6. **Term Governance Rating (2014–2026)**
| Dimension | Score | Verdict |
|-----------|-------|---------|
| Implementation | 56 | Moderate |
| Transparency | 36 | Concerning |
| Accountability | 40 | Concerning |

---

## 🔬 Methodology: PIB vs CAG Scoring

### Severity Levels
| Level | Definition | Gap Threshold |
|-------|------------|---------------|
| **Critical** | Major fund diversions, fraudulent claims, complete scheme failure | > 50% |
| **Major** | Significant delays, partial fund diversion, misleading claims | 25–50% |
| **Minor** | Process issues, documentation gaps, minor overstatements | < 25% |
| **Unaudited** | PIB claims exist but no CAG audit yet (too new or pending) | N/A |

### Accountability Verdict
| Verdict | Score Range | Meaning |
|---------|-------------|---------|
| **On Track** | > 75 | Mostly matching claims, minor issues only |
| **Off Track** | 40–75 | Significant gaps between claims and reality |
| **Critical** | < 40 | Multiple critical findings, severe accountability issues |
| **Unaudited** | N/A | No CAG audit available yet |

---

## 💡 Key Insights & Analysis

### Strengths
1. **Transparent Methodology** — Clearly explains PIB vs CAG, severity levels, scoring
2. **Primary Sources Only** — All data from verifiable government documents
3. **Bilingual** — English + Hindi (हिंदी)
4. **Independent** — Explicitly not affiliated with any party/government
5. **Structured Data** — 57 schemes with PIB/CAG counts, ministry, year, severity
6. **Time-series** — Tracks 2014→2026 across three Lok Sabha terms

### Limitations / Gaps
1. **404 Pages** — `/cabinet-ministers`, `/cag-findings`, `/promises` return "Page not found"
2. **No API/Export** — Data trapped in UI, no CSV/JSON download
3. **Static Scores** — No visible historical trend for individual schemes
4. **Limited Minister Detail** — Cabinet page broken, PM profile only one with detail
5. **No State-Level Data** — Central schemes only

### Notable Patterns
- **High CAG/PIB ratio** = More scrutiny (e.g., Swachh Bharat Urban: 16 CAG / 23 PIB)
- **Unaudited schemes** tend to be newer (Startup India 2016, Stand Up India 2016)
- **Critical rating** doesn't mean scheme failed — means *gap between claim and audit* > 50%
- **Safety & Environment** are lowest national indicators (34, 29 — both Critical)

---

## 🔗 Related Notes in Vault

- [[Undone By A Meme! Do Tyrants Fear Mockery More Than Machine Guns Akash Banerjee & Joyojeet Pal]] — Satire/accountability theme
- [[AndhBhakt.org - 57 Schemes Dataset]] — Full structured dataset of all 57 schemes
- [[Research/]] — For deeper civic tech analysis
- [[05 - INTELLIGENCE/]] — Patterns & syntheses layer

---

## 📌 Action Items

- [ ] Monitor for API/data export feature
- [ ] Track if 404 pages get restored
- [ ] Cross-reference CAG findings with original reports on cag.gov.in
- [ ] Compare with similar platforms (IndiaSpend, FactChecker, PRS Legislative)

---

*Analysis compiled via automated browser exploration (Playwright) across 6 pages. Full schemes text (17K chars) saved to `/tmp/andhbhakt_schemes_full.txt`.*