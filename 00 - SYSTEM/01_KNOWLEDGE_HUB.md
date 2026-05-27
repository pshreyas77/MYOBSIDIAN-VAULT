# 🧠 Second Brain — Knowledge Hub

**Total Notes:** ~1,160  
**Last Updated:** 2026-04-21  
**Structure:** PARA + Topic Clusters

---

## 📂 Areas by Topic

### [[01 Philosophy & Religion/|📜 Philosophy & Religion]]
Core philosophical inquiry, comparative analysis, and religious studies.

**Topics:**
- [[01 Philosophy & Religion/buddhism/|Buddhism]] — Buddha research, Buddhist philosophy
- [[01 Philosophy & Religion/shankara/|Shankara Studies]] — Advaita Vedanta critiques
- [[01 Philosophy & Religion/atheism/|Atheism & Critical Analysis]] — Charvaka, materialist critiques
- [[01 Philosophy & Religion/hinduism/|Hinduism]] — Vedic studies, nationalism
- [[01 Philosophy & Religion/caste/|Caste & Social Systems]] — Brahminism analysis
- [[01 Philosophy & Religion/philosophy-comparison/|Philosophy Comparisons]] — East-West comparisons
- [[01 Philosophy & Religion/indus-valley/|IVC Connection]] — Ancient civilizations & religion

---

### [[02 AI & Technology/|🤖 AI & Technology]]
AI research, technology stacks, and development projects.

**Topics:**
- [[02 AI & Technology/ai/|Artificial Intelligence]] — LLMs, Claude, prompts
- [[02 AI & Technology/data-science/|Data Science]] — Analysis, visualization
- [[02 AI & Technology/programming/|Programming]] — Python, scripts, tools
- [[02 AI & Technology/web-dev/|Web Development]] — Frontend, CSS, projects
- [[02 AI & Technology/os-systems/|Operating Systems]] — Linux, performance
- [[02 AI & Technology/marvel-dc/|Marvel/DC Cosmology]] — Power scaling
- [[02 AI & Technology/career/|Career & Development]] — Jobs, resumes
- [[02 AI & Technology/power-scaling/|Power Scaling]] — Hierarchies, comparisons

---

### [[03 Ancient Civilizations/|🏛️ Ancient Civilizations]]
Research into ancient cultures and early civilizations.

**Topics:**
- [[03 Ancient Civilizations/indus-valley/|Indus Valley Civilization]] — Harappa, Mohenjo-daro
- [[03 Ancient Civilizations/ancient-india/|Ancient India]] — Chanakya, Mauryan
- [[03 Ancient Civilizations/egypt/|Ancient Egypt]] — Pharaohs, pyramids
- [[03 Ancient Civilizations/sumeria/|Sumeria & Mesopotamia]] — Sumerian, cuneiform
- [[03 Ancient Civilizations/buddhism/|Buddhist Origins]] — Historical Buddha

---

### [[04 Political Analysis/|🗳️ Political Analysis]]
Political systems, elections, and governance analysis.

**Topics:**
- [[04 Political Analysis/indian-politics/|Indian Politics]] — BJP, Congress, elections
- [[04 Political Analysis/communism/|Communism & USSR]] — Cold War history
- [[04 Political Analysis/world-politics/|World Politics]] — Global conflicts
- [[04 Political Analysis/zionism/|Zionism & Nationalism]] — Comparative analysis
- [[04 Political Analysis/security/|Security & Intelligence]] — Privacy, data

---

### [[05 Knowledge Management/|🧩 Knowledge Management]]
Systems, templates, and research methodology.

**Topics:**
- [[05 Knowledge Management/ai/|AI-Powered Research]] — Obsidian AI tools
- [[05 Knowledge Management/templates/|Templates & Systems]] — Workflows

---

### [[06 Society & Culture/|👥 Society & Culture]]
Social systems, cultural analysis, and contemporary issues.

**Topics:**
- [[06 Society & Culture/caste/|Caste & Social Structure]] — System analysis
- [[06 Society & Culture/culture/|Cultural Studies]] — Modern issues

---

### 📚 [[03 - RESOURCES/00_Philosophy_Link_Tracker|Resources — Philosophy Links]]
Curated video, book, and organizational links for Osho, J. Krishnamurti, U.G. Krishnamurti, Nagarjuna, and Charvaka.

