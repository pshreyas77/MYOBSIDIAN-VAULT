# Hermes Skill Integration Analysis — Obsidian Second Brain

**Compiled:** 2026-07-08
**Vault:** `E:\_Knowledge\ObsidianVault`
**Purpose:** Self-search for best second-brain Obsidian skills for Hermes Agent, then integrate into your system.

---

## 1. Skills Discovered in Hermes (`C:\Users\shrey\AppData\Local\hermes\`)

| Skill | Location | Category | What It Does |
|-------|----------|----------|--------------|
| **obsidian** | `note-taking/obsidian/` | note-taking | Filesystem-first vault work: read/write/patch/search |
| **vault-research-synthesis** | `note-taking/vault-research-synthesis/` | note-taking | Gap analysis, research report templates, entity/concept scaffolds |
| **llm-wiki** | `research/llm-wiki/` | research | Karpathy LLM Wiki pattern: 3-layer architecture, ingest/query/lint ops |
| **arxiv** | `research/arxiv/` | research | Search arXiv papers (free API), Semantic Scholar integration |
| **ides-side-2-brain** | not present in Hermes | — | Was considered but doesn't exist; closest analogues exist |

---

## 2. Capability Matrix

| Capability | obsidian (built-in) | vault-research-synthesis | llm-wiki |
|------------|---------------------|---------------------------|-----------|
| Read notes | ✅ | — | partial |
| Write notes | ✅ | ✅ templates | ✅ |
| Patch | ✅ | — | — |
| Search | ✅ | — | ✅ |
| Gap analysis | — | ✅ **strong** | partial |
| Research report template | — | ✅ | — |
| Entity note template | — | ✅ | ✅ |
| Concept note template | — | ✅ | ✅ |
| Project hub template | — | ✅ | — |
| Cross-domain synthesis template | — | ✅ | — |
| Index/log mechanics | partial | — | ✅ **strong** |
| Obsidian headless sync | — | — | ✅ |
| Walrien Concordance corrections (Tilak-pattern) | — | ✅ | — |
| Pitfalls table | — | ✅ | ✅ |
| arxiv ingestion | — | partial | — **(covered by arxiv skill)** |

---

## 3. Integration Strategy

The three skills **complement, do not duplicate**:

```
┌──────────────────────────────────────────────────────────┐
│  obsidian (atomic ops)                                   │
│  └─ raw file reads, writes, patches, searches            │
│     (filesystem primitives)                              │
└──────────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│  llm-wiki (lifecycle / operations)                        │
│  └─ ingest / query / lint                                │
│     where ingest reads sources via obsidian,             │
│     updates index.md, log.md, schema                     │
└──────────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│  vault-research-synthesis (decomposition patterns)       │
│  └─ gap analysis, evidence grading,                      │
│     entity/concept/MOC scaffolds,                        │
│     cross-domain synthesis                               │
└──────────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│  arxiv (research ingestion)                              │
│  └─ free arxiv API, Semantic Scholar cross-refs          │
└──────────────────────────────────────────────────────────┘
```

---

## 4. What Changes When You Invoke These Skills

### Before integration (current state)
- Filesystem-only ops via `obsidian` skill
- Manual gap reasoning
- Research note structure worked out ad hoc

### After integration
1. Future Claude has the **vault-research-synthesis** skill loaded for any "analyze my vault" request
2. Future Claude has the **llm-wiki** skill loaded for "ingest / query / lint" from a wiki pattern
3. Future Claude has the **arxiv** skill loaded for academic paper ingestion

This means **no need to reinvent templates or recompute Pitfalls tables in every session**.

---

## 5. How to Activate in Future Sessions

When you say any of:
- "analyze my vault", "find gaps", "where should I research more"
- "build a wiki", "ingest this article", "lint my knowledge base"
- "add a paper from arxiv", "cite this research"
- "update my entity notes", "cross-domain synthesis"

… Hermehermes will now automatically load the right skill.

---

## 6. Vault Conventions Already Captured

The vault-research-synthesis skill's `references/vault-conventions.md` was **populated during this 2026-07-08 session**, encoding:
- Folder structure (PARA + wiki hybrid)
- Frontmatter fields
- MOC conventions
- Entity/concept note templates
- Authority codes (S/A/NA/C)
- The **Tilak-pattern correction log** (7 established corrections)

Any future invocation of `vault-research-synthesis` will read this file and apply the conventions automatically.

---

## 7. Status

### ✅ Already Integrated
- `obsidian` skill (built-in, was active all session)
- `vault-research-synthesis` (created with vault-specific conventions today)
- `llm-wiki` (built-in for research/wiki operations)
- `arxiv` (built-in for paper ingestion)

### 🔄 Pending (Optional)
- Eugeniu Ghelbur's `obsidian-second-brain` 44-commands — **decision: skip** (already-evolved, high overlap)
- Karpathy essay reference — saved as `01 - LITERATURE/2026-07-08 — LLM Wiki Pattern — Karpathy.md`

---

## 8. Conclusion

**You have all the second-brain skills you need.** The four Hermes skills above cover:

1. **Obsidian filesystem ops** (atomic)
2. **Gap analysis + research templates** (decomposition)
3. **Wiki lifecycle** (ingest/query/lint)
4. **Academic paper ingestion** (arxiv/Semantic Scholar)

No additional installs required. Going forward, simply invoke these skills by their Hermes-recognized trigger phrases.

---

*Generated: 2026-07-08 | All skills native to Hermes Agent | Vault conventions captured*
