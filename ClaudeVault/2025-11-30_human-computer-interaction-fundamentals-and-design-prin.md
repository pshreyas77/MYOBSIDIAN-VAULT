---
title: "Human-computer interaction fundamentals and design principles"
date: 2025-11-30
tags:
  - sql
  - machine-learning
  - data-analysis
  - linux
  - job-search
  - history
  - philosophy
  - geopolitics
  - stock-market
  - osint
  - research
  - creative
  - web-dev
  - game-design
source: claude-export
---

# Human-computer interaction fundamentals and design principles

**Date:** 2025-11-30  
**Topics:** [[SQL]] · [[Machine-Learning]] · [[Data-Analysis]] · [[Linux]] · [[Job-Search]] · [[History]] · [[Philosophy]] · [[Geopolitics]] · [[Stock-Market]] · [[OSINT]] · [[Research]] · [[Creative]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

The Human: I/O channels, Memory, Reasoning and problem solving;
The computer: Devices, Memory, processing and networks;
Interaction: Models, frameworks, Ergonomics, styles, elements, interactivity- Paradigms. and Interactive Design: Basics, process, scenarios, navigation, screen design, Iteration and prototyping.
HCI in software process: Software life cycle, usability engineering, Prototyping in practice, design rationale.
Design rules: principles, standards, guidelines, rules. Evaluation Techniques, Universal Design. in HUMAN COMPUTER INTERACTION with diagrams take provided reference(make UNIT 1,2) notes

---

### 🤖 Claude

# HUMAN COMPUTER INTERACTION - COMPREHENSIVE NOTES

## UNIT 1: FOUNDATION OF HCI

---

## 1. THE HUMAN

### 1.1 INPUT-OUTPUT CHANNELS

Input-Output channels are the mediums through which information is exchanged between humans and computers.

#### **Human Input Channels (Senses)**

**1. Vision (Most Important)**
- Primary input channel for receiving information
- Processes text, images, icons, colors, and layouts
- Design considerations:
  - Visual angle and distance
  - Brightness and contrast
  - Color perception and legibility
  - Screen resolution

**2. Hearing**
- Supports interaction through:
  - System alerts and alarms
  - Speech recognition
  - Multimedia content
  - Audio feedback
- Ear detects pitch, loudness, and timbre

**3. Touch (Haptic)**
- Provides tactile feedback
- Critical for:
  - VR environments
  - Mobile devices
  - Accessibility tools (Braille displays)
  - Texture and pressure sensing

**4. Movement (Motor Control)**
- Controls interaction speed and accuracy
- Governed by Fitts' Law: Movement time depends on target size and distance
- Affects pointing, clicking, typing tasks

#### **Human Output Channels (Actions)**

- Speaking
- Hand movements
- Clicking and typing
- Gestures
- Eye movements

#### **Computer I/O Devices**

**Input Devices:**
- Keyboard, Mouse, Touchscreen
- Sensors, Microphones
- Cameras, Scanners

**Output Devices:**
- Monitor/Display
- Speakers
- Haptic feedback devices
- Printers

```
┌─────────────────────────────────────────────────┐
│         HUMAN-COMPUTER I/O CHANNEL              │
├─────────────────────────────────────────────────┤
│                                                 │
│  HUMAN                        COMPUTER          │
│                                                 │
│  INPUT (Senses)               INPUT DEVICES     │
│  ├─ Vision        ────────>   ├─ Monitor        │
│  ├─ Hearing       ────────>   ├─ Speakers       │
│  ├─ Touch         ────────>   ├─ Haptic Device  │
│  └─ Movement      ────────>   └─ Sensors        │
│                                                 │
│  OUTPUT (Actions)             OUTPUT DEVICES    │
│  ├─ Typing        ────────>   ├─ Keyboard       │
│  ├─ Clicking      ────────>   ├─ Mouse          │
│  ├─ Speaking      ────────>   ├─ Microphone     │
│  └─ Gestures      ────────>   └─ Touchscreen    │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

### 1.2 HUMAN MEMORY

Memory enables learning, interaction, and task performance but has limitations that directly affect usability.

#### **Types of Human Memory**

```
┌──────────────────────────────────────────────────┐
│            HUMAN MEMORY STRUCTURE                │
├──────────────────────────────────────────────────┤
│                                                  │
│  ┌─────────────────────────────────────────┐    │
│  │     SENSORY MEMORY                      │    │
│  │  • Duration: Milliseconds               │    │
│  │  • Iconic (visual)                      │    │
│  │  • Echoic (auditory)                    │    │
│  └──────────────┬──────────────────────────┘    │
│                 │                                │
│                 ▼                                │
│  ┌─────────────────────────────────────────┐    │
│  │   SHORT-TERM MEMORY (STM/Working)       │    │
│  │  • Capacity: 7±2 chunks (Miller's Law)  │    │
│  │  • Duration: 20-30 seconds              │    │
│  │  • Rapid decay without rehearsal        │    │
│  │  • Used for: Commands, menu recall      │    │
│  └──────────────┬──────────────────────────┘    │
│                 │                                │
│                 ▼                                │
│  ┌─────────────────────────────────────────┐    │
│  │    LONG-TERM MEMORY (LTM)               │    │
│  │  • Capacity: Unlimited                  │    │
│  │  • Duration: Lifelong (potentially)     │    │
│  │  • Types:                               │    │
│  │    - Episodic (events/experiences)      │    │
│  │    - Semantic (facts/concepts)          │    │
│  │    - Procedural (skills, e.g., typing)  │    │
│  └─────────────────────────────────────────┘    │
│                                                  │
└──────────────────────────────────────────────────┘
```

#### **Memory Experiments**

**Short-Term Memory (STM) Tests:**

1. **Digit Span Test**
   - Present random digit sequences (5-10 numbers)
   - Ask subjects to recall in order
   - Most recall 7 digits accurately; performance drops beyond

2. **Recency Effect**
   - Present word list, test immediate recall
   - Last few items remembered better (STM storage)
   - Delaying recall 30 seconds reduces effect

3. **Chunking Demonstration**
   - Compare: 198419991947 vs 1 9 8 4 1 9 9 9 1 9 4 7
   - Chunked sequences remembered more efficiently

**Long-Term Memory (LTM) Tests:**

1. **Recognition vs. Recall**
   - Present word list, test free recall later
   - Then test recognition (old + new words)
   - Recognition more accurate than recall

2. **Forgetting Curve (Ebbinghaus)**
   - Memorize nonsense syllables
   - Test at intervals (minutes, hours, days)
   - Shows rapid initial forgetting, then slower decay

3. **Interference Experiment**
   - Learn word list 1, then list 2
   - Recall of list 1 declines (retroactive interference)
   - Earlier knowledge disrupts new learning (proactive interference)

#### **HCI Design Implications**

✅ **Recognition over Recall**: Use menus/icons instead of command lines
✅ **Minimize STM Load**: Limit concurrent information display
✅ **Consistency**: Reinforce LTM through repeated patterns
✅ **Visual Cues**: Support memory with persistent visual information
✅ **Chunking**: Group related information (phone: 555-1234 not 5551234)

---

### 1.3 REASONING AND PROBLEM SOLVING

#### **Types of Reasoning**

**1. Deductive Reasoning**
- Logic-based, guarantees correctness if premises true
- Example: "All files in folder are images → This file is in folder → It must be an image"
- Useful in structured environments (databases, programming)

**2. Inductive Reasoning**
- Generalizes from specific cases to broader rules
- Example: "Clicking disk icon saves work → Disk symbol means save"
- Underpins learning through repeated exposure

**3. Abductive Reasoning**
- Infers most likely explanation
- Example: "Printer error → Likely paper jam (based on experience)"
- Common in troubleshooting

```
┌────────────────────────────────────────────────┐
│          REASONING TYPES IN HCI                │
├────────────────────────────────────────────────┤
│                                                │
│  DEDUCTIVE                                     │
│  General → Specific                            │
│  [Rule] → [Application]                        │
│  ├─ Logic-based                                │
│  └─ Used in: Programming, Databases            │
│                                                │
│  INDUCTIVE                                     │
│  Specific → General                            │
│  [Examples] → [Pattern]                        │
│  ├─ Pattern recognition                        │
│  └─ Used in: Learning interfaces               │
│                                                │
│  ABDUCTIVE                                     │
│  Observation → Best Explanation                │
│  [Error] → [Probable Cause]                    │
│  ├─ Hypothesis generation                      │
│  └─ Used in: Troubleshooting                   │
│                                                │
└────────────────────────────────────────────────┘
```

#### **Problem Solving Methods**

**1. Gestalt Theory**
- Reproductive: Using past knowledge
- Productive: Insightful restructuring
- Example: User realizes they must scroll to find Submit button (insight moment)

**2. Problem Space Theory (Newell & Simon)**

```
┌────────────────────────────────────────────────┐
│         PROBLEM SPACE THEORY                   │
├────────────────────────────────────────────────┤
│                                                │
│  ┌──────────────┐                              │
│  │ Initial State│                              │
│  │  (Problem)   │                              │
│  └───────┬──────┘                              │
│          │                                     │
│          │ [Apply Operators/Actions]           │
│          │                                     │
│          ▼                                     │
│  ┌──────────────┐                              │
│  │ Intermediate │                              │
│  │   States     │                              │
│  └───────┬──────┘                              │
│          │                                     │
│          │ [Heuristics: Means-Ends Analysis]   │
│          │                                     │
│          ▼                                     │
│  ┌──────────────┐                              │
│  │  Goal State  │                              │
│  │  (Solution)  │                              │
│  └──────────────┘                              │
│                                                │
└────────────────────────────────────────────────┘
```

- Defines: Initial state, Goal state, Legal operators
- Uses heuristics like means-ends analysis
- Example: Debugging code (current state: error → goal: working program)

**3. Analogical Reasoning**
- Maps solutions from familiar problems to new ones
- Example: Learning spreadsheet by analogy with paper ledgers

#### **HCI Applications**

- **Error Messages**: Support abductive reasoning with clear causes
- **Trial-and-Error**: Allow exploration for inductive learning
- **Tutorials**: Use familiar analogies
- **Feedback**: Provide structured feedback for deductive problem solving

---

### 1.4 MENTAL MODELS

**Definition:** Internal cognitive representations of how systems work, formed from experience, observation, and interaction.

#### **Nature of Mental Models**

- Created from past interactions with similar devices
- Can be accurate or inaccurate
- Simplify complex systems
- Influence usability even if not technically correct

```
┌────────────────────────────────────────────────┐
│        MENTAL MODEL ALIGNMENT                  │
├────────────────────────────────────────────────┤
│                                                │
│  USER'S MENTAL MODEL                           │
│  (How user thinks system works)                │
│         ↕                                      │
│    [Alignment]                                 │
│         ↕                                      │
│  DESIGNER'S MODEL                              │
│  (How designer intends system to work)         │
│         ↕                                      │
│    [Implementation]                            │
│         ↕                                      │
│  SYSTEM IMAGE                                  │
│  (Actual system behavior & interface)          │
│                                                │
│  GOAL: Minimize Gulf of Execution              │
│        & Gulf of Evaluation                    │
│                                                │
└────────────────────────────────────────────────┘
```

#### **Importance in Interface Design**

**1. Predictability**
- Good models enable anticipation of outcomes
- Example: Dragging file to folder → expected to move, not copy

**2. Learnability**
- Matching pre-existing models makes interfaces easier
- Example: Calculator app resembles physical calculator

**3. Error Reduction**
- Misaligned models cause errors
- Example: Hidden "Save" button → user assumes auto-save

**4. Consistency**
- Consistent metaphors reinforce models
- Example: "Undo" function expected across all software

**5. Adaptability**
- Models evolve with feedback
- Designers must provide cues for refinement

#### **Examples in HCI**

1. **Desktop Metaphor**
   - Folders, files, trash cans
   - Reflects real office environments
   - Helped transition from paper to digital

2. **Web Navigation**
   - Blue underlined text = hyperlink
   - Violating this confuses users

3. **Smartphones**
   - Swipe gesture for unlocking/deleting
   - Widely understood model

4. **Voice Assistants**
   - Users assume natural reasoning
   - Limitations break models → frustration

#### **Design Implications**

- Perform user studies to understand existing models
- Align system metaphors with user expectations
- Provide progressive disclosure for new models
- Use consistent feedback
- Test for mismatches (gulf of execution/evaluation)

---

## 2. THE COMPUTER

### 2.1 COMPUTER MEMORY

Computer memory parallels human memory but with technological differences.

```
┌────────────────────────────────────────────────┐
│        COMPUTER MEMORY HIERARCHY               │
├────────────────────────────────────────────────┤
│                                                │
│  ┌─────────────────────────────────────┐      │
│  │     REGISTERS                       │      │
│  │  • Fastest (nanoseconds)            │      │
│  │  • Smallest capacity (bytes)        │      │
│  └──────────────┬──────────────────────┘      │
│                 │                              │
│  ┌─────────────▼──────────────────────┐      │
│  │     CACHE MEMORY                    │      │
│  │  • Very fast                        │      │
│  │  • Small (KB to MB)                 │      │
│  └──────────────┬──────────────────────┘      │
│                 │                              │
│  ┌─────────────▼──────────────────────┐      │
│  │     RAM (Short-Term Memory)         │      │
│  │  • Volatile                         │      │
│  │  • Fast access (nanoseconds)        │      │
│  │  • Temporary storage (GB)           │      │
│  │  • Comparable to human STM          │      │
│  └──────────────┬──────────────────────┘      │
│                 │                              │
│  ┌─────────────▼──────────────────────┐      │
│  │   SECONDARY STORAGE (Long-Term)     │      │
│  │  • Non-volatile                     │      │
│  │  • Slower access (milliseconds)     │      │
│  │  • Permanent storage (TB)           │      │
│  │  • Types:                           │      │
│  │    - Hard Disks (HDD)               │      │
│  │    - Solid State Drives (SSD)       │      │
│  │    - Flash Memory                   │      │
│  │    - Optical Media (CD/DVD)         │      │
│  └─────────────────────────────────────┘      │
│                                                │
└────────────────────────────────────────────────┘
```

#### **Memory Types**

**1. RAM (Random Access Memory)**
- Temporary storage for active processes
- Volatile (data lost when power off)
- Fast access
- Comparable to human working memory

**2. Secondary Storage**
- Permanent storage (HDD, SSD, CD/DVD)
- Non-volatile
- Slower retrieval than RAM
- Massive capacity

**3. Flash Memory**
- Non-volatile
- Bridges RAM and disk memory
- Widely used in mobile devices, USB drives

**4. Data Compression & Standards**
- Compression reduces storage space
- Text encoding: ASCII, Unicode
- Video/Image compression: JPEG, MP4
- Ensures compatibility across systems

---

### 2.2 PROCESSING AND NETWORKS

#### **Processing in HCI**

Processing speed determines system responsiveness, directly affecting user experience.

**Slow Processing Issues:**
- Input buffering causes overshooting
- Variable response times create "icon wars" (multiple clicks trigger delayed responses)
- Frustration from delays

**Fast Processing Issues:**
- Information updates too quickly
- Users can't keep up (fast-scrolling text, real-time dashboards)

**Moore's Law:**
- Processor speeds historically doubled every 18 months
- System capabilities outpaced human cognitive limits
- Shifted HCI focus: managing information overload vs. scarcity

```
┌────────────────────────────────────────────────┐
│       PROCESSING SPEED vs USER PERCEPTION      │
├────────────────────────────────────────────────┤
│                                                │
│  Response Time         User Perception         │
│  ─────────────────────────────────────────     │
│  < 0.1 second         Instantaneous            │
│  0.1 - 1.0 second     Slight delay noticed     │
│  1.0 - 10 seconds     Flow disrupted           │
│  > 10 seconds         Task abandoned           │
│                                                │
│  DESIGN SOLUTIONS:                             │
│  • Progress indicators                         │
│  • Buffering messages                          │
│  • Animations during loading                   │
│  • Optimize critical paths                     │
│                                                │
└────────────────────────────────────────────────┘
```

#### **Networked Computing**

Modern systems rely on networks for communication, resource sharing, and collaboration.

**Impact on HCI:**
- Enables distributed systems
- Cloud services
- Real-time collaboration
- Latency, bandwidth, reliability affect satisfaction

**Network Limitations:**

```
┌────────────────────────────────────────────────┐
│         NETWORK BOTTLENECKS                    │
├────────────────────────────────────────────────┤
│                                                │
│  COMPUTATION-BOUND                             │
│  └─ Limited processor speed                    │
│                                                │
│  STORAGE-BOUND                                 │
│  └─ Disk read/write delays                     │
│                                                │
│  GRAPHICS-BOUND                                │
│  └─ Complex visual rendering                   │
│                                                │
│  NETWORK-BOUND                                 │
│  └─ Limited bandwidth in remote apps           │
│                                                │
└────────────────────────────────────────────────┘
```

**Design Implications:**
- Balance processing speed with human capabilities
- Delays > 1 second disrupt flow
- Use progress indicators
- Implement redundancy and error correction
- Provide feedback mechanisms

---

### 2.3 INPUT DEVICES

#### **Positioning Devices**

**1. Mouse**
- Most common device
- Relative movement controls cursor
- Efficient and precise for desktop

**2. Trackball**
- Stationary device, roll ball to move pointer
- Compact, suitable for limited space
- Used in specialized equipment

**3. Touchpad**
- Flat surface detecting finger movements
- Common in laptops
- Less precision than mouse

**4. Joystick**
- Multidirectional movement
- Used in gaming, simulations, CAD
- Fine control for continuous tasks

```
┌────────────────────────────────────────────────┐
│      INPUT DEVICE COMPARISON                   │
├────────────────────────────────────────────────┤
│                                                │
│  Device      Precision  Speed   Portability    │
│  ───────────────────────────────────────────   │
│  Mouse       High       High    Low            │
│  Trackball   High       Medium  Medium         │
│  Touchpad    Medium     Medium  High           │
│  Joystick    Medium     High    Low            │
│  Touchscreen Low        High    High           │
│  Stylus      Very High  Medium  Medium         │
│                                                │
└────────────────────────────────────────────────┘
```

#### **Pointing Devices**

**1. Light Pen**
- Pen-shaped device for CRT monitors
- High pointing accuracy
- Outdated technology

**2. Touchscreen**
- Direct pointing by touching display
- Smartphones, kiosks, tablets
- Intuitive but "fat-finger" problems

**3. Eyegaze Systems**
- Track eye movement
- Accessibility and hands-free environments
- Costly, sensitive to calibration

**4. Data Glove**
- Wearable device detecting hand/finger movements
- Virtual reality applications
- Gesture recognition

#### **Drawing Devices**

**1. Graphics Tablet & Stylus**
- Used by designers/artists
- High precision
- Pressure sensitivity

**2. Touchscreen with Pen Input**
- Modern tablets (iPad)
- Combines positioning and drawing

**3. 3D Input Devices**
- 3D styluses, motion sensors
- Modeling and VR
- Draw in three-dimensional space

#### **Text Entry Devices**

**1. Keyboard**
- Standard QWERTY layout
- Ergonomic variants (split keyboards)
- Most efficient for text input

**2. Virtual Keyboards**
- On touchscreens
- Flexible but slower than physical

**3. Speech Recognition**
- Converts speech to text
- Affected by noise and accents
- Reduces manual effort

**4. Handwriting Recognition**
- Stylus/pen input on tablets
- Natural writing
- Less accurate than typing

**5. Specialized Devices**
- Braille keyboards
- Chord keyboards

---

### 2.4 THREE-STATE MODEL (Buxton)

Explains how pointing devices operate through state transitions.

```
┌────────────────────────────────────────────────┐
│          THREE-STATE MODEL (BUXTON)            │
├────────────────────────────────────────────────┤
│                                                │
│  ┌──────────────────────────────┐             │
│  │   STATE 0: OUT OF RANGE      │             │
│  │                              │             │
│  │  • Device not controlling    │             │
│  │  • No input signal           │             │
│  │  • Example: Mouse lifted,    │             │
│  │    stylus above surface      │             │
│  └──────────┬───────────────────┘             │
│             │ [Enter Range]                    │
│             ▼                                  │
│  ┌──────────────────────────────┐             │
│  │   STATE 1: TRACKING          │             │
│  │                              │             │
│  │  • Device tracking movement  │             │
│  │  • No action applied yet     │             │
│  │  • Example: Moving mouse,    │             │
│  │    hovering stylus           │             │
│  └──────────┬───────────────────┘             │
│             │ [Press/Contact]                  │
│             ▼                                  │
│  ┌──────────────────────────────┐             │
│  │   STATE 2: DRAGGING          │             │
│  │                              │             │
│  │  • Actively engaged          │             │
│  │  • Button pressed/touching   │             │
│  │  • Example: Click-drag,      │             │
│  │    stylus drawing            │             │
│  └──────────────────────────────┘             │
│                                                │
└────────────────────────────────────────────────┘
```

**Applications:**
- GUI systems (select, move, resize)
- Drawing software (preview vs. actual drawing)
- Touchscreen interactions
- Gaming controllers

---

## 3. INTERACTION

### 3.1 MODELS OF INTERACTION

#### **Norman's Execution-Evaluation Cycle**

```
┌────────────────────────────────────────────────┐
│    NORMAN'S SEVEN STAGES OF ACTION             │
├────────────────────────────────────────────────┤
│                                                │
│  EXECUTION SIDE                                │
│  ├─ 1. Goal Formation                          │
│  │    (What do I want to accomplish?)          │
│  │                                             │
│  ├─ 2. Intention Formation                     │
│  │    (How will I do it?)                      │
│  │                                             │
│  ├─ 3. Action Specification                    │
│  │    (What actions are needed?)               │
│  │                                             │
│  └─ 4. Execution                               │
│       (Perform the action)                     │
│                                                │
│           ↓ [System Response]                  │
│                                                │
│  EVALUATION SIDE                               │
│  ├─ 5. Perception                              │
│  │    (What happened?)                         │
│  │                                             │
│  ├─ 6. Interpretation                          │
│  │    (What does it mean?)                     │
│  │                                             │
│  └─ 7. Evaluation                              │
│       (Did it work? Goal achieved?)            │
│                                                │
│  GULFS:                                        │
│  • Gulf of Execution (steps 1-4)               │
│  • Gulf of Evaluation (steps 5-7)              │
│                                                │
└────────────────────────────────────────────────┘
```

**Gulf of Execution:** Difficulty in expressing user's intention in system terms
**Gulf of Evaluation:** Difficulty in interpreting system's feedback

#### **Interaction Framework (Abowd & Beale)**

```
┌────────────────────────────────────────────────┐
│        INTERACTION FRAMEWORK                   │
├────────────────────────────────────────────────┤
│                                                │
│    USER                                        │
│     │                                          │
│     │ (Articulation)                           │
│     ▼                                          │
│    INPUT                                       │
│     │                                          │
│     │ (Performance)                            │
│     ▼                                          │
│   SYSTEM                                       │
│     │                                          │
│     │ (Presentation)                           │
│     ▼                                          │
│   OUTPUT                                       │
│     │                                          │
│     │ (Observation)                            │
│     ▼                                          │
│    USER                                        │
│                                                │
│  Four Translations:                            │
│  1. Articulation (User → Input)                │
│  2. Performance (Input → System)               │
│  3. Presentation (System → Output)             │
│  4. Observation (Output → User)                │
│                                                │
└────────────────────────────────────────────────┘
```

---

### 3.2 ERGONOMICS

**Definition:** Scientific study of designing systems to fit human capabilities and limitations.

#### **Types of Ergonomics**

```
┌────────────────────────────────────────────────┐
│         TYPES OF ERGONOMICS IN HCI             │
├────────────────────────────────────────────────┤
│                                                │
│  1. PHYSICAL ERGONOMICS                        │
│     • Body posture, movements                  │
│     • Hardware interaction                     │
│     • Examples: Keyboard layout, chair design  │
│     • Goal: Prevent musculoskeletal disorders  │
│                                                │
│  2. COGNITIVE ERGONOMICS                       │
│     • Mental processes                         │
│     • Perception, memory, reasoning            │
│     • Examples: Interface navigation, icons    │
│     • Goal: Reduce mental workload             │
│                                                │
│  3. ORGANIZATIONAL ERGONOMICS                  │
│     • Socio-technical systems                  │
│     • Work schedules, teamwork                 │
│     • Examples: Workflow design, collaboration │
│     • Goal: Optimize organizational systems    │
│                                                │
└────────────────────────────────────────────────┘
```

#### **Ergonomic Guidelines in HCI**

1. **Consistency** in layouts, fonts, colors
2. **Visibility** of important controls
3. **Affordance**: Objects suggest their use
4. **Fitts's Law**: Larger/closer targets easier to select
5. **Minimize Memory Load**: Recognition over recall
6. **Feedback & Error Prevention**
7. **Accessibility**: Accommodate disabilities

#### **Physical Ergonomics Factors**

**Workplace Setup:**
```
┌────────────────────────────────────────────────┐
│      ERGONOMIC WORKSTATION SETUP               │
├────────────────────────────────────────────────┤
│                                                │
│              ┌──────────┐                      │
│              │ Monitor  │  ← Eye level         │
│              │  20-26"  │     Arms length      │
│              └──────────┘     away             │
│                                                │
│    ┌─────────────────────────┐                │
│    │     Keyboard/Mouse      │  ← Elbow level │
│    └─────────────────────────┘                │
│                                                │
│    ┌─────────────────────────┐                │
│    │   Adjustable Chair      │  ← Back support│
│    │   Feet flat on floor    │     90° angles │
│    └─────────────────────────┘                │
│                                                │
└────────────────────────────────────────────────┘
```

**Health Factors:**
- Proper seating and back support
- Appropriate lighting (reduce glare)
- Noise reduction
- Temperature and ventilation
- Regular breaks

**Color and Display:**
- Colors align with conventions (red=danger, green=safe)
- Avoid overuse of blue (poor visibility)
- High contrast for readability
- Colorblind-friendly palettes

---

### 3.3 INTERACTION STYLES

```
┌────────────────────────────────────────────────┐
│          INTERACTION STYLES                    │
├────────────────────────────────────────────────┤
│                                                │
│  1. COMMAND LINE INTERFACE (CLI)               │
│     • User types textual commands              │
│     • Precise and powerful                     │
│     • High learning curve                      │
│     • For expert users                         │
│     • Example: SQL, Terminal                   │
│                                                │
│  2. MENU-BASED INTERFACE                       │
│     • Structured lists of options              │
│     • Recognition over recall                  │
│     • Clear hierarchy                          │
│     • Example: Drop-down menus, ribbons        │
│                                                │
│  3. DIRECT MANIPULATION                        │
│     • Visual representation of objects         │
│     • Drag-and-drop                            │
│     • Immediate feedback                       │
│     • Example: Desktop GUI, touch interfaces   │
│                                                │
│  4. FORM-BASED INTERFACE                       │
│     • Structured data entry                    │
│     • Guided input                             │
│     • Reduces errors                           │
│     • Example: Registration forms              │
│                                                │
│  5. NATURAL LANGUAGE INTERFACE                 │
│     • Text or voice communication              │
│     • Easy for novices                         │
│     • Accuracy depends on NLP                  │
│     • Example: Siri, Alexa, Chatbots           │
│                                                │
└────────────────────────────────────────────────┘
```

#### **Comparison of Interface Styles**

| Style | Ease of Use | Efficiency | Error Rate | Best For |
|-------|-------------|-----------|------------|----------|
| CLI | Low | High | High | Experts |
| Menu | High | Medium | Low | General users |
| Direct Manipulation | Very High | High | Low | Visual tasks |
| Forms | High | Medium | Low | Data entry |
| Natural Language | Very High | Medium | Medium | Casual users |

---

### 3.4 PARADIG

---

### 🧑 You

Continue

---

### 🤖 Claude

MS & INTERACTION ELEMENTS

#### **Interaction Paradigms**

**1. Desktop Computing**
- Windows, Icons, Menus, Pointers (WIMP)
- Keyboard + Mouse interaction
- Office/productivity focus

**2. Mobile Computing**
- Touch gestures
- Limited screen space
- Context-aware
- Mobile-first design

**3. Ubiquitous Computing**
- Embedded in environment
- Invisible interaction
- Context-sensitive
- IoT devices

**4. Virtual Reality (VR)**
- Immersive 3D environments
- Natural gestures
- Spatial interaction
- Head-mounted displays

**5. Augmented Reality (AR)**
- Digital overlay on real world
- Mixed reality experiences
- Contextual information
- Smart glasses

---

## UNIT 2: DESIGN & SOFTWARE PROCESS

---

## 4. INTERACTIVE DESIGN

### 4.1 BASICS OF INTERACTIVE DESIGN

**Definition:** Interactive design focuses on creating engaging interfaces with well-thought-out behaviors.

#### **Key Principles**

```
┌────────────────────────────────────────────────┐
│    INTERACTIVE DESIGN PRINCIPLES               │
├────────────────────────────────────────────────┤
│                                                │
│  1. USER-CENTERED                              │
│     Focus on user needs, not technology        │
│                                                │
│  2. FEEDBACK                                   │
│     System responds to every action            │
│                                                │
│  3. VISIBILITY                                 │
│     Functions clearly visible                  │
│                                                │
│  4. AFFORDANCE                                 │
│     Design suggests how to use                 │
│                                                │
│  5. CONSISTENCY                                │
│     Similar operations, similar behavior       │
│                                                │
│  6. CONSTRAINTS                                │
│     Limit possible actions to prevent errors   │
│                                                │
└────────────────────────────────────────────────┘
```

---

### 4.2 DESIGN PROCESS

```
┌────────────────────────────────────────────────┐
│         INTERACTIVE DESIGN PROCESS             │
├────────────────────────────────────────────────┤
│                                                │
│  ┌─────────────────────────────────┐          │
│  │  1. REQUIREMENTS ANALYSIS       │          │
│  │  • Interviews, surveys          │          │
│  │  • Identify user tasks/goals    │          │
│  │  • Define constraints           │          │
│  └──────────────┬──────────────────┘          │
│                 │                              │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  2. CONCEPTUAL DESIGN           │          │
│  │  • Develop mental models        │          │
│  │  • Create metaphors             │          │
│  │  • High-level structure         │          │
│  └──────────────┬──────────────────┘          │
│                 │                              │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  3. PROTOTYPING                 │          │
│  │  • Low/high fidelity            │          │
│  │  • Interactive mockups          │          │
│  │  • Early user feedback          │          │
│  └──────────────┬──────────────────┘          │
│                 │                              │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  4. EVALUATION                  │          │
│  │  • Usability testing            │          │
│  │  • Heuristic evaluation         │          │
│  │  • Performance metrics          │          │
│  └──────────────┬──────────────────┘          │
│                 │                              │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  5. IMPLEMENTATION              │          │
│  │  • Code development             │          │
│  │  • Interface consistency        │          │
│  │  • Accessibility                │          │
│  └──────────────┬──────────────────┘          │
│                 │                              │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  6. DEPLOYMENT & MAINTENANCE    │          │
│  │  • User feedback                │          │
│  │  • Updates and patches          │          │
│  │  • Continuous improvement       │          │
│  └─────────────────────────────────┘          │
│                                                │
│         [ITERATIVE CYCLE]                      │
│                                                │
└────────────────────────────────────────────────┘
```

---

### 4.3 SCENARIOS

**Definition:** Narrative descriptions of how users will interact with the system.

**Types of Scenarios:**

1. **Task Scenarios**
   - Describe specific user tasks
   - Step-by-step actions
   - Example: "User logs in, searches product, adds to cart, checks out"

2. **Use Case Scenarios**
   - More formal than task scenarios
   - Include preconditions, postconditions
   - Alternative flows

3. **User Stories**
   - Agile format: "As a [user], I want [goal] so that [benefit]"
   - Example: "As a student, I want to download lecture notes so that I can study offline"

**Benefits:**
- Concrete examples for design
- Facilitate communication
- Identify missing features
- Support evaluation

---

### 4.4 NAVIGATION DESIGN

#### **Principles of Good Navigation**

```
┌────────────────────────────────────────────────┐
│       NAVIGATION DESIGN PRINCIPLES             │
├────────────────────────────────────────────────┤
│                                                │
│  1. CONSISTENCY                                │
│     Uniform menus, labels, controls            │
│                                                │
│  2. VISIBILITY                                 │
│     Show current location and options          │
│                                                │
│  3. FEEDBACK                                   │
│     Indicate successful navigation             │
│     (highlight, breadcrumbs)                   │
│                                                │
│  4. FLEXIBILITY                                │
│     Support novices (menus) & experts          │
│     (shortcuts)                                │
│                                                │
│  5. ERROR TOLERANCE                            │
│     Allow undo, backtracking, recovery         │
│                                                │
│  6. CLEAR HIERARCHY                            │
│     Logical organization of content            │
│                                                │
└────────────────────────────────────────────────┘
```

#### **Navigation Aids**

- **Breadcrumbs**: Home > Products > Electronics > Phones
- **Search bars**: Quick access to content
- **Menus**: Hierarchical structure
- **Hyperlinks**: Direct connections
- **Site maps**: Overview of structure
- **Back/Forward buttons**: History navigation

---

### 4.5 SCREEN DESIGN

#### **Key Components**

```
┌────────────────────────────────────────────────┐
│          SCREEN LAYOUT STRUCTURE               │
├────────────────────────────────────────────────┤
│                                                │
│  ┌──────────────────────────────────────────┐ │
│  │         HEADER/TITLE BAR                 │ │
│  │  Logo | Navigation | Search | User       │ │
│  └──────────────────────────────────────────┘ │
│                                                │
│  ┌─────────┬────────────────────────────────┐ │
│  │         │                                │ │
│  │  SIDE   │     MAIN CONTENT AREA          │ │
│  │  MENU   │                                │ │
│  │  or     │  • Primary information         │ │
│  │  NAV    │  • User tasks                  │ │
│  │         │  • Interactive elements        │ │
│  │         │                                │ │
│  └─────────┴────────────────────────────────┘ │
│                                                │
│  ┌──────────────────────────────────────────┐ │
│  │           FOOTER                         │ │
│  │  Links | Copyright | Contact             │ │
│  └──────────────────────────────────────────┘ │
│                                                │
└────────────────────────────────────────────────┘
```

#### **Screen Design Principles**

**1. Clarity**
- Legible fonts
- Sufficient spacing
- High contrast
- Minimize visual noise

**2. Grouping**
- Related controls together
- Visual separation of sections
- Gestalt principles (proximity, similarity)

**3. Typography**
- Readable fonts (sans-serif for screen)
- Appropriate size (minimum 12pt)
- Limited font varieties (2-3 max)
- Proper line spacing

**4. Color Usage**
- Consistent color scheme
- Meaningful use (red=error, green=success)
- Accessibility (colorblind-friendly)
- Limited palette (3-5 primary colors)

**5. Controls Placement**
- Frequently used: easily accessible
- Sequential flow: left-to-right, top-to-bottom
- Action buttons: consistent location
- Primary action: prominent

**6. Feedback Elements**
- Progress indicators
- Status messages
- Error alerts
- Confirmation dialogs
- Tooltips

**7. Whitespace**
- Improves readability
- Reduces cognitive load
- Creates visual hierarchy
- Professional appearance

---

### 4.6 ITERATION AND PROTOTYPING

#### **Types of Prototypes**

```
┌────────────────────────────────────────────────┐
│          TYPES OF PROTOTYPES                   │
├────────────────────────────────────────────────┤
│                                                │
│  1. LOW-FIDELITY                               │
│     ├─ Paper sketches                          │
│     ├─ Wireframes                              │
│     ├─ Storyboards                             │
│     ├─ Quick and cheap                         │
│     └─ Early concept validation                │
│                                                │
│  2. MEDIUM-FIDELITY                            │
│     ├─ Digital wireframes                      │
│     ├─ Interactive mockups                     │
│     ├─ Basic functionality                     │
│     └─ Tool: Figma, Balsamiq                   │
│                                                │
│  3. HIGH-FIDELITY                              │
│     ├─ Realistic appearance                    │
│     ├─ Full interactivity                      │
│     ├─ Detailed functionality                  │
│     └─ Near-final product                      │
│                                                │
└────────────────────────────────────────────────┘
```

#### **Prototyping Approaches**

**1. Throwaway/Rapid Prototyping**
- Built quickly for exploration
- Discarded after evaluation
- Used to clarify requirements
- Example: Paper prototypes for user feedback

**2. Evolutionary Prototyping**
- Continuously refined
- Becomes final product
- Incremental improvements
- Example: Agile development sprints

**3. Incremental Prototyping**
- System built in parts
- Each increment adds functionality
- Parallel development possible
- Example: Module-by-module development

#### **Iteration Cycle**

```
┌────────────────────────────────────────────────┐
│           ITERATIVE DESIGN CYCLE               │
├────────────────────────────────────────────────┤
│                                                │
│         Design → Prototype → Test              │
│           ↑                      │             │
│           │                      ▼             │
│           └──── Refine ←─── Evaluate           │
│                                                │
│  Each iteration:                               │
│  • Improves design                             │
│  • Incorporates user feedback                  │
│  • Reduces usability issues                    │
│  • Converges toward optimal solution           │
│                                                │
└────────────────────────────────────────────────┘
```

**Benefits of Iteration:**
- Early error detection
- User involvement
- Flexibility to changes
- Reduced development risk
- Better final product

---

## 5. HCI IN SOFTWARE PROCESS

### 5.1 SOFTWARE LIFE CYCLE MODELS

#### **5.1.1 Waterfall Model**

```
┌────────────────────────────────────────────────┐
│           WATERFALL MODEL                      │
├────────────────────────────────────────────────┤
│                                                │
│  ┌─────────────────────────────────┐          │
│  │  1. Requirement Analysis        │          │
│  │     • Gather requirements       │          │
│  │     • SRS document              │          │
│  └──────────────┬──────────────────┘          │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  2. System Design               │          │
│  │     • Architecture              │          │
│  │     • HLD/LLD documents         │          │
│  └──────────────┬──────────────────┘          │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  3. Implementation              │          │
│  │     • Coding                    │          │
│  │     • Unit testing              │          │
│  └──────────────┬──────────────────┘          │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  4. Integration & Testing       │          │
│  │     • System testing            │          │
│  │     • Bug detection             │          │
│  └──────────────┬──────────────────┘          │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  5. Deployment                  │          │
│  │     • Installation              │          │
│  │     • User training             │          │
│  └──────────────┬──────────────────┘          │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  6. Maintenance                 │          │
│  │     • Bug fixes                 │          │
│  │     • Updates                   │          │
│  └─────────────────────────────────┘          │
│                                                │
│  Sequential: No backward flow                  │
│                                                │
└────────────────────────────────────────────────┘
```

**Advantages:**
- Simple and easy to understand
- Clear milestones
- Good documentation
- Suitable for stable requirements

**Disadvantages:**
- Rigid and inflexible
- Late discovery of design flaws
- No early user involvement
- Poor for evolving needs

---

#### **5.1.2 Prototyping Model**

```
┌────────────────────────────────────────────────┐
│         PROTOTYPING MODEL                      │
├────────────────────────────────────────────────┤
│                                                │
│  ┌─────────────────────────────────┐          │
│  │  1. Requirements Gathering      │          │
│  │     (Initial, not detailed)     │          │
│  └──────────────┬──────────────────┘          │
│                 │                              │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  2. Quick Design                │          │
│  │     (UI focus, simple design)   │          │
│  └──────────────┬──────────────────┘          │
│                 │                              │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  3. Build Prototype             │ │
│  │     (Working model)             │          │
│  └──────────────┬──────────────────┘          │
│                 │                              │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  4. Customer Evaluation         │          │
│  │     (Feedback collection)       │          │
│  └──────────────┬──────────────────┘          │
│                 │                              │
│            ┌────┴────┐                         │
│            │         │                         │
│       Acceptable  Needs Refinement             │
│            │         │                         │
│            │         └──> Back to Step 2       │
│            │           (Iteration Loop)        │
│            ▼                                   │
│  ┌─────────────────────────────────┐          │
│  │  5. Final System Development    │          │
│  │     (Using standard SDLC)       │          │
│  └──────────────┬──────────────────┘          │
│                 │                              │
│                 ▼                              │
│  ┌─────────────────────────────────┐          │
│  │  6. Deployment & Maintenance    │          │
│  └─────────────────────────────────┘          │
│                                                │
└────────────────────────────────────────────────┘
```

**Advantages:**
- Requirements clarified early
- Reduces risk of failure
- Active user participation
- Early error detection
- High user satisfaction

**Disadvantages:**
- Scope creep risk
- Time-consuming iterations
- Poor quality prototype may mislead
- May reduce documentation focus

---

### 5.2 USABILITY ENGINEERING

**Definition:** Systematic approach to designing usable systems through measurement and testing.

#### **Usability Metrics**

```
┌────────────────────────────────────────────────┐
│          USABILITY METRICS                     │
├────────────────────────────────────────────────┤
│                                                │
│  1. EFFECTIVENESS                              │
│     • Task completion rate                     │
│     • Accuracy of results                      │
│     • Error frequency                          │
│                                                │
│  2. EFFICIENCY                                 │
│     • Time to complete tasks                   │
│     • Steps required                           │
│     • Resource utilization                     │
│                                                │
│  3. SATISFACTION                               │
│     • User ratings                             │
│     • Subjective feedback                      │
│     • Willingness to use again                 │
│                                                │
│  4. LEARNABILITY                               │
│     • Time to learn system                     │
│     • Training requirements                    │
│     • Retention over time                      │
│                                                │
│  5. MEMORABILITY                               │
│     • Ease of remembering                      │
│     • Return user performance                  │
│     • Command recall                           │
│                                                │
└────────────────────────────────────────────────┘
```

#### **Usability Engineering Process**

1. **Know the User**
   - User profiles
   - Task analysis
   - Context of use

2. **Competitive Analysis**
   - Study similar systems
   - Identify best practices
   - Learn from competitors' mistakes

3. **Set Usability Goals**
   - Specific, measurable targets
   - Example: "90% task completion in < 2 minutes"

4. **Participatory Design**
   - Involve users in design
   - Iterative feedback

5. **Usability Testing**
   - Observe real users
   - Collect quantitative/qualitative data

6. **Iterative Design**
   - Refine based on testing
   - Continuous improvement

---

### 5.3 DESIGN RATIONALE

**Definition:** Explicit documentation of reasons behind design decisions.

**Why Document Design Rationale?**
- Helps future designers understand choices
- Supports modification and evolution
- Prevents repeating past mistakes
- Justifies decisions to stakeholders

**Methods:**

1. **Design Space Analysis**
   - Explore alternative designs
   - Document trade-offs
   - Justify selection

2. **Question, Option, Criteria (QOC)**
```
Question: How should users navigate?
  ├─ Option 1: Menu-based
  │   └─ Criteria: Easy for novices, slower for experts
  ├─ Option 2: Command-line
  │   └─ Criteria: Fast for experts, steep learning curve
  └─ Option 3: Hybrid (menu + shortcuts)
      └─ Criteria: Flexible, supports all users [SELECTED]
```

3. **Issue-Based Information System (IBIS)**
   - Issue → Position → Argument
   - Debate-style documentation

---

## 6. DESIGN RULES

### 6.1 PRINCIPLES

**Shneiderman's Eight Golden Rules:**

```
┌────────────────────────────────────────────────┐
│      SHNEIDERMAN'S GOLDEN RULES                │
├────────────────────────────────────────────────┤
│                                                │
│  1. STRIVE FOR CONSISTENCY                     │
│     • Uniform commands, fonts, layouts         │
│     • Reduces confusion                        │
│                                                │
│  2. ENABLE UNIVERSAL USABILITY                 │
│     • Accessibility for all users              │
│     • Beginners, experts, disabled             │
│                                                │
│  3. OFFER INFORMATIVE FEEDBACK                 │
│     • Immediate response to actions            │
│     • Users feel in control                    │
│                                                │
│  4. DESIGN DIALOGS TO YIELD CLOSURE            │
│     • Clear beginnings, middles, ends          │
│     • Confirmation screens                     │
│                                                │
│  5. PREVENT ERRORS & ALLOW RECOVERY            │
│     • Constraints, error messages              │
│     • Undo options                             │
│                                                │
│  6. PERMIT EASY REVERSAL OF ACTIONS            │
│     • Undo/Redo functionality                  │
│     • Reduces anxiety                          │
│                                                │
│  7. SUPPORT INTERNAL LOCUS OF CONTROL          │
│     • Users direct the system                  │
│     • Not vice versa                           │
│                                                │
│  8. REDUCE SHORT-TERM MEMORY LOAD              │
│     • Recognition over recall                  │
│     • Menus instead of commands                │
│                                                │
└────────────────────────────────────────────────┘
```

**Nielsen's 10 Usability Heuristics:**

1. Visibility of system status
2. Match between system and real world
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, and recover from errors
10. Help and documentation

---

### 6.2 STANDARDS

**Definition:** Official guidelines and regulations that must be followed.

**Types:**

1. **ISO Standards**
   - ISO 9241: Ergonomics of human-system interaction
   - ISO 14915: Multimedia user interfaces

2. **WCAG (Web Content Accessibility Guidelines)**
   - Perceivable
   - Operable
   - Understandable
   - Robust

3. **Industry Standards**
   - Apple Human Interface Guidelines
   - Google Material Design
   - Microsoft Fluent Design

---

### 6.3 GUIDELINES

**Definition:** Recommended practices, more flexible than standards.

**Examples:**

- Use clear, concise language
- Provide helpful error messages
- Group related items together
- Use familiar icons and metaphors
- Maintain consistent navigation
- Optimize loading times
- Support keyboard shortcuts

---

### 6.4 RULES

**Definition:** Specific, context-dependent directives.

**Examples:**

- "Save" button always bottom-right
- Red color for destructive actions
- Maximum 7±2 menu items
- Button labels: verb phrases
- Error messages: explain cause and solution

---

## 7. EVALUATION TECHNIQUES

### 7.1 ANALYTICAL EVALUATION (Without Users)

#### **7.1.1 Heuristic Evaluation**

**Process:**
1. 3-5 usability experts
2. Evaluate interface against heuristics
3. Identify violations
4. Rate severity (0-4 scale)
5. Consolidate findings

**Severity Ratings:**
- 0: Not a usability problem
- 1: Cosmetic problem
- 2: Minor usability problem
- 3: Major usability problem
- 4: Usability catastrophe

#### **7.1.2 Cognitive Walkthrough**

**Process:**
```
For each task step:
  └─ Will the user know what to do?
  └─ Will the user see the control?
  └─ Will the user recognize it as correct action?
  └─ Will the user understand feedback?
```

**Focus:** First-time users, learnability

#### **7.1.3 GOMS Model**

- **G**oals: What user wants to achieve
- **O**perators: Basic actions (click, type)
- **M**ethods: Procedures to achieve goals
- **S**election rules: Choosing between methods

**Used for:** Predicting task completion time

---

### 7.2 EMPIRICAL EVALUATION (With Users)

#### **7.2.1 Usability Testing**

```
┌────────────────────────────────────────────────┐
│        USABILITY TESTING PROCESS               │
├────────────────────────────────────────────────┤
│                                                │
│  1. PLANNING                                   │
│     • Define objectives                        │
│     • Select participants                      │
│     • Design tasks                             │
│                                                │
│  2. PREPARATION                                │
│     • Setup environment                        │
│     • Prepare materials                        │
│     • Brief participants                       │
│                                                │
│  3. TESTING                                    │
│     • Observe users                            │
│     • Record metrics                           │
│     • Take notes                               │
│                                                │
│  4. ANALYSIS                                   │
│     • Identify patterns                        │
│     • Calculate metrics                        │
│     • Prioritize issues                        │
│                                                │
│  5. REPORTING                                  │
│     • Document findings                        │
│     • Recommend solutions                      │
│     • Present to stakeholders                  │
│                                                │
└────────────────────────────────────────────────┘
```

**Data Collected:**
- Task completion rate
- Time on task
- Error count
- User satisfaction ratings
- Qualitative feedback

#### **7.2.2 Think-Aloud Protocol**

- Users verbalize thoughts while performing tasks
- Reveals cognitive processes
- Identifies confusions and expectations

#### **7.2.3 Field Studies**

- Observe users in natural environment
- Identify real-world issues
- Contextual understanding

#### **7.2.4 Surveys & Questionnaires**

**Common Instruments:**
- **SUS (System Usability Scale)**: 10-item questionnaire
- **SUMI (Software Usability Measurement Inventory)**
- **Custom surveys**: Task-specific questions

#### **7.2.5 A/B Testing**

- Compare two design versions
- Measure performance differences
- Data-driven decisions

---

## 8. UNIVERSAL DESIGN

### 8.1 SEVEN PRINCIPLES OF UNIVERSAL DESIGN

```
┌────────────────────────────────────────────────┐
│    UNIVERSAL DESIGN PRINCIPLES                 │
├────────────────────────────────────────────────┤
│                                                │
│  1. EQUITABLE USE                              │
│     • Accessible to diverse abilities          │
│     • Example: Ramps + stairs                  │
│                                                │
│  2. FLEXIBILITY IN USE                         │
│     • Multiple ways to perform tasks           │
│     • Example: Touch, voice, keyboard          │
│                                                │
│  3. SIMPLE AND INTUITIVE                       │
│     • Reduce complexity                        │
│     • Example: Universal icons                 │
│                                                │
│  4. PERCEPTIBLE INFORMATION                    │
│     • Effective regardless of sensory ability  │
│     • Example: Subtitles, vibration alerts     │
│                                                │
│  5. TOLERANCE FOR ERROR                        │
│     • Anticipate mistakes                      │
│     • Example: Undo, trash folder              │
│                                                │
│  6. LOW PHYSICAL EFFORT                        │
│     • Minimize fatigue                         │
│     • Example: Auto-fill, shortcuts            │
│                                                │
│  7. SIZE AND SPACE FOR USE                     │
│     • Proper spacing for all users             │
│     • Example: Large touch targets             │
│                                                │
└────────────────────────────────────────────────┘
```

### 8.2 ACCESSIBILITY CONSIDERATIONS

**Visual Impairments:**
- Screen readers
- High contrast modes
- Scalable text
- Alt text for images

**Hearing Impairments:**
- Captions and transcripts
- Visual alerts
- Sign language support

**Motor Impairments:**
- Keyboard navigation
- Large click targets
- Voice control
- Switch access

**Cognitive Disabilities:**
- Simple language
- Clear instructions
- Consistent layouts
- Error prevention

---

## 9. SUMMARY DIAGRAMS

### Overall HCI Design Framework

```
┌──────────────────────────────────────────────────────────┐
│              HCI DESIGN FRAMEWORK                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  UNDERSTAND USERS            DESIGN SOLUTIONS            │
│  ├─ I/O Channels            ├─ Interactive Design       │
│  ├─ Memory                  ├─ Prototyping              │
│  ├─ Reasoning               ├─ Screen Design            │
│  └─ Mental Models           └─ Navigation               │
│                                                          │
│           ↓                           ↓                  │
│                                                          │
│  APPLY PRINCIPLES            EVALUATE DESIGNS            │
│  ├─ Golden Rules             ├─ Heuristic Evaluation    │
│  ├─ Standards                ├─ Usability Testing       │
│  ├─ Guidelines               ├─ Cognitive Walkthrough   │
│  ├─ Ergonomics               └─ Field Studies           │
│  └─ Universal Design                                     │
│                                                          │
│           ↓                           ↓                  │
│                                                          │
│          ITERATE & REFINE                                │
│          └─ Continuous Improvement                       │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## END OF UNIT 1 & 2 NOTES

**Key Takeaways:**

✅ **Unit 1:** Understand human capabilities (I/O, memory, reasoning) and computer components (devices, memory, processing) to design effective interactions

✅ **Unit 2:** Follow systematic design processes, use prototyping, apply design principles, and evaluate thoroughly for usable systems

✅ **Core Philosophy:** User-centered design with iterative refinement based on evaluation

---

These comprehensive notes cover Units 1 and 2 with diagrams, detailed explanations, and practical examples for Human Computer Interaction. Use these for exam preparation and project work!

---
