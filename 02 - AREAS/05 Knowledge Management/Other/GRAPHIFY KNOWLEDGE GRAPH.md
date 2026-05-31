# Graphify Knowledge Graph

**Generated:** 2026-04-11  
**Source:** Complete Obsidian Vault Graphification  
**Files Processed:** 526 | **Nodes:** 263 | **Edges:** 434 | **Communities:** 27

---

## Quick Stats

- **Total corpus:** ~3,272,796 words across 526 files
- **[[Ancient Civilizations]] cluster:** 13 nodes
- **[[AI Research Agents]] cluster:** 13 communities
- **[[Religious Studies]] cluster:** Buddhism, Hinduism, Jainism connections
- **[[Political Analysis]] cluster:** BJP/Congress, India-China, Zionism

---

## Your Research Clusters

### 1. Ancient Civilizations Research
*Chronological sequence from 9600 BCE*

| Rank | Civilization | Era | Key File |
|------|--------------|-----|----------|
| 1st | [[Göbekli Tepe]] | 9600-8200 BCE | OLDEST CIVILIZATION/GÖBEKLI TEPE |
| 2nd | [[Çatalhöyük]] | 7500-5700 BCE | ÇATALHÖYÜK |
| 3rd | [[Ancient Egypt]] | 6000-30 BCE | ANCIENT EGYPTIAN |
| 4th | [[Mesopotamian Sumerian]] | 4500-1750 BCE | MESOPOTAMIAN SUMERIAN |
| 5th | [[Caral-Supe]] | 3500-1800 BCE | CARAL-SUPE |
| 6th | [[Indus Valley]] (Harappan) | 3300-1300 BCE | INDUS VALLEY |

```
Hyperedge: Oldest Civilizations Timeline
[gobekli_tepe] --precedes--> [catalhoyuk] --precedes--> [ancient_egypt]
                                    |
                            [sumerian] --chronologically--> [indus_valley]
```

---

### 2. Buddhism & Hinduism Origins Research
*13-thread comparative analysis*

**Core Nodes:**
- [[BUDDHA RESEARCH]] ←→ [[BUDDHA EVIDENCE]]
- [[Siddhartha Gautama]] (The Buddha) ← founded → [[Buddhism]]
- [[Lumbini]] ← birthplace → [[Buddha]]
- [[Nalanda]] ← center of → [[Buddhism]] ← destroyed by → [[Bakhtiyar Khilji]]

**Surprising Connection:**
```
Buddhism --related_tradition--> Jainism [INFERRED]
Source: Buddha Evidence ↔ QwenVault Buddha-Jain Timeline
```

**Controversial Findings:**
- Buddhist monuments 400-500 years older than Hindu temples
- [[Vishnu Purana]] (400-500 CE) first mentions Buddha as avatar
- [[Buddha avatar theory]] ← rationale: [[Absorption strategy]]

---

### 3. AI Research Agents Framework
*Multi-agent orchestration system (245 files in ClaudeVault)*

**God Nodes** (most connected):
| Node | Edges | Role |
|------|-------|------|
| `BaseAgent` | 56 | Foundation framework |
| `AgentMessage` | 49 | Communication protocol |
| `AnalysisAgent` | 20 | Pattern recognition |
| `ResearchOrchestrator` | 20 | Workflow coordinator |
| `SynthesisAgent` | 18 | Findings synthesis |

**Agent Communities:**
- [[Analyzer Agents]] ←→ [[Synthesizer Agents]]
- [[Citation Manager]] ←→ [[Fact Checker]]
- [[Retriever Agents]] ←→ [[Vault Search]]
- [[Orchestrator]] ← coordinates → all agents

---

### 4. Political & Ideological Analysis

**Indian Politics Cluster:**
- [[BJP]] ←→ [[Congress (INC)]] (political rivals)
- [[Electoral Bonds]] ← benefited → [[BJP]]
- [[2G Spectrum Scam]], [[Coal Scam]] ← associated with → [[INC]]

