---
title: "Cognitive Computing Notes Units 1 & 2"
date: 2025-12-01
tags:
  - machine-learning
  - data-analysis
  - linux
  - obsidian
  - job-search
  - osint
  - research
  - creative
  - web-dev
  - game-design
source: qwen-export
model: qwen3-max-2025-10-20
---

# Cognitive Computing Notes Units 1 & 2

**Date:** 2025-12-01  
**Model:** `qwen3-max-2025-10-20`  
**Topics:** [[Machine-Learning]] · [[Data-Analysis]] · [[Linux]] · [[Obsidian]] · [[Job-Search]] · [[OSINT]] · [[Research]] · [[Creative]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

Here are **simple, exam-ready notes** for **Unit-1** and **Unit-2** of Cognitive Computing (as per your syllabus and provided material). Notes are short, point-wise, with easy language and diagrams (described in text form — you can draw them easily).

### UNIT-1: FOUNDATION OF COGNITIVE COMPUTING

#### 1. What is Cognitive Computing?
- Simulates **human thought process** using computers.
- Helps solve **complex, ambiguous, uncertain** problems.
- Does **not replace** humans → **augments (helps)** human intelligence.
- Works with **unstructured data** (text, images, voice) + structured data.

**Simple Definition**:  
"Cognitive Computing = Machines that think and learn like humans to help us make better decisions."

#### 2. Key Characteristics / Design Principles (Very Important)

| Principle           | Meaning                                                                 | Example                              |
|---------------------|-------------------------------------------------------------------------|--------------------------------------|
| **Adaptive**        | Learns & improves from new data automatically                          | Doctor AI updates with new research  |
| **Interactive**     | Talks naturally with humans & other systems                            | Chatbot asks questions to understand |
| **Iterative & Stateful** | Remembers past interactions, asks clarifying questions            | Remembers your preferences          |
| **Contextual**      | Understands time, place, user goal, meaning                             | Gives different answers based on location |

**Diagram to Draw**:
```
+----------------+     +------------------+     +------------------+
|   Adaptive     |<--->|   Interactive    |<--->| Iterative/Stateful|
+----------------+     +------------------+     +------------------+
         \                  /   \                     /
          \                /     \                   /
           \              /       \                 /
            \            /         \               /
             \          /           \             /
              \        /             \           /
               \      /               \         /
                \    /                 \       /
                 \  /                   \     /
                  \/                     \   /
               Contextual Understanding  \ /
                                          V
                                COGNITIVE SYSTEM
```

#### 3. How is Cognitive Computing Different from Traditional AI?

| Traditional AI / Programming       | Cognitive Computing                       |
|------------------------------------|-------------------------------------------|
| Follows fixed rules                | Learns and adapts                         |
| Works only on structured data      | Works on unstructured data (text, image)  |
| Gives one correct answer           | Gives options with confidence %           |
| Automates tasks                    | Helps humans make decisions               |

#### 4. What Makes a System "Cognitive"?

Three main abilities:
1. **Contextual Insight** → Understands situation
2. **Hypothesis Generation** → Gives possible answers with evidence
3. **Continuous Learning** → Keeps improving with new data

**Diagram**:
```
Data → Contextual Understanding → Generate Hypotheses → Learn & Improve → Answer with Evidence
```

#### 5. Artificial Intelligence as Foundation of Cognitive Computing
- AI started in 1950s (Alan Turing, Dartmouth Conference)
- Key idea: Can machines **think** and **learn** like humans?
- Technologies used:
  - Machine Learning
  - Neural Networks
  - Natural Language Processing (NLP)
  - Deep Learning

#### 6. Understanding Cognition (Human Thinking)
Two types of thinking (from psychology):

| System 1 (Fast)         | System 2 (Slow)             |
|-------------------------|-----------------------------|
| Automatic, intuitive    | Logical, analytical         |
| Quick decisions         | Solves hard problems        |
| Example: Recognizing face | Solving math problem      |

Cognitive systems combine both: Fast + Deep thinking

**Diagram**:
```
          +------------------+
          |    System 1      | ← Fast, Intuitive
          | (Automatic)      |
          +--------+---------+
                   ↑
             Check / Correct
                   ↓
          +--------+---------+
          |    System 2      | → Slow, Analytical
          | (Deliberate)     |
          +------------------+

     Together → Cognitive Computing
```

#### 7. Components of a Cognitive System (Architecture)

| Component                         | Job                                                      |
|-----------------------------------|----------------------------------------------------------|
| Corpus                            | Big storage of all knowledge (text, images, etc.)        |
| Machine Learning                  | Learns patterns from data                                |
| Hypothesis Generation & Scoring   | Gives possible answers + confidence score               |
| NLP & Processing                  | Understands language, images, voice                      |
| Presentation & Visualization      | Shows results using charts, graphs                       |

**Diagram** (Architecture Flow):
```
External Data → Corpus → Processing (NLP, ML) → Hypothesis → Visualization → User
```

### UNIT-2: NATURAL LANGUAGE PROCESSING (NLP) IN SUPPORT OF A COGNITIVE SYSTEM

#### 1. Role of NLP in Cognitive Systems
- Humans speak/write in **natural language** (English, Hindi, etc.)
- Computers understand only code
- NLP acts as a **translator** between humans and machines

**Main Jobs of NLP**:
- Understand meaning of text/speech
- Answer questions
- Summarize documents
- Translate languages
- Detect emotions (sentiment)

#### 2. Example: How NLP Works in Real Life
Question: “What’s the weather in Hyderabad tomorrow?”

**Steps NLP Does**:
1. **Tokenization** → Breaks into words
2. **NER** → Finds “Hyderabad” = Location, “tomorrow” = Time
3. **Intent Detection** → User wants weather forecast
4. **Answer Generation** → Gives reply in English

**Diagram**:
```
User: "What's the weather tomorrow in Hyderabad?"

       ↓ NLP Breaks it
[What’s] [the] [weather] [tomorrow] [in] [Hyderabad]

       ↓ Understands
Intent: Weather Forecast
Location: Hyderabad
Time: Tomorrow

       ↓ Gets data & replies
"Tomorrow in Hyderabad: 32°C, partly cloudy"
```

#### 3. Semantic Web
- Normal web = links between pages
- Semantic Web = links between **meaning**
- Machines can understand relationships like:
  - “Diabetes” → related to “Blood Sugar”, “Insulin”

#### 4. Knowledge Representation: Taxonomies and Ontologies

| Term         | Meaning                                    | Example                              |
|--------------|--------------------------------------------|--------------------------------------|
| **Taxonomy** | Simple hierarchy (tree structure)          | Animal → Mammal → Dog                |
| **Ontology** | Richer: defines objects + relationships    | Dog → hasOwner → Person              |
|              |                                            | Dog → treatsWith → Medicine          |

**Diagram** (Taxonomy vs Ontology):

```
Taxonomy (Simple Tree)          Ontology (With Relations)
       Animal                            Person
        /  \                              |  \
     Mammal Reptile                      owns treats
       |                                  |     |
      Dog -----------------------------→ Medicine
```

#### 5. Why Taxonomies & Ontologies are Important?
- Help machine understand **meaning**, not just words
- Enable reasoning:  
  If “Fever + Cough” → maybe “Flu”
- Used in medical, e-commerce, search engines

#### 6. Applying NLP to Business Problems
Examples:
- Customer care chatbots
- Summarizing long reports
- Sentiment analysis of reviews
- Fraud detection from text (banking)
- Medical diagnosis from doctor notes

**Summary Table – Unit 2**

| Topic                          | Key Point                                      |
|--------------------------------|------------------------------------------------|
| Role of NLP                    | Bridge between human language and machine      |
| Semantic Web                   | Web of meaning, not just links                 |
| Taxonomies                     | Simple classification (tree)                   |
| Ontologies                     | Classification + relationships                 |
| Business Use                   | Chatbots, sentiment, medical, fraud detection  |

**Quick Revision Tips**:
- Unit 1 → Focus on **4 design principles** + **components**
- Unit 2 → Focus on **NLP role** + **Taxonomy vs Ontology** + diagram

Draw the diagrams in your notes — they fetch extra marks in exams!

Let me know when you want **Unit 3, 4, 5** notes in the same simple format! Good luck for exams!

---
