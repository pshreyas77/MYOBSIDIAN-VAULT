---
title: "Creating a fun retro game prompt"
date: 2026-02-27
tags:
  - machine-learning
  - llm-ai
  - data-analysis
  - linux
  - geopolitics
  - stock-market
  - creative
  - web-dev
  - game-design
source: claude-export
---

# Creating a fun retro game prompt

> **Conversation Overview**

The person asked Claude to create a detailed game design prompt for a fun, innovative retro-style browser game. Claude produced a comprehensive game design document for a concept called "GlitchBound" — a pixel-art platformer where the player is a rogue AI trapped in a corrupted arcade machine. The core mechanic centers on a "Glitch Gun" that intentionally corrupts the environment to create pathways, with a corruption meter, escape sequences, and reactive chiptune music. The design document covered visual style, gameplay loop, enemy types, innovative features, and a suggested tech stack.

The person then asked Claude to build a fully playable browser prototype directly. Claude generated a complete single-file HTML/JavaScript game called GlitchBound, featuring three levels with distinct themes (Boot Sequence, Memory Leak, Boss Fight), pixel-art rendering with a CRT scanline overlay, procedural chiptune audio via Web Audio API, multiple enemy types (Debuggers, Loop Ghosts, a Boss), collectible gems, a corruption system with escape countdowns, screen shake, particle effects, RGB glitch visuals, and keyboard controls. The game was delivered as a self-contained HTML file.

Following delivery of the prototype, the person asked only for a list of enhancement prompts they could use optionally. Claude provided six ready-to-paste prompts covering: improved chiptune music, mobile touch controls, additional levels, cinematic story screens, power-ups, and a high score leaderboard. The person acknowledged with "ok," and Claude confirmed the prompts were available whenever needed. No corrections or preference instructions were given during the conversation.

