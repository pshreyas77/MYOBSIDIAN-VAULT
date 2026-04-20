# 🧠 Obsidian Research Skills Hub
*Your Complete 2nd Brain Research System (2026-04-11)*

---

## 📚 **Installed Skills**

### Core Research Skills

| Skill | Trigger | Purpose | Status |
|-------|---------|---------|--------|
| **academic-research-skills:deep-research** | `/academic-research-skills:deep-research` | 13-agent research pipeline | ✅ Installed |
| **academic-research-skills:academic-paper** | `/academic-research-skills:academic-paper` | 12-agent paper writing | ✅ Installed |
| **academic-research-skills:academic-paper-reviewer** | `/academic-research-skills:academic-paper-reviewer` | Multi-perspective review | ✅ Installed |
| **academic-research-skills:academic-pipeline** | `/academic-research-skills:academic-pipeline` | Full research→write→review pipeline | ✅ Installed |
| **graphify** | `/graphify` | Knowledge graph generation | ✅ Installed |
| **obsidian-research** | `/obsidian-research` | Vault-aware research assistant | ✅ Installed |
| **simplify** | `/simplify` | Code review & optimization | ✅ Installed |

---

## 🎯 **Quick Start Workflows**

### Workflow 1: Deep Research → Vault
```
# Research any topic with academic rigor
/academic-research-skills:deep-research "Buddhism origins archaeological evidence"

# Results automatically saved to QwenVault/ or ClaudeVault/
```

### Workflow 2: Knowledge Graph → Insights
```
# Build knowledge graph of your entire vault
/graphify /home/sunny77/Documents/Obsidian Vault

# Query the graph
/graphify query "How does Buddhism connect to ancient civilizations?"
/graphify path "BJP" "Congress"
/graphify explain "Buddha avatar theory"
```

### Workflow 3: Obsidian-Aware Research
```
# Research using your existing vault knowledge
/obsidian-research "connections between my AI agents and religious research"
/obsidian-research --graph "shortest path from BaseAgent to Buddhism"
```

### Workflow 4: Academic Paper Pipeline
```
/full-pipeline "Comparing ancient civilizations: Göbekli Tepe to Indus Valley"
# → Deep research → Write → Review → Revise → Finalize
```

---

## 🔍 **Skill Details**

### 1. graphify — Knowledge Graph Generation
**Location:** `~/.claude/skills/graphify/`

**Usage:**
```bash
/graphify                          # Current directory
/graphify <path>                   # Specific path
/graphify <path> --mode deep       # Thorough extraction
/graphify <path> --update          # Incremental update
/graphify <path> --obsidian        # Generate Obsidian vault
/graphify query "<question>"       # Query existing graph
/graphify path "A" "B"             # Shortest path
/graphify explain "Node"           # Explain node
```

**Outputs for your vault:**
- `graphify-out/graph.html` — Interactive visualization
- `graphify-out/GRAPH_REPORT.md` — Audit report
- `graphify-out/graph.json` — GraphRAG data
- `GRAPHIFY KNOWLEDGE GRAPH.md` — Vault documentation

---

### 2. academic-research-skills:deep-research
**Location:** `~/.claude/skills/academic-research-skills/academic-paper/deep-research/`

**13-Agent Pipeline:**
1. **Intake Agent** — Parse research request, set scope
2. **Planner Agent** — Create research plan with milestones
3. **Librarian Agent** — Gather sources systematically
4. **Analyst Agent** — Extract findings, identify patterns
5. **Fact Checker Agent** — Verify claims against sources
6. **Synthesizer Agent** — Combine findings into coherence
7. **Critic Agent** — Identify gaps, weaknesses, contradictions
8. **Reviser Agent** — Iterate based on critique
9. **Citation Manager** — Format references (APA/MLA/Chicago)
10. **Disclosure Agent** — Document conflicts, transparency
11. **Formatter Agent** — Final formatting (PDF/LaTeX/DOCX)
12. **Stress Tester** — Edge cases, robustness
13. **Final Validator** — Pre-publication checklist

**Modes:**
- `full` — Complete 13-agent pipeline
- `quick` — Rapid brief (3-5 paragraphs)
- `paper-review` — Review existing paper
- `lit-review` — Literature survey only
- `fact-check` — Verify specific claims
- `socratic` — Guided dialogue
- `systematic-review` — Meta-analysis with PRISMA

---

### 3. academic-research-skills:academic-paper
**Location:** `~/.claude/skills/academic-research-skills/academic-paper/`

