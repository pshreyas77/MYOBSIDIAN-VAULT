---
title: "HCI UNIT III Models Theories"
date: 2025-11-30
tags:
  - machine-learning
  - linux
  - obsidian
  - job-search
  - geopolitics
  - stock-market
  - research
  - creative
  - web-dev
  - game-design
source: qwen-export
model: qwen3-max-2025-10-20
---

# HCI UNIT III Models Theories

**Date:** 2025-11-30  
**Model:** `qwen3-max-2025-10-20`  
**Topics:** [[Machine-Learning]] · [[Linux]] · [[Obsidian]] · [[Job-Search]] · [[Geopolitics]] · [[Stock-Market]] · [[Research]] · [[Creative]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

### UNIT III: MODELS AND THEORIES  
**CS8079 – HUMAN COMPUTER INTERACTION**  
(As per Anna University syllabus – 10 classes)

#### Topics Covered
- Cognitive models  
- Socio-Organizational issues and stakeholder requirements  
- Communication and collaboration models  
- Hypertext, Multimedia and WWW  

---

### 1. Cognitive Models
Cognitive models describe how humans perceive, think, remember and solve problems while interacting with systems.

| Model                        | Description                                                                                          | Key Features / Diagram                                                                                           | Goal / Use in HCI                                                                 |
|------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Goal, Operators, Methods, Selection Rules (GOMS)** | Predicts user performance by breaking tasks into goals, operators, methods and selection rules.      | Hierarchy: Goal → Sub-goals → Methods → Operators → Selection rules                                             | Quantitative prediction of execution time & learning time                         |
| **Keystroke-Level Model (KLM)** | Simplified version of GOMS; predicts time for error-free expert performance.                        | T = Tk + Tp + Th + Td + Tm + Tr  <br>(Keystroking, Pointing, Homing, Drawing, Mental act, System response)      | Fast estimation of task time (6 operators only)                                   |
| **Cognitive Complexity Theory** | Two independent mental systems: Theory of Model Human Processor & Theory of Descriptive/Prescriptive models | -                                                                                                                 | Explains why some interfaces are harder to learn/use                              |
| **Human Processor Model (Card, Moran & Newell)** | Three interacting subsystems: Perceptual, Cognitive, Motor                                   | → Perceptual (1 sec buffer) → Cognitive (2–3 sec) → Motor (70–100 ms) <br>Memory stores: WM decay 7±2 chunks (7s single, 73s rehearsed), LTM unlimited | Explains reaction time, memory limitations, Fitts’ Law, Power Law of Practice    |
| **Hierarchical Task Analysis (HTA)** | Breaks task into goals and sub-goals with plans                                               | Textual or diagrammatic tree structure                                                                           | Task decomposition for training & interface design                                |

**Important Diagram – Human Processor Model**

```
Visual/Auditory Input → [Perceptual Processor] → [Working Memory] ↔ [Long-term Memory]
                                           ↓
                                   [Cognitive Processor]
                                           ↓
                                    [Motor Processor] → Physical Action
```

---

### 2. Socio-Organizational Issues and Stakeholder Requirements

| Issue                                 | Description                                                                                           | Impact on HCI Design                                                                 |
|---------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Organizational structure & politics  | Power distribution, departmental boundaries                                                           | May force compromises in design (e.g., legacy system integration)                   |
| Job design & work roles               | Task allocation, autonomy, skill level                                                               | Affects training needs, error rates, job satisfaction                                |
| Stakeholder conflicts                | Users vs managers vs developers vs clients                                                            | Requirement conflicts (e.g., manager wants audit trail vs user wants speed)         |
| Participatory design                  | Involving real users throughout design cycle                                                          | Reduces resistance, increases acceptance                                             |
| Ethnography & Contextual Inquiry     | Observing users in real environment                                                                   | Uncovers hidden requirements that interviews miss                                    |

**Stakeholder Types**  
Primary – actual end users  
Secondary – affected by system but not direct users  
Tertiary – affected by introduction or operation (e.g., IT support)

---

### 3. Communication and Collaboration Models

| Model                              | Purpose                                                                                        | Key Concept / Diagram                                                                      |
|------------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **Face-to-face conversation model** | Basis of all human communication                                                              | Speaker → Message → Listener + Feedback loop                                               |
| **Norman’s Seven Stages of Action** | Explains how users form intention → execute → evaluate                                        | 1. Forming the goal<br>2. Forming the intention<br>3. Specifying action<br>4. Executing action<br>5. Perceiving world<br>6. Interpreting state<br>7. Evaluating outcome<br>**Gulf of Execution** & **Gulf of Evaluation** |
| **CSCW (Computer-Supported Cooperative Work) Matrix** | Classifies groupware applications                                                      | Time: Same / Different<br>Location: Same / Different<br>→ 4 quadrants: Face-to-face, Asynchronous distributed, etc. |
| **Language/Action Perspective (Winograd & Flores)** | Actions are performed through language (requests, promises, declarations)             | Conversation for Action cycle: Request → Negotiate → Promise → Perform → Declare complete |

**Diagram – Norman’s Seven Stages of Action**

```
             Intention to act
                   ↓
         Specification of action
                   ↓
           Execution of action          ← Gulf of Execution
                   ↓
             World state change
                   ↓
              Perception of world
                   ↓
             Interpretation
                   ↓
               Evaluation                 ← Gulf of Evaluation
```

---

### 4. Hypertext, Multimedia and WWW

| Concept               | Definition                                                                                                     | Characteristics / Issues in HCI                                                         |
|-----------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| **Hypertext**         | Non-linear text with embedded links (Ted Nelson, 1965)                                                        | Node-Link structure, disorientation (“lost in hyperspace”), cognitive overhead          |
| **Hypermedia**        | Hypertext + multimedia (text, graphics, audio, video)                                                          | Increases engagement but also cognitive load                                            |
| **World Wide Web**    | Global hypermedia system using HTTP, HTML, URLs                                                                | Client-server model, stateless protocol, navigation problems                           |
| **Back’s 7 Issues of Hypertext** | 1. Searching vs Browsing<br>2. Question asking problem<br>3. Cognitive overhead<br>4. Where am I?<br>5. How did I get here?<br>6. Where can I go?<br>7. Disorientation | Classic problems still relevant in modern web design                                    |
| **Multimedia Design Principles** | Use multiple channels wisely, avoid redundancy, ensure coherence (Mayer’s principles)                 | Temporal vs spatial contiguity, modality principle, redundancy principle               |

**Diagram – Basic Hypertext Structure**

```
       [Node A]
        /     \
       /       \
[Node B]     [Node C] ← bidirectional links
       \       /
        \     /
       [Node D]
```

---

### Summary Table (Quick Revision)

| Topic                                 | Key Models / Concepts                                 | Important Diagram / Rule                                      |
|---------------------------------------|-------------------------------------------------------|----------------------------------------------------------------|
| Cognitive Models                      | GOMS, KLM, Human Processor, HTA                       | Human Processor Model, Norman’s 7 stages                      |
| Socio-Organizational                 | Stakeholder conflicts, Participatory design           | Stakeholder triangle                                           |
| Communication & Collaboration        | Norman’s 7 stages, CSCW matrix                        | Gulf of Execution & Evaluation, 2×2 CSCW matrix                |
| Hypertext & WWW                       | Node-link model, Back’s 7 issues                      | Hypertext node-link diagram                                    |

Use these notes + diagrams for both theory exams and viva. All diagrams are standard and frequently asked in Anna University papers. Good luck! 🚀

---