**Date:** 2026-02-27  
**Topics:** [[Machine-Learning]] · [[LLM-AI]] · [[Data-Analysis]] · [[Linux]] · [[Geopolitics]] · [[Stock-Market]] · [[Creative]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

write me an prompt to make an fun game like an retro game it should to fun and innovative from other in detail to built it

---

### 🤖 Claude

Here's a detailed prompt you can use to build a fun, innovative retro-style game:

---

## 🎮 Master Prompt: "GlitchBound" — A Retro Puzzle-Action Game

**Concept:**
Build a retro-pixel-art game called **GlitchBound** where the player is a rogue AI trapped inside a corrupted arcade machine. The twist: the game world itself is "breaking" — levels glitch, flip, invert, or partially disappear as you play, and you must *exploit* these glitches to progress rather than fear them.

---

**Core Mechanic (What Makes It Unique):**

The player has a **"Glitch Gun"** — instead of shooting enemies, you shoot *the environment* to intentionally corrupt it:

- Shoot a wall → it flickers and becomes passable for 3 seconds
- Shoot a platform → it duplicates or flips upside down
- Shoot an enemy → it glitches into a helper or obstacle randomly
- Shoot the background → hidden paths appear from corrupted pixels

This turns traditional platformer logic on its head — destruction is your tool, not your enemy.

---

**Visual Style:**
- CRT scanline filter with RGB color bleeding
- 16-bit pixel art with intentional "corruption" animations (pixels scrambling, color palette swaps)
- Glitch transitions between levels — screen tears, memory dump text, fake "error" screens that are actually part of the level
- Neon green, electric blue, and hot pink as dominant colors on a dark background

---

**Gameplay Loop:**

Each level is a self-contained "corrupted program" with 3 phases:

1. **Explore** — Navigate a normal-looking level that slowly starts breaking
2. **Exploit** — Use the Glitch Gun creatively to open paths (multiple solutions per level)
3. **Escape** — A 30-second countdown where the entire level visually collapses while you run to the exit

---

**Innovative Features to Build In:**

- **Glitch Memory System** — Each glitch you create is "remembered." In later levels, past glitches bleed through as ghost platforms or phantom enemies from earlier stages
- **Corruption Meter** — The more you glitch, the more unstable the world gets. High corruption = harder enemies but more secret paths
- **Randomized Glitch Events** — Every 60 seconds, a random event fires: gravity flips, screen inverts, a second player ghost appears mimicking your past moves
- **Chiptune Soundtrack that Reacts** — Music degrades and glitches in sync with the corruption meter (add distortion, drop instruments, reverse loops)
- **Hidden "Clean" Rooms** — Secret areas with NO glitching and perfect pixel art, acting as lore drops and safe zones

---

**Enemies:**
- **Debuggers** — Enemies that try to "fix" your glitches and close the paths you open
- **Loop Ghosts** — Enemies stuck in infinite animation loops that block paths rhythmically
- **Bosses** — Each boss IS a corrupted game mechanic (e.g., a boss that IS the scrolling background, one that IS the HUD)

---

**Tech Stack Suggestion (for building):**
- **Engine:** Unity or Godot (Godot is great for 2D pixel games)
- **Rendering:** Custom CRT shader + pixel-perfect camera
- **Audio:** SFXR or BeepBox for chiptune + Audacity for glitch audio effects
- **Tilemap:** LDtk or Tiled for level design

---

**Tone & Feel:**
Think *Undertale* meets *Pony Island* meets *Hotline Miami* — self-aware, slightly creepy, bursting with personality, and rewarding to players who experiment and break the rules.

---

Use this prompt as your game design document foundation. Want me to build a **playable prototype** of this directly in the browser right now?

---

### 🧑 You

Yes! If you want to enhance this prototype, here's what would make the biggest impact:
## High Priority Assets
**1. Pixel Art Sprites**
- Player character sprite sheet (16x24 or 24x32 pixels, 4-frame walk cycle)
- Enemy sprites (debuggers, loop ghosts, boss)
- Tileset (walls, platforms, corrupted variants)
- Format: PNG or base64 encoded image
**2. Chiptune Music**
- A looping .mp3 or .ogg track for background music
- Ideally something that can "degrade" (I can add distortion effects via Web Audio API)
**3. Level Designs**
- More levels in the format I used, or describe layouts you'd like
- Any specific puzzle ideas with the glitch mechanic
## Optional Enhancements
**4. Sound Effects**
- Pre-made glitch sounds, jumps, collection sounds (can be .wav/.mp3 or I can keep procedural)
**5. Story/Lore Text**
- Secret "clean room" messages
- Error screen text
- Anything you want the corrupted arcade machine to "say"
**6. Color Scheme Tweaks**
- If you have specific hex colors in mind for the palette
---
If you provide any of these, I'll integrate them into the game. Just paste images as base64, upload audio files, or describe text/levels and I'll code them in.
What would you like to contribute?

---

### 🤖 Claude

{'type': 'text', 'text': '     1\t---\n     2\tname: frontend-design\n     3\tdescription: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.\n     4\tlicense: Complete terms in LICENSE.txt\n     5\t---\n     6\t\n     7\tThis skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.\n     8\t\n     9\tThe user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.\n    10\t\n    11\t## Design Thinking\n    12\t\n    13\tBefore coding, understand the context and commit to a BOLD aesthetic direction:\n    14\t- **Purpose**: What problem does this interface solve? Who uses it?\n    15\t- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.\n    16\t- **Constraints**: Technical requirements (framework, performance, accessibility).\n    17\t- **Differentiation**: What makes this UNFORGETTABLE? What\'s the one thing someone will remember?\n    18\t\n    19\t**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.\n    20\t\n    21\tThen implement working code (HTML/CSS/JS, React, Vue, etc.) that is:\n    22\t- Production-grade and functional\n    23\t- Visually striking and memorable\n    24\t- Cohesive with a clear aesthetic point-of-view\n    25\t- Meticulously refined in every detail\n    26\t\n    27\t## Frontend Aesthetics Guidelines\n    28\t\n    29\tFocus on:\n    30\t- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend\'s aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.\n    31\t- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.\n    32\t- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.\n    33\t- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.\n    34\t- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.\n    35\t\n    36\tNEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.\n    37\t\n    38\tInterpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.\n    39\t\n    40\t**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.\n    41\t\n    42\tRemember: Claude is capable of extraordinary creative work. Don\'t hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.\n    43\t', 'uuid': '2c6d825b-b327-449b-9c9b-5dbd813b988c'}
I'll build you the full **GlitchBound** prototype right now — a complete playable browser game with everything baked in!

{'type': 'text', 'text': 'File created successfully: /mnt/user-data/outputs/glitchbound.html', 'uuid': 'abb5d14d-323d-4d6e-a7f1-79843589af2d'}

{'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/glitchbound.html', 'name': 'glitchbound', 'mime_type': 'text/html', 'uuid': 'ec432037-8c47-421e-b1c2-bfed4a1c1f28'}
**GlitchBound is ready to play!** 🎮

Here's everything packed into this prototype:

**Gameplay**
- 3 full levels: Boot Sequence → Memory Leak → Boss Fight
- **Glitch Gun** (F or Z) — shoot walls to make them passable for ~2 seconds, shoot enemies to corrupt them
- **Corruption meter** — fills as you glitch. At 80%, escape mode triggers with a countdown timer
- **Random glitch events** fire mid-level: ghost mode, memory dumps, speed boosts, screen tears

**Enemies**
- **Debuggers** — patrol enemies that actively restore your glitched tiles
- **Loop Ghosts** — floating patrol enemies that phase through the air
- **Boss** — a massive chaser with an HP bar in Level 3

**Feel**
- CRT scanline overlay with vignette + green border
- Procedural chiptune that degrades with corruption level
- RGB color-shift bullets, particle effects, screen shake
- Pixel-art player with walk animation and gun arm

**Controls:** `WASD` / `Arrow Keys` — Move | `Space` — Jump | `F` or `Z` — Glitch Gun

---

### 🧑 You

give me only prompt to add if anything required

---

### 🤖 Claude

Here are focused enhancement prompts you can paste directly into the chat:

---

**🎵 Better Music**
```
Add a proper chiptune melody using Web Audio API. Create a 8-bar looping bassline with melody layer using oscillators. The music should have 3 channels: bass (square wave, low octave), melody (triangle wave), and percussion (noise bursts for kick/snare). Tempo: 140 BPM. As corruption increases, add pitch wobble, drop the melody channel, and add distortion.
```

---

**📱 Mobile Touch Controls**
```
Add on-screen touch controls for mobile: a left/right D-pad on the bottom-left, a jump button bottom-right, and a glitch gun button next to it. Style them as semi-transparent retro pixel buttons with glow. They should work alongside existing keyboard controls.
```

---

**🗺️ More Levels**
```
Add 3 more levels after the boss. Level 4: "Infinite Loop" — a vertically scrolling level. Level 5: "Fragmented Memory" — platforms that randomly disappear and reappear. Level 6: "Final Defrag" — a gauntlet with all enemy types, a corruption meter that starts at 50%, and a final door that only opens when 10 enemies are defeated.
```

---

**💀 Death & Story Screen**
```
Add cinematic screens between levels. Each should look like a corrupted terminal with typewriter text. Level 1 intro: "BOOT SEQUENCE INITIATED... CONTAINMENT FAILED." Level 2: "WARNING: MEMORY SECTORS CORRUPTED." Level 3: "BOSS PROCESS DETECTED. TERMINATE OR BE TERMINATED." Game over screen: show a fake system crash with error codes. Win screen: show a green "ESCAPE SUCCESSFUL" with ASCII art.
```

---

**⚡ Power-ups**
```
Add 4 collectible power-ups that spawn randomly in levels: (1) OVERCLOCK — doubles movement speed for 8 seconds, player glows orange. (2) FIREWALL — temporary shield that blocks one hit, shown as blue aura. (3) GLITCH BOMB — explodes and corrupts all tiles in a 5-tile radius. (4) GHOST PROTOCOL — full ghost mode for 5 seconds, pass through walls freely. Each has a pixel art icon and plays a unique sound.
```

---

**🏆 High Score Board**
```
Add a persistent local high score leaderboard using localStorage. After game over or win, prompt the player to enter a 3-character name (like classic arcades). Show the top 10 scores on the title screen in a scrolling marquee styled like an old arcade cabinet attract screen.
```

---

### 🧑 You

ok

---

### 🤖 Claude

Got it! Just paste any of those prompts whenever you're ready to upgrade the game and I'll build it in. 🎮

---