**12-Agent Writing Pipeline:**
1. **Intake Agent** — Understand requirements
2. **Literature Strategist** — Plan literature coverage
3. **Structure Architect** — Outline & IMRAD
4. **Draft Writer** — Section-by-section writing
5. **Argument Builder** — Logical flow
6. **Citation Manager** — Source tracking
7. **Fact Checker** — Accuracy verification
8. **Revision Coach** — Guided improvement
9. **Citation Compliance Agent** — Format checking
10. **Peer Reviewer** — External critique
11. **Visualization Agent** — Charts & figures
12. **Formatter Agent** — Final output

**Paper Types:** Empirical, Theoretical, Methodological, Case Study, Policy Brief
**Formats:** APA, MLA, Chicago, Harvard, Vancouver
**Output:** LaTeX, DOCX, PDF, Markdown

---

### 4. academic-research-skills:academic-paper-reviewer
**Location:** `~/.claude/skills/academic-research-skills/academic-paper-reviewer/`

**5 Simulated Reviewers:**
- **Editor in Chief** — Editorial perspective
- **Reviewer 1** — Technical depth
- **Reviewer 2** — Alternative methods
- **Reviewer 3** — Broader significance
- **Devil's Advocate** — Attack weaknesses

---

### 5. obsidian-research
**Location:** `~/.claude/skills/obsidian-research/`

**Vault-Aware Research:**
```bash
/obsidian-research "connections between Buddhism and ancient civilizations"
/obsidian-research --graph "shortest path from Buddha to Indus Valley"
/obsidian-research --themes "find patterns in 2026-04 files"
/obsidian-research --report "Hinduism origins controversy"
/obsidian-research --surprise "unexpected links between files"
```

**Configuration:**
- Default vault: `/home/sunny77/Documents/Obsidian Vault`
- Config: `~/.claude/skills/obsidian-research/config.json`

---

### 6. simplify
**Location:** `~/.claude/skills/simplify/`

**Usage:** `/simplify <files>`
Reviews code for reuse, quality, and efficiency

---

## 🔗 **Integration Points**

### Your Vault Structure
```
📂 Obsidian Vault/
├── 📂 BUDDHA/                    ← graphify Community 10
├── 📂 OLDEST CIVILIZATION/       ← graphify Community 10
├── 📂 COSMOLOGY/                 ← graphify Community 17
├── 📂 QwenVault/                 ← deep-research outputs
├── 📂 ClaudeVault/               ← academic-paper outputs
├── 📂 DeepseekVault/             ← research & analysis
├── 📂 KIWI VAULT/                ← personal knowledge
├── 📂 project OB _AI/            ← graphify Community 1-9
├── 📂 AI_Research_Agents/        ← graphify Community 0-9
├── 📄 GRAPHIFY KNOWLEDGE GRAPH.md    ← graphify documentation
├── 📄 00_OBSIDIAN RESEARCH SKILLS HUB.md  ← This file
└── 📄 MASTER LINK INDEX.md       ← Cross-vault navigation
```

### Research → Vault Flow
```
/academic-research-skills:deep-research "Buddhism vs Hinduism chronology"
    ↓
[13-agent pipeline runs]
    ↓
Save to: QwenVault/2026-04-11_[research-topic].md
    ↓
/graphify --update
    ↓
Knowledge graph updated with new connections
    ↓
/obsidian-research "Buddhism connections" (includes new file)
```

---

## 📊 **Current Knowledge Graph**

**Stats:**
- 263 nodes | 434 edges | 27 communities
- 10 "God" nodes identified
- 5 surprising cross-vault connections

**Major Clusters:**
1. **AI Research Agents** (13 communities) — Your Python framework
2. **Ancient Civilizations** — Göbekli Tepe → Indus Valley
3. **Buddhism/Hinduism** — Origins, temples, scholarly debate
4. **Political Analysis** — BJP/Congress, India-China, ideologies
5. **Cosmology** — DC/Marvel, Abrahamic, Indian religions

