---
title: "BTECH Performance Appraisal & Strategic Concepts"
date: 2026-03-31
tags:
  - machine-learning
  - linux
  - obsidian
  - job-search
  - geopolitics
  - stock-market
  - research
  - projects
  - finance
source: qwen-export
model: qwen3.5-plus
---

# BTECH Performance Appraisal & Strategic Concepts

**Date:** 2026-03-31  
**Model:** `qwen3.5-plus`  
**Topics:** [[Machine-Learning]] · [[Linux]] · [[Obsidian]] · [[Job-Search]] · [[Geopolitics]] · [[Stock-Market]] · [[Research]] · [[Projects]] · [[Finance]]

---

### 🧑 You

answer my questions BTECH 4 year  Unit 	Question	Blooms	Course outcome
III	Explain the importance, methods, and limitation of Performance Appraisal.	L2	CO3
IV	Explain the concept of Network Analysis.
Explain how to identify the critical path in a project network with an example.	    L2

L2	CO4
V	What are Objectives and Goals? Explain their role in strategic planning.
Discuss briefly about benchmarking and Balanced Scorecard.	L2    with required flow chart  and required diagrams to understand simply

L2	CO5
SET  B
Unit 	Question	Blooms	Course outcome
III	Differentiate between job evaluation and merit rating with suitable examples.	L4	CO3
IV	Discuss different types of floats and their importance in scheduling.
Explain assumptions, applications, and significance of CPM in project planning.	
   L2

L2	CO4
V	Explain SWOT Analysis in detail. How does it help organizations formulate strategies?
Differentiate between Vision and Mission by providing suitable examples.	
L2

L4	CO5
SET  C
Unit 	Question	Blooms	Course outcome
III	Explain steps involved in resolving employee grievances effectively.	L2	CO3
IV	Explain the steps involved in crashing a project with a simple numerical example.
Discuss the differences, advantages and limitations of PERT and CPM techniques.	
L2

L2	CO4
V	Explain the concept of Strategic Intent. Discuss its key elements 
Describe Strategy Formulation. Explain the steps involved in developing effective strategies. 	
L2

L2	CO5

---

### 🧑 You

make it easy ans simple for reading and understanding with defnation  and diagram

---

### 🧑 You

I’ll simplify all answers with **clear definitions**, **easy steps**, and **simple diagrams** (text‑based). Each answer is self‑contained and easy to read.

---

# SET A

## Unit III – Performance Appraisal

**Definition:**  
Performance Appraisal is the systematic evaluation of an employee’s job performance and potential.

### Importance
- Helps decide promotions, pay raises, and training needs.  
- Provides feedback to improve performance.  
- Creates records for legal protection.  

### Methods

```
Performance Appraisal Methods
        /                \
   Traditional          Modern
    |   |   |           |     |     |
Graphic Ranking Paired  MBO  360°  BARS
Rating        Comparison      Feedback
```

- **Graphic Rating Scale:** Rate traits on a scale (e.g., 1–5).  
- **Ranking:** List employees from best to worst.  
- **Paired Comparison:** Compare each employee with others.  
- **MBO (Management by Objectives):** Set goals together, then evaluate goal achievement.  
- **360° Feedback:** Get feedback from boss, peers, subordinates, self.  
- **BARS (Behaviorally Anchored Rating Scales):** Use real job behaviors as anchors.  

### Limitations
- Bias (halo effect, leniency)  
- Recency effect (focus on recent events)  
- Time‑consuming  
- Resistance from employees  

---

## Unit IV – Network Analysis

**Definition:**  
Network Analysis is a project management technique that uses diagrams to plan, schedule, and control project activities.

### Critical Path – Steps (with diagram)

```
1. List activities, durations, dependencies
          ↓
2. Draw network diagram
          ↓
3. Forward pass → ES, EF
          ↓
4. Backward pass → LS, LF
          ↓
5. Calculate float = LS – ES
          ↓
6. Activities with float = 0 → Critical Path
```

