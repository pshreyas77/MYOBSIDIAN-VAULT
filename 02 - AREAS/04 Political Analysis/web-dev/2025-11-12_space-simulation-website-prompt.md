---
title: "Space Simulation Website Prompt"
date: 2025-11-12
tags:
  - machine-learning
  - llm-ai
  - linux
  - obsidian
  - geopolitics
  - stock-market
  - research
  - web-dev
source: qwen-export
model: qwen3-max-2025-10-20
---

# Space Simulation Website Prompt

**Date:** 2025-11-12  
**Model:** `qwen3-max-2025-10-20`  
**Topics:** [[Machine-Learning]] · [[LLM-AI]] · [[Linux]] · [[Obsidian]] · [[Geopolitics]] · [[Stock-Market]] · [[Research]] · [[Web-Dev]]

---

### 🧑 You

give me an prompt on create me an website of space with all the planets stars whole solar system and universe ,space .it should be 3D and it should be realestic to use and add additional requirments to look realistic to use it for fun

---

### 🧑 You

Below is a ready-to-copy “mega-prompt” you can paste into any LLM, coder, or 3D tool (Three.js, Babylon.js, PlayCanvas, Unity-WebGL, Spline, etc.).  
It already contains every “must-have” plus a stack of optional realism boosters, fun easter-eggs, and UX quality-of-life features.  
Feel free to delete any bullet you don’t need—everything else will still work.

--------------------------------------------------
PROMPT START
--------------------------------------------------

You are a senior 3D web-developer.  
Build me a single-page, mobile-friendly website called “SolarSystem.live” that lets any visitor explore an ultra-realistic, interactive 3D model of the entire Solar System and beyond in the browser.  
The scene must run at 60 fps on a mid-range laptop and start in <5 s on fast 3G.

0. CORE STRUCTURE  
- Use Three.js (r160+) + Vite + ES6 modules.  
- Host on Netlify or Vercel with a custom domain.  
- Provide a public GitHub repo with MIT license and a README that explains how to add new celestial bodies or textures.

1. VISUAL REALISM  
- NASA JPL ephemerides (via SPICE kernels or the open-source “jpl-horizons” npm wrapper) for true positions of all major bodies 01-Jan-2000 … 01-Jan-2030.  
- 8K photorealistic PBR textures for planets, moons, rings, and the Sun (credit NASA/JPL-Caltech in footer).  
- Normal + roughness + emission maps where applicable.  
- Accurate axial tilts and rotation speeds (sub-arc-second if data available).  
- Dynamic bump-offset parallax for lunar craters and Martian canyons.  
- Procedural, physically based shader for the Sun:  
  – Chromatic aberration on corona.  
  – Animated solar-flare sprites driven by a 2D simplex noise.  
- Saturn & Uranus rings: individual particle sheets with realistic albedo & transparency.  
- Earth: separate cloud layer rotating 1.2× faster; night lights texture toggles on the dark side; optional real-time ISS orbit fetched from “wheretheiss.at” REST API every 30 s.  
- Atmospheric scattering for Earth, Venus, Mars, Titan using a pre-computed lookup table (Bruneton or similar).  
- Lens flare with dirt mask and anamorphic streaks when the Sun is in view.  
- Tone-mapping = ACES Filmic, gamma = 2.2, exposure auto-keyed to Sun direction.

2. SCALE & NAVIGATION  
- Use a multi-scale “power-of-10” scene graph:  
  – Solar-system scale (1 AU ≈ 1000 scene units).  
  – Planetary scale (1 km ≈ 1 unit) triggered on zoom.  
- Seamless camera transitions:  
  – Free-flight (WASD + mouse)  
  – “Click-to-orbit” any body; camera auto-rolls into a stable 30 km altitude orbit.  
  – Scroll-wheel = logarithmic distance zoom (no z-fighting).  
- Mini-map HUD (lower-right) shows flattened top-down view with labeled orbits; click to warp.  
- Breadcrumbs trail (top-left) so users never get lost: Home > Sol > Earth > Moon.