---

## 🔗 Cross-Cutting Themes

| Theme | Related Areas |
|-------|---------------|
| **Philosophy Comparison** | Phil, Ancient Civ |
| **Power Dynamics** | Politics, Knowledge |
| **Technology & Society** | AI/Tech, Society |
| **Historical Analysis** | Ancient Civ, Philosophy |
| **Critical Thinking** | Phil, Political |

---

## 📊 Quick Stats

| Category | Count |
|----------|-------|
| Total Files | ~1,160 |
| Topic Clusters | 65+ |
| Interlinks Created | 62+ |
| Areas | 7 |

---

## 🏷️ Common Tags

#philosophy #shankara #buddhism #ai #prompts #ancient-civ #politics #research

---

*Navigate by area → topic → file. Use graph view for visual exploration.*
## 🧠 God Node Dashboard

> *Core abstractions from your knowledge graph analysis*

### 🔝 Top Connected Nodes
- [[now()]] — 2,311 connections → Temporal Logic, Scheduling, Date Handling
- [[map()]] — 1,944 connections → Functional Programming, Data Transformation  
- [[error()]] — 1,056 connections → Error Handling, Debugging
- [[Values()]] — 1,026 connections → Data Structures, Object Manipulation
- [[Task]] — 697 connections → Project Management, Workflow Automation
- [[includes()]] — 842 connections → Search, Filtering, Data Validation
- [[min()/max()]] — 774/770 connections → Optimization, Comparison, Bounds Checking
- [[trim()]] — 712 connections → Text Processing, Data Cleaning
- [[has()]] — 697 connections → Existence Checks, Membership Testing

### 📊 Quick Graph Stats
| Metric | Value |
|--------|-------|
| Total Nodes Analyzed | 46,525 |
| Total Edges | 135,370 |
| Communities Detected | 352 |
| Extracted Edges | 52% |
| Inferred Edges | 48% |
| Avg Inferred Edge Confidence | 0.75 |

### 🔗 Exploration Queries
```dataview
TABLE file.link as "Note", length(file.outlinks) + length(file.inlinks) as "Connections"
FROM ""
WHERE contains(lower(file.name), "now()") OR 
      contains(lower(file.name), "map()") OR 
      contains(lower(file.name), "error()") OR 
      contains(lower(file.name), "values()") OR 
      contains(lower(file.name), "task") OR
      contains(lower(file.name), "includes()") OR
      contains(lower(file.name), "min()") OR
      contains(lower(file.name), "max()") OR
      contains(lower(file.name), "trim()") OR
      contains(lower(file.name), "has()")
SORT length(file.outlinks) + length(file.inlinks) DESC
```

```dataview
TABLE file.link as "Bridge Note", file.folder as "Location"
FROM ""
WHERE (contains(lower(file.name), "map") OR 
       contains(lower(file.name), "error") OR 
       contains(lower(file.name), "now") OR 
       contains(lower(file.name), "task") OR 
       contains(lower(file.name), "values") OR
       contains(lower(file.name), "includes") OR
       contains(lower(file.name), "min") OR
       contains(lower(file.name), "max") OR
       contains(lower(file.name), "trim") OR
       contains(lower(file.name), "has"))
  AND (contains(lower(file.content), "philosophy") OR 
       contains(lower(file.content), "ethic") OR 
       contains(lower(file.content), "value") OR 
       contains(lower(file.content), "belief") OR 
       contains(lower(file.content), "political") OR 
       contains(lower(file.content), "power") OR 
       contains(lower(file.content), "justice") OR 
       contains(lower(file.content), "religious") OR 
       contains(lower(file.content), "faith") OR 
       contains(lower(file.content), "sacred") OR 
       contains(lower(file.content), "myth") OR 
       contains(lower(file.content), "theology"))
SORT length(file.outlinks) + length(file.inlinks) DESC
LIMIT 10
```

## See Also
- [[Nagarjuna]] - Important Buddhist philosopher and founder of Madhyamaka school
- [[Buddha]] - Central figure in Buddhist philosophy and practice

- [[Nagarjuna]] - Important Buddhist philosopher and founder of Madhyamaka school