**Example Diagram:**

```
    A(3)     C(5)
   ┌───┐    ┌───┐
   │   │───→│   │
   └───┘    └─┬─┘
              │
              ↓
           ┌───┐
    B(2)   │ E │
   ┌───┐   │(2)│
   │   │──→│   │
   └───┘   └───┘
    D(4)───┘
```

**Critical Path:** A → C → E (duration 3+5+2 = 10 days)  
**Float:** Activities B and D have 2 days slack.

---

## Unit V – Objectives & Goals; Benchmarking; Balanced Scorecard

### Objectives and Goals

| Term | Definition | Example |
|------|------------|---------|
| **Goal** | Broad, long‑term aspiration | “Become market leader” |
| **Objective** | Specific, measurable, time‑bound | “Achieve 25% market share by 2026” |

**Role in Strategic Planning:**  
- Turn vision into action.  
- Provide targets for performance.  
- Align departments.

### Benchmarking
**Definition:** Comparing your processes or performance with industry best practices to improve.

**Steps:** Plan → Collect data → Analyze → Adapt → Monitor.

### Balanced Scorecard (BSC)
**Definition:** A strategy tool that measures performance from four perspectives.

```
              Vision & Strategy
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
Financial      Customer      Internal       Learning &
"How do we    "How do we    Processes      Growth
look to       appear to     "What must    "How do we
shareholders?" customers?"   we excel at?" sustain
                                            improvement?"
```

Each perspective has **objectives, measures, targets, and initiatives**.

---

# SET B

## Unit III – Job Evaluation vs. Merit Rating

**Definitions:**

- **Job Evaluation:** Determines the relative worth of a **job** (not the person) to set pay grades.  
- **Merit Rating (Performance Appraisal):** Evaluates the **employee’s performance** for rewards, promotion, feedback.

### Comparison Diagram

```
Job Evaluation                         Merit Rating
│                                       │
▼                                       ▼
Focus: Job                              Focus: Employee
Purpose: Pay structure                  Purpose: Performance improvement
Methods: Ranking, Point                 Methods: Rating scales, MBO, 360°
Output: Salary grades                   Output: Rating, bonus, promotion
Example: "Software Engineer gets        Example: "Rated 4.5/5 → annual bonus"
higher grade than HR Assistant"
```

---

## Unit IV – Floats and CPM

### Types of Floats (with diagram)

```
Timeline for an activity:

|←────────── Total Float (TF) ──────────→|
|←─ Free Float (FF) →|← Interfering Float →|
|← Independent Float (IF) →| (if any)
```

| Float Type | Definition | Importance |
|------------|------------|------------|
| **Total Float** | Time an activity can delay without delaying project end | Identifies critical activities (TF=0) |
| **Free Float** | Delay without delaying early start of next activity | Helps in scheduling dependencies |
| **Independent Float** | Delay without affecting any predecessor or successor | Rarely used, shows total independence |
| **Interfering Float** | TF – FF | If used, delays project or successor |

### CPM – Assumptions, Applications, Significance

| Aspect | Details |
|--------|--------|
| **Assumptions** | Durations known & fixed; activities independent; resources available as planned |
| **Applications** | Construction, manufacturing, software, event planning |
| **Significance** | Identifies critical path; enables cost‑time trade‑offs (crashing); provides clear schedule |

---

## Unit V – SWOT Analysis; Vision vs. Mission

### SWOT Analysis

**Definition:** A planning tool that evaluates **S**trengths, **W**eaknesses, **O**pportunities, **T**hreats.

```
        Internal           External
      +-------------+   +-------------+
      | Strengths   |   | Opportunities|
      | (advantages)|   | (chances to  |
      |             |   |  grow)       |
      +-------------+   +-------------+
      | Weaknesses  |   | Threats      |
      | (disadvantages)| | (risks)      |
      +-------------+   +-------------+
```

