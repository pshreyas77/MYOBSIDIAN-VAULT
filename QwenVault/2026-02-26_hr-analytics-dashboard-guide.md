---
title: "HR Analytics Dashboard Guide"
date: 2026-02-26
tags:
  - python
  - machine-learning
  - data-analysis
  - obsidian
  - job-search
  - stock-market
  - research
  - projects
  - web-dev
  - game-design
source: qwen-export
model: qwen3.5-plus
---

# HR Analytics Dashboard Guide

**Date:** 2026-02-26  
**Model:** `qwen3.5-plus`  
**Topics:** [[Python]] · [[Machine-Learning]] · [[Data-Analysis]] · [[Obsidian]] · [[Job-Search]] · [[Stock-Market]] · [[Research]] · [[Projects]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

Here's your detailed prompt to build the HR Analytics Dashboard using OpenCode (AI coding assistant):

---

## Master Prompt (Use This First)

```
I want to build a complete HR Analytics Dashboard using Python 
instead of Power BI. I will use the IBM HR Analytics dataset 
from Kaggle (WA_Fn-UseC_-HR-Employee-Attrition.csv).

My skill level: Complete beginner
Goal: Portfolio-ready dashboard for resume

Tech stack I want to use:
- Python (pandas for data cleaning)
- Plotly/Dash for interactive dashboard
- DAX-equivalent calculations in Python

Please guide me phase by phase. Start with Phase 1 only 
and wait for my confirmation before moving to next phase.

Phase 1: Load and explore the dataset
Phase 2: Data cleaning
Phase 3: KPI calculations
Phase 4: Build interactive dashboard
Phase 5: Deploy online (free)
Phase 6: GitHub documentation

Start Phase 1 now.
```

---

## Phase-by-Phase Prompts

**Phase 1 - Load Data:**
```
Phase 1: Write Python code to:
1. Load WA_Fn-UseC_-HR-Employee-Attrition.csv using pandas
2. Show shape, column names, data types
3. Show first 5 rows
4. Check for null values
5. Show basic statistics (describe())

Add comments explaining every single line of code.
I am a beginner.
```

---

**Phase 2 - Data Cleaning:**
```
Phase 2: Using the IBM HR dataset already loaded, write 
Python pandas code to:
1. Remove useless columns: EmployeeCount, Over18, 
   StandardHours, EmployeeNumber
2. Create AgeGroup column: 18-30, 31-40, 41-50, 50+
3. Create SalarySlab: Low(<=5K), Medium(5K-10K), 
   High(10K-15K), Very High(>15K)
4. Create TenureCategory: New(0-2), Mid(3-5), 
   Senior(6-10), Veteran(>10)
5. Convert Attrition Yes/No to 1/0 for calculations
6. Print cleaned dataframe shape and sample

Explain every step with comments.
```

---

**Phase 3 - KPI Calculations:**
```
Phase 3: Using the cleaned IBM HR dataframe, 
calculate these KPIs using Python pandas:

1. Total Employees
2. Total Attrition (where Attrition = 1)
3. Attrition Rate % (round to 2 decimal)
4. Active Employees
5. Average Age
6. Average Monthly Income
7. Average Years at Company
8. Attrition by Department (count + rate %)
9. Attrition by Age Group
10. Attrition by Gender
11. Attrition by Salary Slab
12. Attrition by Job Role
13. Overtime impact on attrition

Print all results clearly labeled.
Add comments explaining every line.
```

---

**Phase 4 - Build Dashboard:**
```
Phase 4: Build a complete interactive dashboard using 
Plotly Dash with the IBM HR Analytics cleaned data.

Include:
1. Header: "HR Analytics Dashboard - Attrition Analysis"

2. KPI Cards row (4 cards):
   - Total Employees
   - Attrition Rate %
   - Active Employees  
   - Average Tenure

3. Dropdown/Slicer filters:
   - Department
   - Gender
   - Age Group

4. Charts:
   - Bar chart: Attrition by Department
   - Column chart: Attrition by Age Group
   - Donut chart: Attrition by Gender
   - Horizontal bar: Attrition by Job Role
   - Bar chart: Attrition by Salary Slab

5. Color scheme:
   - Background: #F8F9FA
   - Primary: #2E5C8A
   - Attrition highlight: #E07A5F
   - Positive: #81B29A

6. Make all charts interactive - clicking filters update 
   all other charts

Write complete working code in a single app.py file.
Add comments on every section.
```

---

**Phase 5 - Deploy Free:**
```
Phase 5: I have built my HR Analytics Dash app in app.py.
Help me deploy it for free online so I can share the link 
on my resume and LinkedIn.

Options to explain:
1. Deploy on Render.com (free tier)
2. Deploy on Railway.app (free tier)

For each option give me:
- Exact files I need to create (requirements.txt, 
  Procfile, etc.)
- Step by step deployment instructions
- How to get the public shareable URL

I am a complete beginner. Explain every step.
```

---

**Phase 6 - GitHub + README:**
```
Phase 6: Write a complete professional README.md for my 
HR Analytics Dashboard Python project on GitHub.

Include:
1. Project title and description
2. Live demo link placeholder
3. Dashboard screenshot placeholder
4. Key insights found (use real IBM dataset insights)
5. Tech stack used
6. How to run locally (step by step)
7. Folder structure
8. Business recommendations from analysis
9. Contact/LinkedIn section

Make it look impressive for recruiters.
Format with proper markdown, emojis, badges.
```

---

## Stuck Prompt (Use Anytime)

```
I am building HR Analytics Dashboard in Python Dash.
I am on Phase [X] and getting this error:

[paste exact error message here]

My current code is:
[paste your code here]

Fix the error and explain what caused it and 
why your fix works. I am a beginner.
```

---

### 🧑 You

check and fix errors and debug code

---

### 🧑 You

use this csv file

---

### 🧑 You

add : AI search option and use only grey ,white, black colors to make css

---
