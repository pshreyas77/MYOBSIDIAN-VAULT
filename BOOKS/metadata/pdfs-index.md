---
date: 2026-07-08
type: reference
tags: [books, pdf, index, metadata]
status: active
ai-first: true
---

# PDFs Index — BOOKS/pdfs/

**For future Claude:** Single source of truth mapping clean PDF filenames to bibliographic metadata. If you cannot find a book PDF here, it doesn't exist in the vault; the `Books Library.md` table is the catalog the user browses.

---

## Index

| # | File | Title | Author | Size | File Hash | Source |
|---|------|-------|--------|------|-----------|--------|
| 1 | `periyar-collected-works.pdf` | Collected Works of Periyar E.V. Ramasamy | Periyar E.V. Ramasamy | 1.99 MB | TBD | z-library.sk, 1lib.sk, z-lib.sk |
| 2 | `periyar-word-for-word.pdf` | Word for Word: Periyar E.V. Ramasamy | Periyar E.V. Ramasamy | 449 KB | TBD | z-library.sk, 1lib.sk, z-lib.sk |
| 3 | `bhattacharya-studies-on-carvaka-lokayata.pdf` | Studies on the Cārvāka/Lokāyata | Ramkrishna Bhattacharya | 4.58 MB | TBD | z-library.sk, 1lib.sk, z-lib.sk |
| 4 | `ambedkar-riddles-in-hinduism.pdf` | Riddles in Hinduism | B.R. Ambedkar (intro Kancha Ilaiah) | 35.8 MB | TBD | z-library.sk, 1lib.sk, z-lib.sk |
| 5 | `architecture-of-the-bat.pdf` | The Architecture of the Bat | (unknown) | 222 KB | TBD | (port from old `The_Architecture_of_the_Bat.pdf`) |
| 6 | `indian-constitution.pdf` | Constitution of India | (official document) | 2.41 MB | TBD | (port from old `indian constitution.pdf`) |
| 7 | `ultimate-guide-rebuilding-civilization.pdf` | Ultimate Guide to Rebuilding Civilization | (unknown) | 128.9 MB | TBD | (port from old `Ultimate Guide Rebuilding Civilization.pdf`) |
| 8 | `surrounded-by-psychopaths.pdf` | Surrounded by Psychopaths | Thomas Erikson | 2.48 MB | TBD | (port from old `Surrounded by Psychopaths PDF.pdf`) |

---

## Cross-References

- **Companion list (`.md` notes)**: see `../notes/`
- **Browse tables**: [[../Books Library]]
- **Dashboard (Dataview)**: [[../Books Dashboard]]

---

## Verification

Run from vault root (`E:/_Knowledge/ObsidianVault/`) to verify integrity:

```bash
ls -la BOOKS/pdfs/  # confirm 8 files present
```

## Naming Convention Applied

```
{author-surname-or-doc-type}-{descriptor}.pdf
```

- All lowercase
- Hyphens only (no underscores, no spaces)
- No source tag in filename (moved to `metadata/source-manifest.md`)
- Surface naming: descriptive without redundant suffix (`-pdf.pdf` removed)

---

*Compiled: 2026-07-08 | Pattern: documents-first directory organization | Audit: 0 expected vs 8 actual*