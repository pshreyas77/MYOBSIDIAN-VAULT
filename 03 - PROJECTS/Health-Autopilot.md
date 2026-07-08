---
date: 2026-07-08
type: project
tags: [project, health-autopilot, autonomous-agent, quantified-self, fitness, supplements]
status: active
ai-first: true
---

# Health Autopilot — Adaptive Protocol Agent

**For future Claude:** Autonomous agent that reads daily notes, workout logs, supplement adherence, bloodwork → outputs weekly protocol adjustments for your 12-week integrated protocol. Part of Cross-Domain Idea Synthesis Top 3 priority.

---

## Overview

**Problem**: 12-week protocol is static. Real life: missed workouts, travel, bloodwork changes, supplement tolerance, plateau detection. Manual weekly review is inconsistent.

**Solution**: Agent consumes daily notes + health data + protocol rules → weekly adjustment note with specific, actionable changes.

---

## Inputs (Data Sources)

| Source | Location | Frequency | Parsing Method |
|--------|----------|-----------|----------------|
| Daily notes | `04 - DAILY/YYYY-MM-DD.md` | Daily | Read markdown, extract checklist items, health section |
| Workout logs | Daily notes + potential separate log | Per workout | Structured parsing (exercise, sets, reps, RPE, weight) |
| Supplement adherence | Daily notes checklist | Daily | Checkbox parsing (✓/✗ for each Tier A supplement) |
| Bloodwork PDFs | `Attachments/bloodwork/` or similar | Monthly | NotebookLM upload → structured extraction |
| Body measurements | Daily/weekly notes | Weekly | Weight, waist, progress photos metadata |
| Sleep/energy subjective | Daily notes | Daily | 1-10 scale or qualitative |

---

## Protocol Rules Engine (From Your MOC)

### Tier A Supplements (Non-Negotiable Baseline)
- Whey Protein — 1.6-2.2g/kg/day target
- Creatine Monohydrate — 5g daily
- Caffeine — Pre-workout, ≤400mg/day
- Omega-3 — 2-3g EPA/DHA daily
- Vitamin D3 — 4000-5000 IU daily (India: common deficiency)
- Berberine — 500mg 2-3x/day with meals (GI monitoring)

### Training: 3-Day PPL with 4kg Dumbbells
- Push / Pull / Legs rotation
- 45-60s rest between sets
- Progression: Track 4kg dumbbell max reps per exercise
- Deload triggers: RPE >9 for 2+ sessions, joint pain, sleep <6 for 3+ nights

### Checkpoints
- **Week 4 (2026-07-19)**: Full review — adjust Weeks 5-8
- **Week 8**: Mid-point — adjust Weeks 9-12
- **Week 12**: Final — plan next cycle

---

## Agent Logic: Weekly Adjustment Rules

### Supplement Adjustments
| Trigger | Action |
|---------|--------|
| Berberine GI upset noted ≥3x/week | Reduce to 500mg 1x/day with largest meal; trial berberine HCl vs dihydroberberine |
| Creatine bloating | Split 5g → 2.5g AM + 2.5g PM; ensure 3L+ water |
| Vitamin D3 bloodwork >80 ng/mL | Reduce to 2000 IU maintenance |
| Omega-3 fish burps | Switch to enteric-coated or algal DHA |
| New bloodwork: fasting glucose >100 mg/dL | Add berberine 500mg 3x/day; prioritize post-meal walks |

### Training Adjustments
| Trigger | Action |
|---------|--------|
| RPE >9 for same exercise 2+ sessions | Deload: -20% volume (sets × reps) for that movement 1 week |
| Joint pain (knee/shoulder/elbow) | Swap exercise: DB bench → floor press; squat → goblet squat; row → chest-supported row |
| Missed ≥2 sessions/week | Compress to 2-day full-body; don't "make up" — continue rotation |
| Plateau: no rep increase 3+ weeks | Add 1 set/exercise; or reduce rest to 30s; or add drop set final set |

### Recovery Adjustments
| Trigger | Action |
|---------|--------|
| Sleep score <6 for 5+ nights | Add magnesium glycinate 400mg nightly; caffeine cutoff 12pm |
| HRV trending down 7+ days | Deload week; prioritize sleep; reduce caffeine |
| Resting HR >10 bpm baseline | Check hydration, electrolytes, overtraining |

---

## Tool Stack

| Component | Tool | Why |
|-----------|------|-----|
| **Data Analysis** | Julius AI (free tier) | Chat with CSV/spreadsheets of workout logs, measurements |
| **Bloodwork Parsing** | NotebookLM | Upload PDF → ask for structured JSON extraction |
| **Reasoning** | Local Ollama (qwen2.5:7b) | Privacy for health data; runs on i5-8350U 8GB |
| **Orchestration** | genericagent SOP | Your existing agent framework |
| **Vault I/O** | File tools (read/write) | Direct markdown note manipulation |

---

## Agent Configuration

```yaml
agent:
  name: health-autopilot
  schedule: "weekly sunday 20:00"  # Before Monday workout week
  max_runtime_minutes: 30
  
stages:
  collect:
    - read: "04 - DAILY/last-7-days/*.md"
    - parse: workout_logs, supplement_checklist, subjective_scores
    - load: latest_bloodwork.json (from NotebookLM)
    - load: measurements.csv (weight, waist, etc.)
    
  analyze:
    - tool: julius_ai
      prompt: |
        Analyze 7-day training adherence, supplement adherence, 
        progression trends, recovery metrics. 
        Output: JSON with flags, trends, recommendations.
    - tool: local_llm
      prompt: |
        Apply protocol rules engine to analysis output.
        Generate specific adjustments for Week N.
        
  generate:
    - output: "04 - DAILY/Weekly-Review-YYYY-MM-DD.md"
    - format: structured sections (Supplements, Training, Recovery, Checkpoint)
    - link: wikilinks to protocol MOC, bloodwork source, daily notes
    
  notify:
    - if: checkpoint_week (4, 8, 12)
    - then: create extended review note in 06-OUTPUTS/
```