**Comparative Ideologies:**
- [[Zionism]] ← compared to → [[Hindu Nationalism]]

**Geopolitical:**
- [[India]] ← compared economically → [[China]]

---

### 5. Religious Cosmology Comparison

**Abrahamic Traditions:**
- [[Christianity]] ←→ [[Islam]] (theological cousins)

**Indian Traditions:**
- [[Buddhism]] ←→ [[Hinduism]] ←→ [[Jainism]]
- [[Mahavira]] ← founder → [[Jainism]]
- [[Buddha]] ← contemporary → [[Mahavira]]

**Comic Cosmology:**
- [[Marvel Cosmology]] ←→ [[DC Cosmology]]

---

### 6. Technical Projects

**Local RAG System:**
- [[KeywordRAG]] ←→ [[build_chain]]
- [[load_and_index]] ←→ [[get_keywords]]

**Web Development:**
- [[React]] ←→ [[Node.js]] (Food Nutrition website)
- [[Three.js]] ← complementary → [[React]] (3D Portfolio)

**Linux/Systems:**
- [[Feren OS]] ← KDE Plasma [[Batman theme]]

---

## Cross-Vault Surprising Connections

1. **Religious Continuity:** 
   ```
   Buddhism ←→ Jainism (contemporary founders)
   Evidence: Buddha (~500 BCE), Mahavira (~600-510 BCE)
   ```

2. **Technology Stack Bridge:**
   ```
   Three.js (DeepseekVault/3D Portfolio) 
   --complementary-->
   React (QwenVault/Food Nutrition)
   ```

3. **Code-Research Bridge:**
   ```
   Deep Research AI Agents Demo
   --uses-->
   InformationRetrieverAgent
   --uses-->
   AnalysisAgent
   ```

---

## Geographic Distribution

| Region | Key Sites/Entities |
|--------|------------------|
| **India** | Lumbini, Sarnath, Nalanda, Rakhigarhi, Indus Valley |
| **Mesopotamia** | Uruk, Gilgamesh, Sumerian cities |
| **Turkey** | Göbekli Tepe, Çatalhöyük |
| **Americas** | Caral-Supe (Peru) |
| **China** | Comparative economy, data centers |
| **Middle East** | Zionism comparison, Saudi/Israel weapons |

---

## Scholars Referenced

- [[Wendy Doniger]] - Hinduism/Buddhism scholarship
- [[Romila Thapar]] - Ancient Indian history
- [[Richard Gombrich]] - Buddhist studies
- [[Johannes Bronkhorst]] - Sanskrit/Buddhist texts
- [[Helmuth von Glasenapp]] - Hindu appropriation analysis
- [[B.R. Ambedkar]] - Rejected caste system, converted to Buddhism

---

## Files Generated

```
graphify-out/
├── graph.html          ← Interactive visualization (open in browser)
├── GRAPH_REPORT.md     ← Full technical audit
├── GRAPH_SUMMARY.md    ← Quick reference
└── graph.json          ← Raw graph data (GraphRAG-compatible)
```

---

## Usage

### Query the Graph
```bash
# From terminal in vault directory
gotify query "How does Buddhism connect to ancient civilizations?"
gotify query "How does BaseAgent coordinate with other agents?"
gotify path "Buddha" "Indus Valley"
```

### Update Graph
```bash
# After adding new files
gotify /path/to/vault --update
```

---

## Next Steps

1. **Explore the interactive graph:** Open `graphify-out/graph.html`
2. **Query specific paths:** "How does Hindu nationalism compare to Zionism?"
3. **Find surprising connections:** Look for INFERRED edges in [[GRAPH_REPORT_1]]
4. **Add new research:** Re-run graphify to update

---

*Last Updated: 2026-04-11*  
*Corpus: 526 files | Communities: 27 | Cohesion: 0.1-1.0*