**Interactive Graph:**
- `graphify-out/graph.html` (local server: http://localhost:8080/graph.html)

---

## 🛠️ **Configuration Files**

### 1. ~/.claude/CLAUDE.md (Global)
Your existing global instructions already include:
- `/graphify` trigger
- Obsidian vault path references

### 2. ~/.claude/skills/obsidian-research/config.json
```json
{
  "vault_path": "/home/sunny77/Documents/Obsidian Vault",
  "default_output_dir": "QwenVault/",
  "graph_path": "graphify-out/graph.json",
  "auto_graphify": false,
  "max_files_per_query": 20
}
```

### 3. Skill Triggers in ~/.claude/
```
academic-research-skills/  ← Full academic pipeline
├── academic-paper/        ← 12-agent writing
├── deep-research/         ← 13-agent research
├── academic-paper-reviewer/ ← 5-reviewer critique
└── academic-pipeline/     ← Orchestrator

graphify/                  ← Knowledge graphs
├── graph.html             ← Interactive visualization
├── GRAPH_REPORT.md        ← Audit trail
└── graph.json             ← GraphRAG data

obsidian-research/         ← Vault-aware research
├── SKILL.md               ← Usage documentation
└── config.json            ← Vault settings
```

---

## 📝 **Usage Examples**

### Example 1: Research to Paper
```
# Step 1: Deep research
/academic-research-skills:deep-research \
  "Temple destruction in medieval India: Nalanda, Buddhism, Hindutva"

# Step 2: Write paper
/academic-research-skills:academic-paper \
  --type theoretical \
  --output latex \
  --citations apa

# Step 3: Review paper
/academic-research-skills:academic-paper-reviewer \
  --field history \
  --mode full

# Step 4: Full pipeline (alternative)
/academic-research-skills:academic-pipeline \
  "Temple destruction in medieval India" \
  --type theoretical \
  --output pdf
```

### Example 2: Knowledge Graph Queries
```
# Find connections
/graphify query "How did Modi benefit from electoral bonds?"

# Trace specific path
/graphify path "Göbekli Tepe" "Buddhism"

# Explain concept
/graphify explain "Pushyamitra Shunga"

# Directed analysis
/graphify query "BJP connections" --directed
```

### Example 3: Vault Exploration
```
# Find surprising links
/obsidian-research --surprise "unexpected connections in my vault"

# Pattern analysis
/obsidian-research --themes "common threads in corruption analyses"

# Graph-aware
/obsidian-research --graph "paths from Zionism to Hindu Nationalism"
```

---

## 🔄 **Update Workflow**

When you add new research files:
```bash
# Navigate to vault
cd "/home/sunny77/Documents/Obsidian Vault"

# Incremental graph update
/graphify . --update

# Or full rebuild
/graphify . --mode deep
```

---

## 📖 **Documentation**

| Document | Location | Content |
|----------|----------|---------|
| **GRAPHIFY KNOWLEDGE GRAPH** | Vault root | Complete graph documentation |
| **GRAPH_REPORT** | graphify-out/ | Technical graph audit |
| **GRAPH_SUMMARY** | graphify-out/ | Quick reference |
| **MASTER LINK INDEX** | Vault root | Cross-vault navigation |
| **VAULT ORGANIZATION MAP** | Vault root | Folder structure |

---

## 🎓 **Research Workflows**

### For Ancient History Research: ```
/graphify --> Query --> /deep-research --> Paper --> Review
     ↑                                      ↓
     └──────────── Update Graph ←───────────┘
```

### For Agent Development: ```
/simplify --> /graphify --watch -- Code changes tracked automatically
```

---

## 🚨 **Troubleshooting**

### Graph not rendering:
```bash
# Start local server
cd graphify-out && python3 -m http.server 8080 &
# Open: http://localhost:8080/graph.html
```

### Skill not found:```
# Check installed skills
ls ~/.claude/skills/

# Re-import if needed
cd ~/.claude/skills && git clone <repo>
```

### Research output not saving to vault:
```bash
# Check config
cat ~/.claude/skills/obsidian-research/config.json

# Ensure vault_path matches
```

---

## 🎯 **Next Steps**

1. ✅ **Skills installed** — All core research tools ready
2. ✅ **Knowledge graph built** — 263 nodes mapped
3. ✅ **Vault integration** — Files created and linked
4. ⏳ **Try a research query:**
   ```
   /obsidian-research "What connects my AI agents to Buddhism research?"
   ```
5. ⏳ **Generate a paper:**
   ```
   /academic-research-skills:academic-pipeline \
     "Comparative analysis of oldest civilizations"
   ```
6. ⏳ **Update graph after new research**

---

**Your Obsidian Vault is now a fully-equipped 2nd brain with AI-powered research capabilities!**

*Last Updated: 2026-04-11*  
*Total Skills: 7 | Graph Nodes: 263 | Communities: 27*

---

## 🔗 **ClaudeVault Research Workflow** *(New: 2026-04-14)*

> **User Preference:** All research from Claude → `ClaudeVault/` + cross-linked across vault

### Standard Protocol

| Step | Action | Location |
|------|--------|----------|
| 1 | Store research notes | `ClaudeVault/YYYY-MM-DD_title.md` |
| 2 | Tag with topics | `#research`, `#claude-generated` |
| 3 | Link to Topic files | `07 - Topics/Subject/` |
| 4 | Link to Area files | `02 - Areas/Subject/` |
| 5 | Update MASTER LINK INDEX | Root level index |
| 6 | Backlink from destinations | Reference ClaudeVault source |

### Current ClaudeVault Research
See: [[RESEARCH_WORKFLOW_PREFERENCE]] for full template and 500+ files indexed.

