---
date: 2026-07-08
type: research
subtype: technical-guide
tags: [pkm, writing, publication, pandoc, obsidian, multi-format, pipeline]
priority: practical
status: completed
ai-first: true
---

# Writing & Publication Pipeline

**For future Claude:** `06 - OUTPUTS/` exists but no systematic workflow from vault → finished pieces. This pipeline enables progressive summarization → essay → multi-format publishing.

---

## 1. Progressive Summarization → Essay

| Stage | Action | Output |
|-------|--------|--------|
| **Harvest** | Collect atomic notes on a topic from MOCs, Research/, 2-atoms/ | Note cluster |
| **Connect** | Find bidirectional links and emergent themes; identify gaps | Link map |
| **Draft** | Write a "seedling" essay in Obsidian (500 words) | `03 - PROJECTS/Drafts/*.md` |
| **Grow** | Expand with evidence, counter-arguments, citations | `03 - PROJECTS/Drafts/*.md` (2000+ words) |
| **Prune** | Cut 30%; tighten structure; verify claims | Near-final draft |
| **Publish** | Export via Pandoc to target formats | `06 - OUTPUTS/*.{pdf,epub,html,md}` |

---

## 2. Technical Pipeline

```bash
# Obsidian → Pandoc → PDF/EPUB/HTML

# 1. Export from Obsidian (manual or script)
obsidian-export vault/essay.md > essay.md

# 2. Pandoc with citations
pandoc essay.md \
  --citeproc \
  --bibliography=zotero.bib \
  --csl=chicago-note-bibliography.csl \
  -o essay.pdf \
  --template=eisvogel.tex

# 3. EPUB
pandoc essay.md -o essay.epub --css=style.css

# 4. HTML (for blog)
pandoc essay.md -o essay.html --template=blog.html --css=blog.css
```

### Required Setup

| Component | Tool | Config |
|-----------|------|--------|
| **Reference manager** | Zotero | Better BibTeX → `zotero.bib` auto-export |
| **Citation style** | CSL | Chicago note-bibliography (or your preference) |
| **LaTeX template** | Eisvogel | `eisvogel.tex` for professional PDFs |
| **CSS** | Custom | For EPUB/HTML styling |

---

## 3. Multi-Format Publishing

| Platform | Format | Tool | Notes |
|----------|--------|------|-------|
| **Blog** | Markdown → HTML | Quartz / Hugo | Static site from vault |
| **PDF** | LaTeX via Pandoc | Eisvogel template | Academic/professional |
| **EPUB** | Pandoc | Custom CSS | E-reader friendly |
| **Substack** | Markdown | Manual paste | Newsletter |
| **Notion** | Markdown | Notion API | Team sharing |
| **GitHub** | Markdown | Git | Version control |

---

## 4. Vault Integration

| Folder | Purpose |
|--------|---------|
| `03 - PROJECTS/Drafts/` | Working drafts (git-tracked) |
| `06 - OUTPUTS/` | Published artifacts (final) |
| `Research/PKM/zotero.bib` | Bibliography (symlinked from Zotero) |
| `Research/PKM/templates/` | Pandoc templates (Eisvogel, blog, etc.) |
| `scripts/publish.py` | Automation script |

---

## 5. Automation Script Scaffold

```python
# scripts/publish.py
import subprocess
import frontmatter
from pathlib import Path

def publish(note_path: Path, formats: list = ["pdf", "epub", "html"]):
    """Publish a note to multiple formats."""
    # Load frontmatter for metadata
    post = frontmatter.load(note_path)
    
    # Build Pandoc command
    base_cmd = ["pandoc", str(note_path), "--citeproc", "--bibliography=zotero.bib"]
    
    if "pdf" in formats:
        subprocess.run(base_cmd + ["--template=eisvogel.tex", "-o", f"06 - OUTPUTS/{post['title']}.pdf"])
    if "epub" in formats:
        subprocess.run(base_cmd + ["--css=style.css", "-o", f"06 - OUTPUTS/{post['title']}.epub"])
    if "html" in formats:
        subprocess.run(base_cmd + ["--template=blog.html", "--css=blog.css", "-o", f"06 - OUTPUTS/{post['title']}.html"])
```

---

## 6. Vault Updates Required

- [ ] Create `Research/PKM/Writing-Publication-Pipeline.md` with this content
- [ ] Create `scripts/publish.py` 
- [ ] Set up Zotero + Better BibTeX auto-export to `Research/PKM/zotero.bib`
- [ ] Download Eisvogel template to `Research/PKM/templates/eisvogel.tex`
- [ ] Create `03 - PROJECTS/Drafts/` folder
- [ ] Test pipeline with one essay (e.g., TVK analysis or Charvaka note)

---

*Report 18 of 20 | Generated: 2026-07-08 | Priority: 🟢 Practical | Domain: PKM*