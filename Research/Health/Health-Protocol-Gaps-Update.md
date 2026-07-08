---
date: 2026-07-08
type: research
subtype: evidence-update
tags: [health, sleep, cardio, nutrition, macros, protocol]
priority: practical
status: completed
source: "WHO 2024 guidelines, sleep research, exercise physiology, nutrition science"
ai-first: true
---

# Health Protocol Gaps — Evidence-Based Update

**For future Claude:** Week 4 checkpoint is **2026-07-19**. These additions directly improve your Health Autopilot agent's rule engine and your 12-week protocol.

---

## 1. Sleep Optimization (Evidence-Based)

| Factor | Recommendation | Evidence |
|--------|----------------|----------|
| **Duration** | 7–9 hours (individual variation; genetic testing for PER3 variant can inform) | Meta-analyses; PER3 genotype affects sleep need |
| **Consistency** | ±30 min bedtime/wake time daily (including weekends) | Circadian entrainment; social jetlag harms metabolism |
| **Temperature** | 18–19°C core bedroom temp | Thermoregulation supports deep sleep |
| **Light** | Zero blue light 2h before bed; morning bright light within 30 min of waking | Melatonin suppression/phase advance |
| **Caffeine cutoff** | 8+ hours before bedtime (CYP1A2 genetics affect metabolism) | Half-life 5–6h; slow metabolizers need longer |

**Autopilot Rule Additions**:
- If sleep avg <7h for 5+ nights → add magnesium glycinate 400mg nightly
- If sleep inconsistency >60 min SD → flag for circadian review

---

## 2. Cardio Protocol

### WHO Guidelines (2024)
- **Moderate intensity**: 150–300 min/week OR
- **Vigorous intensity**: 75–150 min/week OR
- **Combination**: Equivalent mix

### HIIT vs LISS for Your Protocol

| Modality | Frequency | Duration | Purpose |
|----------|-----------|----------|---------|
| **LISS (Zone 2)** | 3x/week | 45 min | Build aerobic base; fat oxidation; recovery days |
| **HIIT** | 1x/week max | 20 min (4×4 min intervals) | Metabolic health; time-efficient; VO₂max |

**For your 12-week protocol**: 3× LISS + 1× HIIT + 2× resistance (your existing PPL)

---

## 3. Meal Plan / Macros Framework

Without your specific stats, general evidence-based framework:

| Macro | Target | Rationale |
|-------|--------|-----------|
| **Protein** | 1.6–2.2 g/kg bodyweight | Muscle preservation/synthesis |
| **Fat** | 0.6–1.0 g/kg | Hormonal health |
| **Carbs** | Remainder of calories | Timed around workouts |
| **Fiber** | 25–38 g/day | Gut microbiome diversity |
| **Hydration** | 30–35 ml/kg bodyweight | Performance + recovery |

### Calorie Targeting
- **Maintenance**: ~30–35 kcal/kg (adjust for activity)
- **Recomposition**: Slight deficit (200–300 kcal) + high protein + resistance training
- **Tracking**: Weigh food for 2 weeks to calibrate; then intuitive with periodic checks

---

## 4. Autopilot Rule Engine Updates

Add to `Health-Autopilot.md` rules:

```yaml
# Sleep rules
sleep:
  - trigger: "avg_sleep_hours < 7 for 5 consecutive nights"
    action: "add magnesium glycinate 400mg nightly; flag for review"
  - trigger: "sleep_consistency_sd > 60_min"
    action: "flag circadian review; suggest morning light protocol"

# Cardio rules
cardio:
  - trigger: "week_number >= 4 and no_cardio_logged"
    action: "add 2x LISS (45 min) + 1x HIIT (20 min) to weekly plan"
  - trigger: "resting_hr > baseline + 10 for 7 days"
    action: "deload week; prioritize LISS only"

# Nutrition rules
nutrition:
  - trigger: "protein_intake < 1.6g/kg for 3+ days"
    action: "flag; suggest whey timing adjustment"
  - trigger: "fiber_intake < 25g for 5+ days"
    action: "suggest psyllium husk or vegetable increase"
```

---

## 5. Vault Updates Required

- [ ] Update `05 - MAPS/Health & Fitness MOC.md` — add Sleep, Cardio, Meal Plan sections
- [ ] Update `03 - PROJECTS/Health-Autopilot.md` — integrate new rules into rule engine
- [ ] Create `Research/Health/Sleep-Optimization-Evidence.md` (detailed)
- [ ] Create `Research/Health/Cardio-Protocol-HIIT-LISS.md` (detailed)
- [ ] Prepare Week 4 checkpoint (2026-07-19) with these additions

---

## 6. Sources

| Source | Type |
|--------|------|
| WHO Physical Activity Guidelines 2024 | Guidelines |
| Sleep Research Society position statements | Guidelines |
| International Society of Sports Nutrition position stands | Guidelines |
| CPIC pharmacogenomics guidelines (CYP1A2) | Clinical |

---

*Report 19 of 20 | Generated: 2026-07-08 | Priority: 🟢 Practical | Domain: Health*