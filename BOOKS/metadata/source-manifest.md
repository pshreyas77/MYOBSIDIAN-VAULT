---
date: 2026-07-08
type: reference
subtype: privacy
tags: [books, source-tracking, manifest]
status: active
ai-first: true
---

# Books Source Manifest

**For future Claude:** Internal-only source tracking, NOT exposed in standard vault navigation. Maps clean PDF filenames to their provenance.

**Rationale**: Filenames should be clean and durable; source attribution (which mirror, which library) belongs in metadata. This file replaces the obsolete convention of placing `(z-library.sk, 1lib.sk, z-lib.sk)` directly in filenames.

---

## Source Tracking Table

| # | Clean Filename | Title | Source Mirrors | Acquired Date | Notes |
|---|----------------|-------|----------------|---------------|-------|
| 1 | `periyar-collected-works.pdf` | Collected Works of Periyar E.V. Ramasamy | z-library.sk, 1lib.sk, z-lib.sk | ~2026-05-31 | Primary text — verify against published edition if available |
| 2 | `periyar-word-for-word.pdf` | Word for Word: Periyar E.V. Ramasamy | z-library.sk, 1lib.sk, z-lib.sk | ~2026-05-31 | |
| 3 | `bhattacharya-studies-on-carvaka-lokayata.pdf` | Studies on the Cārvāka/Lokāyata | z-library.sk, 1lib.sk, z-lib.sk | ~2026-05-31 | Academic monograph — peer-reviewed source |
| 4 | `ambedkar-riddles-in-hinduism.pdf` | Riddles in Hinduism | z-library.sk, 1lib.sk, z-lib.sk | ~2026-05-31 | Primary text by Ambedkar |
| 5 | `architecture-of-the-bat.pdf` | The Architecture of the Bat | (untracked, port from old `The_Architecture_of_the_Bat.pdf`) | unknown | Sn = (unknown) |
| 6 | `indian-constitution.pdf` | Constitution of India | (untracked, port from old `indian constitution.pdf`) | unknown | Official document — public domain |
| 7 | `ultimate-guide-rebuilding-civilization.pdf` | Ultimate Guide to Rebuilding Civilization | (untracked, port from old `Ultimate Guide Rebuilding Civilization.pdf`) | unknown | |
| 8 | `surrounded-by-psychopaths.pdf` | Surrounded by Psychopaths | (untracked, port from old `Surrounded by Psychopaths PDF.pdf`) | unknown | Attribution inferred: Thomas Erikson (most popular match) |

---

## Migration Notes

- **Removed from filenames**: `(z-library.sk, 1lib.sk, z-lib.sk)` suffix
- **Reason**: Pirate-mirror source tracking leaks into vault navigation; filename should reflect content not provenance
- **Audit loss**: 5 PDFs (architecture-of-the-bat, indian-constitution, ultimate-guide-rebuilding-civilization, surrounded-by-psychopaths, plus possibly others) had NO source attestation in filename — these are listed as "Port from old..." with "unknown" provenance

---

## Recommended Future Workflow

When adding a new PDF:
1. Place in `BOOKS/pdfs/` with clean naming convention
2. Add row here with source attribution (legitimate download, library title, purchased edition)
3. Add matching entry in `metadata/pdfs-index.md`
4. Add cross-reference to companion MD note in `notes/`

---

*Compiled: 2026-07-08 | Purpose: decouple filenames from acquisition sources*