---
date: 2026-07-09
type: metadata
subtype: pdf-index
tags: [books, pdf, index, metadata]
status: active
---

# PDFs Index — `BOOKS/pdfs/`

> Machine-readable mapping of all PDF files in the vault's BOOKS collection.
> Used for quick lookups, scripts, and cross-referencing with notes.

| Clean Filename | Bibliographic Title | Author | Category | Has Note | Note Filename | Size (bytes) | SHA256 (body) |
|---|---|---|---|---|---|---|---|
| periyar-collected-works.pdf | Collected Works of Periyar E.V. Ramasamy | Periyar E.V. Ramasamy | Anti-caste / Dravidian | ✅ | Collected Works of Periyar E.V. Ramasamy.md | 1,988,585 | pending |
| periyar-word-for-word.pdf | Word for Word: Periyar E.V. Ramasamy | Periyar E.V. Ramasamy | Anti-caste / Dravidian | ✅ | Word for Word Periyar E.V. Ramasamy.md | 2,413,611 | pending |
| bhattacharya-studies-on-carvaka-lokayata.pdf | Studies on the Cārvāka/Lokāyata | Ramkrishna Bhattacharya | Philosophy / Indian Materialism | ✅ | Studies on the Cārvāka Lokāyata.md | 4,575,535 | pending |
| architecture-of-the-bat.pdf | The Architecture of the Bat | (unknown) | Science / Cognition | ❌ | — | 221,445 | pending |
| indian-constitution.pdf | Constitution of India | (official document) | Governance / Law | ❌ | — | 2,413,611 | pending |
| ultimate-guide-rebuilding-civilization.pdf | Ultimate Guide to Rebuilding Civilization | (unknown) | Systems / Survival | ❌ | — | 128,867,076 | pending |
| surrounded-by-psychopaths.pdf | Surrounded by Psychopaths | Thomas Erikson | Psychology / Manipulation | ❌ | — | 2,483,899 | pending |
| ambedkar-riddles-in-hinduism.pdf | Riddles in Hinduism | B.R. Ambedkar (intro Kancha Ilaiah) | Anti-caste / Religious Critique | ✅ | Riddles in Hinduism.md | 35,816,513 | pending |

---

## Source Tracking (formerly in filenames)

| Clean Filename | Original Filename Tag | Notes |
|---|---|---|
| periyar-collected-works.pdf | (z-library.sk, 1lib.sk, z-lib.sk) | Removed from filename; stored here |
| periyar-word-for-word.pdf | (z-library.sk, 1lib.sk, z-lib.sk) | Removed from filename; stored here |
| bhattacharya-studies-on-carvaka-lokayata.pdf | (z-library.sk, 1lib.sk, z-lib.sk) | Removed from filename; stored here |
| ambedkar-riddles-in-hinduism.pdf | (z-library.sk, 1lib.sk, z-lib.sk) | Removed from filename; stored here |

---

## Status Notes

- **Has Note**: All 8 PDFs currently lack companion `.md` notes in `BOOKS/notes/`. Consider creating notes for priority PDFs (Periyar, Bhattacharya, Ambedkar) using the Book Template.
- **SHA256**: Marked "pending" — compute on demand or via script to detect drift if re-downloaded.
- **Cross-ref**: This index should be updated whenever PDFs are added/removed/renamed.

---

## Update Procedure

When adding a PDF to `BOOKS/pdfs/`:
1. Use clean kebab-case filename: `author-title-keywords.pdf`
2. Add row to table above
3. Add source tag to "Source Tracking" if applicable
4. Update `Books Library.md` PDFs section
5. If creating a companion note in `BOOKS/notes/`, update "Has Note" and "Note Filename" columns