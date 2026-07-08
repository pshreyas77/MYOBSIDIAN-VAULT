---
date: 2026-07-08
type: map
tags: [moc, population-genetics, ancient-dna, methods, admixture, south-asia]
priority: medium-high
status: completed
ai-first: true
---

# Population Genetics Methods MOC

**For future Claude:** Your Aryan migration synthesis uses these methods but doesn't explain them. This MOC provides the methodological framework to evaluate new papers. Connects to `Research/Deep/2026-06-22 — Aryan Migration Debate Evidence and Pre-Aryan India.md`.

---

## 1. Method Map

| Method | What It Does | Key Papers | Limitations |
|--------|-------------|------------|-------------|
| **PCA** | Visualizes population structure by reducing dimensionality | Narasimhan 2019 | Descriptive only; doesn't prove admixture or directionality |
| **ADMIXTURE** | Estimates ancestry proportions assuming K ancestral populations | Moorjani 2013 | Assumes K populations; sensitive to sample choice; no directionality |
| **qpAdm** | Formal admixture modeling; tests if target is admixture of source + reference pops | Narasimhan 2019 | Requires "right" reference populations; model-dependent; overfitting risk |
| **qpGraph** | Phylogenetic tree with admixture edges | Reich 2009 | Complex; computationally intensive; overfitting risk |
| **f4-statistics** | Tests for gene flow, drift, and admixture; robust to ascertainment bias | Patterson 2012 | Requires large sample sizes; interpretation requires care |
| **DATES/ALDER** | Estimates admixture timing | Moorjani 2013 | Assumes pulse admixture; continuous admixture is harder to date |
| **X vs Autosome** | Detects sex-biased admixture (male-biased = more Y-chromosome steppe) | Narasimhan 2019 | Requires large samples; X chromosome has different recombination history |

---

## 2. Critical Update: Rakhigarhi & Steppe Timing

- **Rakhigarhi (Shinde 2019)**: IVC individuals had **zero steppe ancestry**
- **Steppe entry**: After 2000 BCE (confirmed by multiple papers: Narasimhan 2019, Vagheesh Narasimhan Science 2019)
- **Current consensus**: ANI = Steppe + Iranian farmer + AASI; ASI = Iranian farmer + AASI
- **OIT Genetics**: No geneticist supports Out of India Theory. The steppe → India direction is unambiguous from qpAdm/f4 patterns.

---

## 3. How to Evaluate New Papers (Checklist)

| Check | Why It Matters |
|-------|----------------|
| **Sample size** | Ancient DNA <10 samples is suggestive, not conclusive |
| **Dating** | Radiocarbon dates must be direct on bone, not inferred from context |
| **Contamination** | aDNA studies must report contamination estimates (<5% acceptable) |
| **Replication** | Do qpAdm/f4 results replicate with different reference populations? |
| **Publication venue** | Nature/Science/Cell are strong; predatory journals are not |

---

## 4. Entity Notes to Add

| Entity | File | Description |
|--------|------|-------------|
| **ANI-ASI** | `wiki/concepts/ANI-ASI.md` | Ancestral North Indian vs Ancestral South Indian |
| **Steppe Migration** | `wiki/concepts/Steppe-Migration.md` | Yamnaya → Corded Ware → Sintashta → India |
| **AASI** | `wiki/concepts/AASI.md` | Ancient Ancestral South Indian (Andamanese-related hunter-gatherers) |
| **Iranian Farmer** | `wiki/concepts/Iranian-Farmer-Ancestry.md` | Zagros Neolithic component in both ANI and ASI |

---

## 5. Key Papers Reference

| Paper | Year | Journal | Key Contribution |
|-------|------|---------|------------------|
| Narasimhan et al. | 2019 | *Science* | 523 ancient genomes; steppe ancestry timeline |
| Shinde et al. | 2019 | *Cell* | Rakhigarhi genome; zero steppe in IVC |
| Moorjani et al. | 2013 | *AJHG* | ANI-ASI mixture model; DATES method |
| Reich et al. | 2009 | *Nature* | Original ANI/ASI two-population paper |
| Patterson et al. | 2012 | *Genetics* | f4-statistics framework |
| Lazaridis et al. | 2016 | *Nature* | Ancient DNA from Near East/Steppe |

---

## 6. Vault Integration

- **Links to**: `Research/Deep/2026-06-22 — Aryan Migration Debate Evidence and Pre-Aryan India.md`
- **Links to**: `Research/2026-06-24 — Aryan Migration & Pre-Aryan Substrate — Final Verified Synthesis.md`
- **Links to**: `05 - MAPS/Historical Linguistics MOC.md` (complementary evidence)
- **Links to**: `05 - MAPS/Epigraphy Methods MOC.md` (complementary evidence)

---

*Report 11 of 20 | Generated: 2026-07-08 | Priority: 🟢 Medium-High | Domain: History/Science*