3. STARS & DEEP SPACE  
- 93 k Hipparcos stars down to magnitude 8; positions corrected for proper motion.  
- Add 4 k brighter stars with diffraction spikes and subtle chromatic aberration.  
- Milky Way skybox built from ESO’s “GigaGalaxy” mosaic, tone-mapped and split into six 8K cube faces.  
- Optional toggle: “Exoplanet mode” – pull JSON from NASA Exoplanet Archive; place detected planets around their parent stars with plausible orbits and relative sizes.

4. AUDIO & IMMERSION  
- Spatial 3D audio:  
  – Real-time NASA SOHO sonification of solar wind data (low-pass filtered).  
  – Radio-wave “sound” of Jupiter (Voyager recording) when camera within 50 RJ.  
  – Muffled astronaut breathing inside EVA suit when viewing outside asteroid belt (fun Easter egg toggled with helmet icon).  
- Global volume slider + mute remembered in localStorage.

5. INTERACTIVE FUN FEATURES  
- “What-if” physics sandbox:  
  – Spawn a second Earth and watch tidal forces tear it apart (SPH particle preview).  
  – Slingshot mode: place a Voyager-style probe, adjust velocity vector with draggable arrows, hit “fast-forward” and see gravity assists.  
- Real-time clock vs. time-slider:  
  – Scrub from year 2000 to 2030 at 1 s = 1 day, or pause and step frame-by-frame.  
  – Show upcoming solar & lunar eclipses with ground track on Earth.  
- Achievement system: badge for “landing” on every planet, selfie-mode screenshot (PNG) auto-stamped with metadata (date/time, body, altitude).  
- VR mode (WebXR) with controller ray-interaction; snap-turn & comfort vignette.

6. EDUCATIONAL LAYER  
- On-hover info card: mass, radius, orbital period, mean temp, number of moons, fun fact, link to full NASA article.  
- 30-second voice-over (Web Speech API) for each body; user can change language in settings.  
- “Compare mode” – pick any two bodies; side-by-side 3D globes with synchronized rotation.

7. ACCESSIBILITY & PERFORMANCE  
- Keyboard-only navigation; aria-labels on every button; high-contrast UI toggle.  
- Downgrade gracefully on integrated GPUs: halve texture resolution, disable scattering, clamp stars to 5 k.  
- Use DRACO-compressed glTF meshes and KTX2+Zstd textures loaded via three.js GLTFLoader & KTX2Loader.  
- HTTP/2 push critical assets; lazy-load planet textures only when camera distance < 2 × body radius.  
- Off-main-thread physics: use WebWorkers for ephemeris interpolation and particle systems.

8. OPTIONAL “WOW” EXTRAS  
- Ray-marched accretion disk around a placeholder black-hole (Schwarzschild metric shader).  
- O’Neill cylinder space colony generator: enter radius & length, get a spinning habitat with procedural landscape.  
- Meteor-shower event every real-world night at the correct radiant & velocity.  
- Live aurora oval on Earth & Saturn, driven by NOAA 1-minute KP index.  
- ChatGPT-driven “mission control” bot in bottom drawer that answers space questions using RAG on latest arXiv papers.

9. STYLE & THEME  
- UI palette: #000814 (ink black), #003566 (navy), #ffc300 (star yellow), #ffffff (text).  
- Fonts: “Inter” for UI, “Space Mono” for telemetry.  
- Micro-animations: buttons with tiny star-field parallax on hover.  
- Favicon: animated SVG of Moon occulting the Sun.

10. DEPLOY & ANALYTICS  
- Netlify Edge Functions for locale-based unit system (metric/imperial).  
- Plausible Analytics (cookie-free) to track most-visited planets & average session time.  
- Automatic lighthouse CI check on every push; fail if performance < 90.