---

## Output Format: Weekly Review Note

```markdown
---
date: 2026-07-13
type: weekly-review
week: 4
checkpoint: true
tags: [health, weekly-review, protocol-adjustment]
---

# Weekly Review — Week 4 (2026-07-07 to 2026-07-13)

## Checkpoint Status: WEEK 4 FORMAL REVIEW

## Adherence Summary
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Workout sessions | 3 | 3 | ✅ |
| Supplement adherence (Tier A) | 100% | 95% | ⚠️ Missed creatine 2x |
| Sleep avg | ≥7h | 6.8h | ⚠️ |
| Protein target | 160g | 145g | ⚠️ |

## Bloodwork Delta (vs Baseline)
| Marker | Baseline | Current | Change | Protocol Implication |
|--------|----------|---------|--------|---------------------|
| Fasting glucose | 98 | 92 | -6 mg/dL | ✅ Berberine working |
| Vitamin D | 22 | 48 | +26 ng/mL | ✅ Reduce D3 to 2000 IU |
| LDL | 130 | 115 | -15 mg/dL | ✅ Omega-3 + training |
| Testosterone | 450 | 520 | +70 ng/dL | ✅ Creatine + sleep + training |

## Adjustments for Week 5-8

### Supplements
- **Vitamin D3**: Reduce to 2000 IU daily (bloodwork >40 ng/mL)
- **Berberine**: Continue 500mg 2x/day (glucose trending down, no GI issues)
- **Add**: Magnesium glycinate 400mg nightly (sleep avg 6.8h)

### Training
- **Push Day**: Add 1 set to DB bench (3→4 sets) — progression stalled Week 3
- **Pull Day**: Swap bent-over row → chest-supported row (lower back fatigue)
- **Legs**: Goblet squat 4kg → 4kg + 5kg backpack (progression)

### Recovery
- Caffeine cutoff: 12pm sharp
- Add 10-min evening walk post-dinner (glucose + digestion)

## Checkpoint Decision
**Continue protocol with above adjustments.** Week 8 review scheduled 2026-08-16.

## Links
- [[05 - MAPS/Health & Fitness MOC]]
- [[Research/2026-06-21-3 — Integrated Health Protocol — Training + Supplement Synthesis]]
- [[04 - DAILY/2026-07-07]] ... [[04 - DAILY/2026-07-13]]
- [[Attachments/bloodwork/2026-07-10-comprehensive.pdf]]
```

---

## First Week Deliverable (2026-07-13 for Week 4 Checkpoint)

- [ ] Bloodwork PDF uploaded to NotebookLM, structured JSON extracted
- [ ] Last 7 daily notes parsed for adherence data
- [ ] Julius AI analysis run on workout/measurement CSV
- [ ] Local LLM applies rules engine → generates adjustments
- [ ] `04 - DAILY/Weekly-Review-2026-07-13.md` created (Week 4 checkpoint)
- [ ] Project hub note created: `03 - PROJECTS/Health-Autopilot.md`
- [ ] Added to `05 - MAPS/AI & Technology MOC.md` and `05 - MAPS/Health & Fitness MOC.md`
- [ ] Night Shift cron configured for weekly Sunday runs

---

## Vault Integration

```
03 - PROJECTS/
├── Cross-Domain Idea Synthesis.md
├── History-Watchdog.md
├── Health-Autopilot.md              ← This project hub
└── Health-Autopilot/
    ├── bloodwork/                    ← Parsed JSON from NotebookLM
    ├── measurements.csv              ← Weight, waist, bodyfat tracking
    ├── workout-log.csv               ← Structured: date, exercise, sets, reps, RPE, weight
    ├── supplements.csv               ← Daily adherence per supplement
    ├── weekly-reviews/               ← Generated review notes (symlinked to 04-DAILY)
    └── logs/
        
04 - DAILY/
├── Weekly-Review-2026-07-13.md       ← Week 4 checkpoint (generated)
├── Weekly-Review-2026-07-20.md       ← Week 5 (generated)
└── ...

06 - OUTPUTS/
├── Health-Protocol-Week4-Checkpoint-2026-07-13.md  ← Extended checkpoint report
├── Health-Protocol-Week8-Review-2026-08-16.md
└── Health-Protocol-Final-2026-09-27.md
```

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Weekly review generated | 100% (every Sunday) |
| Checkpoint reviews (W4, W8, W12) | Extended reports in 06-OUTPUTS |
| Protocol adherence improvement | >90% supplement, 100% workouts |
| Bloodwork trends | Glucose ↓, Vit D 40-60, LDL ↓, Test ↑ |
| Subjective energy/sleep | Avg ≥7/10 by Week 8 |

---

## Related Notes

- [[Cross-Domain Idea Synthesis]] — Parent idea
- [[05 - MAPS/AI & Technology MOC]] — Tech project map
- [[05 - MAPS/Health & Fitness MOC]] — Health map
- [[Research/2026-06-21-3 — Integrated Health Protocol — Training + Supplement Synthesis]] — Protocol source
- [[genericagent/memory/autonomous_operation_sop.md]] — Agent framework
- [[house-rules.md]] — Night Shift rules
- [[Research/AI Tools/2026-06-19 — AI-Specific Researcher Tools 2026 — Complete Table.md]] — Julius AI, NotebookLM refs

---

*Created: 2026-07-08 | Status: Ready to implement | Priority: #2 of Cross-Domain Top 3 | Week 4 Checkpoint: 2026-07-19*