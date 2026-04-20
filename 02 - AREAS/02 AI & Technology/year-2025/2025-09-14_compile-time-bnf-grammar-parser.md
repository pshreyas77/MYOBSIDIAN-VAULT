---
title: "Compile-Time BNF Grammar Parser"
date: 2025-09-14
tags:
  - geopolitics
  - research
  - creative
  - web-dev
  - game-design
source: claude-export
---

# Compile-Time BNF Grammar Parser

**Date:** 2025-09-14  
**Topics:** [[Geopolitics]] · [[Research]] · [[Creative]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

"Write a C++20 program that, at compile-time, parses a raw string literal containing a context-free grammar in BNF, then instantiates a `constexpr` parser which can validate any other compile-time string against that grammar, reporting syntax errors with line/column information; the entire compilation must abort with a clear diagnostic if the input string does not conform to the supplied grammar."

---

### 🤖 Claude

I'll create a C++20 compile-time BNF parser and validator. This is a complex metaprogramming challenge that pushes the boundaries of what's possible with constexpr evaluation.

{'type': 'text', 'text': 'OK', 'uuid': '87922815-2e90-485b-8164-f7ada7ea1417'}
This C++20 program implements a complete compile-time BNF parser and validator with the following key features:

## Core Components:

1. **Compile-Time String Handling**: `FixedString` template for handling string literals at compile time
2. **Position Tracking**: Tracks line/column information for error reporting
3. **Lexical Analysis**: `BNFLexer` tokenizes BNF grammar into tokens (identifiers, operators, strings)
4. **Grammar Parsing**: `BNFParser` builds an internal grammar representation from BNF tokens
5. **Input Validation**: `GrammarValidator` validates input strings against the parsed grammar

## Key Features:

- **Fully Constexpr**: Everything runs at compile-time using C++20 constexpr capabilities
- **Error Reporting**: Provides line/column information when validation fails
- **BNF Support**: Handles standard BNF notation with `::=`, `|`, parentheses, and string literals
- **Compilation Failure**: Uses `static_assert` to abort compilation with clear diagnostics on invalid input

## Usage:

The `VALIDATE_GRAMMAR` macro takes:
- A BNF grammar as a raw string literal
- The start rule name
- The input string to validate

If validation fails, compilation aborts with a clear error message pointing to the syntax error location.

## Example Grammars Included:

1. **Arithmetic Grammar**: Supports basic math expressions with operator precedence
2. **Programming Language Grammar**: Simple language with assignments and if statements

The implementation handles the complexity of recursive descent parsing entirely at compile-time, making it a powerful tool for compile-time validation of domain-specific languages or structured text formats.

To see the error reporting in action, uncomment the invalid example at the bottom - the compiler will halt with a clear diagnostic message.

---

### 🧑 You

make me an football type souls game  make it 3D

---

### 🤖 Claude

I'll create a 3D football-themed souls-like game using Three.js with challenging combat, stamina management, and atmospheric presentation.

---

### 🧑 You

Continue

---

### 🤖 Claude

{'type': 'text', 'text': 'OK', 'uuid': '28525948-a2be-4556-8671-e0bffa777562'}
I've created **Pitch Souls** - a 3D football-themed souls-like game! Here are the key features that make it a true souls experience:

## 🎮 Core Souls Mechanics:
- **Stamina Management**: Every action (sprinting, kicking, dashing) consumes stamina
- **Challenging Combat**: Enemies deal significant damage and require tactical positioning
- **Death & Respawn**: Classic "YOU DIED" screen with respawn mechanic (Press R)
- **Boss Battles**: Large, powerful boss enemies with special attacks and dedicated health bars

## ⚽ Football Integration:
- **Ball Combat**: Use the football as your primary weapon - kick it at enemies
- **Stadium Setting**: Play on a proper football pitch with goals and atmospheric lighting
- **Player Movement**: Football-style running, dashing, and ball control

## 🎯 Gameplay Features:
- **3D Environment**: Full 3D world with shadows, lighting, and atmospheric fog
- **Enemy AI**: Enemies chase both you and the ball, creating dynamic encounters
- **Physics System**: Realistic ball physics with bouncing, gravity, and momentum
- **Progressive Difficulty**: Boss spawns after time, more enemies appear after boss defeats

## 🕹️ Controls:
- **WASD**: Move around the pitch
- **Mouse**: Look around (first-person perspective)
- **Left Click**: Kick the football at enemies
- **Right Click**: Dash to evade attacks (costs stamina)
- **Space**: Jump
- **Shift**: Sprint (drains stamina faster)
- **R**: Respawn after death

## 🎨 Souls Atmosphere:
- Dark, moody lighting with dramatic stadium spotlights
- Ominous fog effects
- Classic souls UI with health/stamina bars
- Challenging, punishing gameplay that rewards skill

The game combines the tactical, stamina-based combat of Dark Souls with the unique mechanics of football. You must carefully manage your resources while using the ball as both a weapon and strategic tool. The 3D environment creates immersive encounters where positioning and timing are crucial for survival.

Click to lock the mouse cursor and start playing! The game gets progressively harder as bosses spawn and the field fills with more enemies.

---