DELIVERABLES  
1) GitHub repo URL  
2) Live demo URL  
3) 2-minute screen-capture trailer (60 fps, 1080p) showcasing each planet, VR mode, and the physics sandbox.  
4) One-page PDF “user manual” with controls & shortcuts.

End of prompt—build it, polish it, and send me the links. Have fun!
--------------------------------------------------
PROMPT END
--------------------------------------------------

Use this verbatim or trim it to your scope; either way it gives you a crystal-clear, self-contained spec that any dev (or AI) can run with.

---

### 🧑 You

Below is a ready-to-copy “mega-prompt” you can paste into any LLM, coder, or 3D tool (Three.js, Babylon.js, PlayCanvas, Unity-WebGL, Spline, etc.).  
It already contains every “must-have” plus a stack of optional realism boosters, fun easter-eggs, and UX quality-of-life features.  
Feel free to delete any bullet you don’t need—everything else will still work.

--------------------------------------------------
PROMPT START
--------------------------------------------------

You are a senior 3D web-developer.  
Build me a single-page, mobile-friendly website called “SolarSystem.live” that lets any visitor explore an ultra-realistic, interactive 3D model of the entire Solar System and beyond in the browser.  
The scene must run at 60 fps on a mid-range laptop and start in <5 s on fast 3G.

0. CORE STRUCTURE  
- Use Three.js (r160+) + Vite + ES6 modules.  
- Host on Netlify or Vercel with a custom domain.  
- Provide a public GitHub repo with MIT license and a README that explains how to add new celestial bodies or textures.

1. VISUAL REALISM  
- NASA JPL ephemerides (via SPICE kernels or the open-source “jpl-horizons” npm wrapper) for true positions of all major bodies 01-Jan-2000 … 01-Jan-2030.  
- 8K photorealistic PBR textures for planets, moons, rings, and the Sun (credit NASA/JPL-Caltech in footer).  
- Normal + roughness + emission maps where applicable.  
- Accurate axial tilts and rotation speeds (sub-arc-second if data available).  
- Dynamic bump-offset parallax for lunar craters and Martian canyons.  
- Procedural, physically based shader for the Sun:  
  – Chromatic aberration on corona.  
  – Animated solar-flare sprites driven by a 2D simplex noise.  
- Saturn & Uranus rings: individual particle sheets with realistic albedo & transparency.  
- Earth: separate cloud layer rotating 1.2× faster; night lights texture toggles on the dark side; optional real-time ISS orbit fetched from “wheretheiss.at” REST API every 30 s.  
- Atmospheric scattering for Earth, Venus, Mars, Titan using a pre-computed lookup table (Bruneton or similar).  
- Lens flare with dirt mask and anamorphic streaks when the Sun is in view.  
- Tone-mapping = ACES Filmic, gamma = 2.2, exposure auto-keyed to Sun direction.

2. SCALE & NAVIGATION  
- Use a multi-scale “power-of-10” scene graph:  
  – Solar-system scale (1 AU ≈ 1000 scene units).  
  – Planetary scale (1 km ≈ 1 unit) triggered on zoom.  
- Seamless camera transitions:  
  – Free-flight (WASD + mouse)  
  – “Click-to-orbit” any body; camera auto-rolls into a stable 30 km altitude orbit.  
  – Scroll-wheel = logarithmic distance zoom (no z-fighting).  
- Mini-map HUD (lower-right) shows flattened top-down view with labeled orbits; click to warp.  
- Breadcrumbs trail (top-left) so users never get lost: Home > Sol > Earth > Moon.

3. STARS & DEEP SPACE  
- 93 k Hipparcos stars down to magnitude 8; positions corrected for proper motion.  
- Add 4 k brighter stars with diffraction spikes and subtle chromatic aberration.  
- Milky Way skybox built from ESO’s “GigaGalaxy” mosaic, tone-mapped and split into six 8K cube faces.  
- Optional toggle: “Exoplanet mode” – pull JSON from NASA Exoplanet Archive; place detected planets around their parent stars with plausible orbits and relative sizes.