**How it helps in strategy:**

- **SO Strategies:** Use strengths to grab opportunities.  
- **WO Strategies:** Fix weaknesses to use opportunities.  
- **ST Strategies:** Use strengths to avoid threats.  
- **WT Strategies:** Defensive plans to reduce weaknesses and threats.

### Vision vs. Mission

| | Vision | Mission |
|--|--------|--------|
| **Definition** | What we want to become (future) | Why we exist (present) |
| **Example** | Tesla: “Create the most compelling car company of 21st century” | Tesla: “Accelerate world’s transition to sustainable energy” |

---

# SET C

## Unit III – Resolving Employee Grievances

**Definition:** A grievance is a formal complaint by an employee about unfair treatment. Effective resolution follows a step‑by‑step process.

### Steps (with flowchart)

```
1. Open Door / Informal Talk with Supervisor
            ↓
      Resolved? → Yes → End
            ↓ No
2. Formal Written Grievance to HR
            ↓
3. Investigation & Hearing
            ↓
4. Decision Communicated
            ↓
      Satisfied? → Yes → End
            ↓ No
5. Appeal to Higher Authority
            ↓
6. Final Decision & Follow‑up
```

**Key Principles:** Timely, confidential, impartial, consistent.

---

## Unit IV – Crashing; PERT vs. CPM

### Crashing a Project

**Definition:** Shortening project duration by adding resources (overtime, extra staff) to critical activities, at extra cost.

**Steps (with diagram):**

```
1. Find critical path (normal durations)
         ↓
2. Determine crash limits & cost slopes
         ↓
3. Pick critical activity with lowest cost slope
         ↓
4. Crash by one time unit
         ↓
5. Re‑compute critical path
         ↓
6. Repeat until desired duration or cost too high
```

**Simple Example:**

| Activity | Normal Time | Crash Time | Cost Slope |
|----------|-------------|------------|------------|
| B        | 4 days      | 3 days     | $60/day    |
| D        | 6 days      | 4 days     | $60/day    |

Crash B first (lowest slope) → project time reduces by 1 day, cost +$60.

### PERT vs. CPM

| Feature | PERT | CPM |
|---------|------|-----|
| **Time** | Probabilistic (3 estimates) | Deterministic (1 estimate) |
| **Focus** | Time (for R&D, new projects) | Time‑cost trade‑off |
| **Critical Path** | Based on expected time | Based on fixed time |
| **Probability** | Can calculate chance of finishing on time | No probability |
| **Use** | Uncertain, non‑routine projects | Well‑defined, repetitive projects |

**Diagram: PERT 3‑Estimates**

```
Optimistic (O)   Most Likely (M)   Pessimistic (P)
      │               │                 │
      └───────────────┼─────────────────┘
                      ▼
         Expected Time = (O + 4M + P) / 6
```

---

## Unit V – Strategic Intent & Strategy Formulation

### Strategic Intent

**Definition:** A compelling, long‑term goal that stretches the organization beyond its current resources, inspiring innovation and commitment.

**Key Elements:**
- **Direction** – clear future vision  
- **Discovery** – encourages innovation  
- **Destiny** – emotional commitment  
- **Stretch** – gap between resources and ambition

### Strategy Formulation

**Definition:** The process of developing long‑term plans to achieve organizational goals.

**Steps (with flowchart):**

```
1. Vision, Mission, Objectives
          ↓
2. External Analysis (Opportunities & Threats)
          ↓
3. Internal Analysis (Strengths & Weaknesses)
          ↓
4. Generate Strategic Alternatives
          ↓
5. Evaluate & Select Strategies
          ↓
6. Implement
          ↓
7. Monitor & Adjust
```

**Tools used:** PESTLE, Porter’s Five Forces, VRIO, SWOT, BCG Matrix.

---

All answers now include **definitions**, **simple bullet points**, and **easy diagrams** for quick understanding. You can use these directly for revision or presentation.

---