4. AUDIO & IMMERSION  
- Spatial 3D audio:  
  – Real-time NASA SOHO sonification of solar wind data (low-pass filtered).  
  – Radio-wave “sound” of Jupiter (Voyager recording) when camera within 50 RJ.  
  – Muffled astronaut breathing inside EVA suit when viewing outside asteroid belt (fun Easter egg toggled with helmet icon).  
- Global volume slider + mute remembered in localStorage.

5. INTERACTIVE FUN FEATURES  
- “What-if” physics sandbox:  
  – Spawn a second Earth and watch tidal forces tear it apart (SPH particle preview).  
  – Slingshot mode: place a Voyager-style probe, adjust velocity vector with draggable arrows, hit “fast-forward” and see gravity assists.  
- Real-time clock vs. time-slider:  
  – Scrub from year 2000 to 2030 at 1 s = 1 day, or pause and step frame-by-frame.  
  – Show upcoming solar & lunar eclipses with ground track on Earth.  
- Achievement system: badge for “landing” on every planet, selfie-mode screenshot (PNG) auto-stamped with metadata (date/time, body, altitude).  
- VR mode (WebXR) with controller ray-interaction; snap-turn & comfort vignette.

6. EDUCATIONAL LAYER  
- On-hover info card: mass, radius, orbital period, mean temp, number of moons, fun fact, link to full NASA article.  
- 30-second voice-over (Web Speech API) for each body; user can change language in settings.  
- “Compare mode” – pick any two bodies; side-by-side 3D globes with synchronized rotation.

7. ACCESSIBILITY & PERFORMANCE  
- Keyboard-only navigation; aria-labels on every button; high-contrast UI toggle.  
- Downgrade gracefully on integrated GPUs: halve texture resolution, disable scattering, clamp stars to 5 k.  
- Use DRACO-compressed glTF meshes and KTX2+Zstd textures loaded via three.js GLTFLoader & KTX2Loader.  
- HTTP/2 push critical assets; lazy-load planet textures only when camera distance < 2 × body radius.  
- Off-main-thread physics: use WebWorkers for ephemeris interpolation and particle systems.

8. OPTIONAL “WOW” EXTRAS  
- Ray-marched accretion disk around a placeholder black-hole (Schwarzschild metric shader).  
- O’Neill cylinder space colony generator: enter radius & length, get a spinning habitat with procedural landscape.  
- Meteor-shower event every real-world night at the correct radiant & velocity.  
- Live aurora oval on Earth & Saturn, driven by NOAA 1-minute KP index.  
- ChatGPT-driven “mission control” bot in bottom drawer that answers space questions using RAG on latest arXiv papers.

9. STYLE & THEME  
- UI palette: #000814 (ink black), #003566 (navy), #ffc300 (star yellow), #ffffff (text).  
- Fonts: “Inter” for UI, “Space Mono” for telemetry.  
- Micro-animations: buttons with tiny star-field parallax on hover.  
- Favicon: animated SVG of Moon occulting the Sun.

10. DEPLOY & ANALYTICS  
- Netlify Edge Functions for locale-based unit system (metric/imperial).  
- Plausible Analytics (cookie-free) to track most-visited planets & average session time.  
- Automatic lighthouse CI check on every push; fail if performance < 90.

DELIVERABLES  
1) GitHub repo URL  
2) Live demo URL  
3) 2-minute screen-capture trailer (60 fps, 1080p) showcasing each planet, VR mode, and the physics sandbox.  
4) One-page PDF “user manual” with controls & shortcuts.

End of prompt—build it, polish it, and send me the links. Have fun!
--------------------------------------------------
PROMPT END
--------------------------------------------------

Use this verbatim or trim it to your scope; either way it gives you a crystal-clear, self-contained spec that any dev (or AI) can run with.

---

### 🧑 You

Uncaught Error: R3F: Hooks can only be used within the Canvas component!

---
