---
title: "Cosmic Atlas web application builder"
date: 2025-11-15
tags:
  - sql
  - machine-learning
  - obsidian
  - creative
  - web-dev
  - game-design
source: claude-export
---

# Cosmic Atlas web application builder

**Date:** 2025-11-15  
**Topics:** [[SQL]] · [[Machine-Learning]] · [[Obsidian]] · [[Creative]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

“Build a complete, self-contained ‘Cosmic Atlas’ web application that lets users explore, compare, and battle Marvel & DC/Vertigo cosmology layers. Use only modern, framework-free HTML5, CSS3, and vanilla ES6 (no external libs). Everything must run in one file (data + code + styles) and open directly in any current browser. Provide the fully-working file contents inside a single markdown code-fence titled `cosmic-atlas.html`.
Mandatory feature checklist (all in one file):
1. Data Model
   * One global array `cosmologyLayers[]` whose items are plain objects with keys: `universe` (`'Marvel'|'DC'`), `name`, `tier` (`'Lower'|'Mid-Tier'|'Higher'|'Top-Tier'`), `tierNumber` (1-4), `powerLevel` (1-10), `description`, `keyEntities` (string[]), `connections` (string[] of other layer names), `imageURL` (string or empty).
   * Seed the array with at least 8 sample layers per universe (32 total) covering every tier.
2. Hierarchical Visualizer (default route `'#/viz'`)
   * Radial layout: Top-Tier center → Lower outermost.
   * Nodes are color-coded discs: gold (Top), purple (Higher), orange (Mid), green (Lower).
   * Zoom/pan via mouse wheel & drag; animated entrance (fade-in + scale).
   * Hover tooltip (name + tier + power).
   * SVG curves show inter-layer connections.
   * Optional images mask-clipped inside nodes.
   * Legend & live stats (total layers, zoom %).
   * Click node to open side panel with full details.
3. Comparison View (route `'#/compare'`)
   * Split-screen: Marvel left (red theme) vs DC right (blue theme).
   * Same radial layout per side.
   * Auto-draw similarity lines: – Purple if same tier + name/description keyword overlap ≥ 30 %. – Gradient if power levels within ±2 and at least one keyword match. – Line opacity ∝ similarity score.
   * Hover highlight; toggle back to single-universe viz.
4. Image Manager (route `'#/manage'`)
   * Universe tabs; responsive grid of cards (thumbnail, name, tier).
   * Click card → inline editor: upload file (convert to data-URL) or paste URL; live preview; save updates global array.
   * Quick-search links to Marvel Wiki, DC Database, Comic Vine open in new tabs.
5. 1v1 Battle Arena (route `'#/battle'`)
   * Dramatic cosmic animated background (pure CSS).
   * Two dropdowns populate all layers (Marvel + DC).
   * “START BATTLE” pulsing gradient button.
   * Fight logic: higher powerLevel wins; equal = stalemate.
   * Animated power bars, win-margin badge.
   * After result, AI-generated 3-paragraph narrative (use built-in deterministic Markov-ish filler seeded by layer names & powers—no external API).
   * Trophy animation for winner; “New Battle” reset.
6. Navigation & Chrome
   * Fixed sidebar: logo (gradient + cosmos icon), three links: Visualizer, Cosmic Battle, Manage Images.
   * Active link highlighted; collapses to hamburger on mobile.
   * Purple/blue gradient theme throughout.
   * Add a prominent pulsing “1v1 Battle” button in the top controls of the Visualizer that jumps to `#/battle`.
7. Polishes
   * All routes handled via `window.onhashchange` (no page reloads).
   * Smooth CSS transitions everywhere.
   * Fully responsive (flex/grid, media queries).
   * No console errors; code readable & commented.

---

### 🤖 Claude

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cosmic Atlas - Marvel & DC Cosmology Explorer</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    :root {
      --primary: #6b46c1;
      --secondary: #4299e1;
      --gold: #fbbf24;
      --purple: #a855f7;
      --orange: #fb923c;
      --green: #34d399;
      --marvel-red: #ed1d24;
      --dc-blue: #0476f2;
      --bg-dark: #0f0f23;
      --bg-light: #1a1a2e;
      --text: #e2e8f0;
      --text-dim: #94a3b8;
    }

    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, var(--bg-dark) 0%, var(--bg-light) 100%);
      color: var(--text);
      overflow-x: hidden;
      min-height: 100vh;
    }

    /* Cosmic background animation */
    @keyframes stars {
      0% { transform: translateY(0); }
      100% { transform: translateY(-2000px); }
    }

    .cosmic-bg {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: -1;
      background: radial-gradient(2px 2px at 20% 30%, white, transparent),
                  radial-gradient(2px 2px at 60% 70%, white, transparent),
                  radial-gradient(1px 1px at 50% 50%, white, transparent),
                  radial-gradient(1px 1px at 80% 10%, white, transparent),
                  radial-gradient(2px 2px at 90% 60%, white, transparent),
                  radial-gradient(1px 1px at 33% 80%, white, transparent);
      background-size: 200% 200%;
      animation: stars 100s linear infinite;
      opacity: 0.3;
    }

    /* Sidebar */
    .sidebar {
      position: fixed;
      top: 0;
      left: 0;
      width: 260px;
      height: 100vh;
      background: rgba(26, 26, 46, 0.95);
      backdrop-filter: blur(10px);
      border-right: 2px solid rgba(107, 70, 193, 0.3);
      padding: 2rem 0;
      z-index: 1000;
      transition: transform 0.3s ease;
    }

    .sidebar.collapsed {
      transform: translateX(-260px);
    }

    .logo {
      text-align: center;
      margin-bottom: 3rem;
      padding: 0 1rem;
    }

    .logo-icon {
      font-size: 3rem;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .logo h1 {
      font-size: 1.5rem;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-top: 0.5rem;
    }

    .nav-links {
      list-style: none;
    }

    .nav-links li {
      margin: 0.5rem 0;
    }

    .nav-links a {
      display: flex;
      align-items: center;
      padding: 1rem 2rem;
      color: var(--text-dim);
      text-decoration: none;
      transition: all 0.3s ease;
      border-left: 3px solid transparent;
    }

    .nav-links a:hover {
      color: var(--text);
      background: rgba(107, 70, 193, 0.1);
    }

    .nav-links a.active {
      color: var(--text);
      background: rgba(107, 70, 193, 0.2);
      border-left-color: var(--primary);
    }

    .nav-links a span {
      margin-right: 1rem;
      font-size: 1.2rem;
    }

    /* Hamburger */
    .hamburger {
      position: fixed;
      top: 1rem;
      left: 1rem;
      width: 40px;
      height: 40px;
      background: var(--primary);
      border: none;
      border-radius: 8px;
      cursor: pointer;
      display: none;
      z-index: 1001;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 4px;
    }

    .hamburger span {
      width: 20px;
      height: 2px;
      background: white;
      transition: all 0.3s ease;
    }

    /* Main content */
    .main-content {
      margin-left: 260px;
      padding: 2rem;
      transition: margin-left 0.3s ease;
      min-height: 100vh;
    }

    .main-content.expanded {
      margin-left: 0;
    }

    /* View containers */
    .view {
      display: none;
      animation: fadeIn 0.5s ease;
    }

    .view.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Visualizer */
    .viz-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .viz-header h2 {
      font-size: 2rem;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .battle-btn {
      padding: 1rem 2rem;
      background: linear-gradient(135deg, var(--marvel-red), var(--dc-blue));
      border: none;
      border-radius: 12px;
      color: white;
      font-weight: bold;
      font-size: 1.1rem;
      cursor: pointer;
      animation: pulse 2s infinite;
      box-shadow: 0 0 20px rgba(237, 29, 36, 0.5);
      transition: transform 0.2s ease;
    }

    .battle-btn:hover {
      transform: scale(1.05);
    }

    @keyframes pulse {
      0%, 100% { box-shadow: 0 0 20px rgba(237, 29, 36, 0.5); }
      50% { box-shadow: 0 0 40px rgba(237, 29, 36, 0.8); }
    }

    .viz-controls {
      display: flex;
      gap: 1rem;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }

    .viz-controls button {
      padding: 0.75rem 1.5rem;
      background: rgba(107, 70, 193, 0.2);
      border: 1px solid var(--primary);
      border-radius: 8px;
      color: var(--text);
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .viz-controls button:hover {
      background: rgba(107, 70, 193, 0.4);
    }

    .viz-controls button.active {
      background: var(--primary);
    }

    .viz-container {
      position: relative;
      width: 100%;
      height: 80vh;
      background: rgba(15, 15, 35, 0.5);
      border-radius: 16px;
      border: 2px solid rgba(107, 70, 193, 0.3);
      overflow: hidden;
      cursor: grab;
    }

    .viz-container:active {
      cursor: grabbing;
    }

    .viz-canvas {
      width: 100%;
      height: 100%;
    }

    .legend {
      position: absolute;
      top: 1rem;
      right: 1rem;
      background: rgba(26, 26, 46, 0.9);
      backdrop-filter: blur(10px);
      padding: 1rem;
      border-radius: 12px;
      border: 1px solid rgba(107, 70, 193, 0.3);
    }

    .legend-item {
      display: flex;
      align-items: center;
      margin: 0.5rem 0;
      font-size: 0.9rem;
    }

    .legend-color {
      width: 20px;
      height: 20px;
      border-radius: 50%;
      margin-right: 0.5rem;
    }

    .stats {
      position: absolute;
      bottom: 1rem;
      left: 1rem;
      background: rgba(26, 26, 46, 0.9);
      backdrop-filter: blur(10px);
      padding: 1rem;
      border-radius: 12px;
      border: 1px solid rgba(107, 70, 193, 0.3);
    }

    .tooltip {
      position: absolute;
      background: rgba(26, 26, 46, 0.95);
      padding: 1rem;
      border-radius: 8px;
      border: 1px solid var(--primary);
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.3s ease;
      z-index: 100;
      max-width: 300px;
    }

    .tooltip.visible {
      opacity: 1;
    }

    /* Side panel */
    .side-panel {
      position: fixed;
      top: 0;
      right: -400px;
      width: 400px;
      height: 100vh;
      background: rgba(26, 26, 46, 0.98);
      backdrop-filter: blur(10px);
      border-left: 2px solid rgba(107, 70, 193, 0.3);
      padding: 2rem;
      overflow-y: auto;
      transition: right 0.3s ease;
      z-index: 1000;
    }

    .side-panel.open {
      right: 0;
    }

    .side-panel-close {
      position: absolute;
      top: 1rem;
      right: 1rem;
      background: none;
      border: none;
      color: var(--text);
      font-size: 1.5rem;
      cursor: pointer;
    }

    .side-panel h3 {
      color: var(--primary);
      margin-bottom: 1rem;
    }

    .side-panel-image {
      width: 100%;
      height: 200px;
      object-fit: cover;
      border-radius: 8px;
      margin-bottom: 1rem;
    }

    .side-panel-section {
      margin: 1.5rem 0;
    }

    .side-panel-section h4 {
      color: var(--secondary);
      margin-bottom: 0.5rem;
    }

    .entity-tag {
      display: inline-block;
      padding: 0.25rem 0.75rem;
      background: rgba(107, 70, 193, 0.2);
      border-radius: 20px;
      margin: 0.25rem;
      font-size: 0.85rem;
    }

    /* Compare view */
    .compare-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
      height: 85vh;
    }

    .compare-side {
      position: relative;
      border-radius: 16px;
      border: 2px solid;
      overflow: hidden;
    }

    .compare-side.marvel {
      border-color: var(--marvel-red);
      background: linear-gradient(135deg, rgba(237, 29, 36, 0.1), transparent);
    }

    .compare-side.dc {
      border-color: var(--dc-blue);
      background: linear-gradient(135deg, rgba(4, 118, 242, 0.1), transparent);
    }

    .compare-header {
      text-align: center;
      padding: 1rem;
      font-size: 1.5rem;
      font-weight: bold;
    }

    .compare-side.marvel .compare-header {
      background: linear-gradient(90deg, var(--marvel-red), transparent);
    }

    .compare-side.dc .compare-header {
      background: linear-gradient(90deg, var(--dc-blue), transparent);
    }

    /* Manager */
    .manager-tabs {
      display: flex;
      gap: 1rem;
      margin-bottom: 2rem;
    }

    .manager-tabs button {
      padding: 1rem 2rem;
      background: rgba(107, 70, 193, 0.2);
      border: 1px solid var(--primary);
      border-radius: 8px;
      color: var(--text);
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .manager-tabs button.active {
      background: var(--primary);
    }

    .manager-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1.5rem;
    }

    .layer-card {
      background: rgba(26, 26, 46, 0.6);
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid rgba(107, 70, 193, 0.3);
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .layer-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 30px rgba(107, 70, 193, 0.3);
    }

    .layer-card-image {
      width: 100%;
      height: 180px;
      object-fit: cover;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
    }

    .layer-card-content {
      padding: 1rem;
    }

    .layer-card-title {
      font-weight: bold;
      margin-bottom: 0.5rem;
    }

    .tier-badge {
      display: inline-block;
      padding: 0.25rem 0.75rem;
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: bold;
    }

    .tier-badge.top { background: var(--gold); color: #000; }
    .tier-badge.higher { background: var(--purple); }
    .tier-badge.mid { background: var(--orange); }
    .tier-badge.lower { background: var(--green); }

    /* Modal */
    .modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.8);
      display: none;
      justify-content: center;
      align-items: center;
      z-index: 2000;
    }

    .modal.open {
      display: flex;
    }

    .modal-content {
      background: var(--bg-light);
      padding: 2rem;
      border-radius: 16px;
      max-width: 600px;
      width: 90%;
      max-height: 90vh;
      overflow-y: auto;
    }

    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
    }

    .modal-close {
      background: none;
      border: none;
      color: var(--text);
      font-size: 1.5rem;
      cursor: pointer;
    }

    .form-group {
      margin: 1rem 0;
    }

    .form-group label {
      display: block;
      margin-bottom: 0.5rem;
      color: var(--text-dim);
    }

    .form-group input {
      width: 100%;
      padding: 0.75rem;
      background: rgba(15, 15, 35, 0.5);
      border: 1px solid rgba(107, 70, 193, 0.3);
      border-radius: 8px;
      color: var(--text);
    }

    .image-preview {
      width: 100%;
      height: 200px;
      object-fit: cover;
      border-radius: 8px;
      margin-top: 0.5rem;
    }

    .wiki-links {
      display: flex;
      gap: 0.5rem;
      margin-top: 0.5rem;
    }

    .wiki-links a {
      padding: 0.5rem 1rem;
      background: var(--primary);
      color: white;
      text-decoration: none;
      border-radius: 6px;
      font-size: 0.85rem;
      transition: all 0.3s ease;
    }

    .wiki-links a:hover {
      background: var(--secondary);
    }

    .save-btn {
      width: 100%;
      padding: 1rem;
      background: var(--primary);
      border: none;
      border-radius: 8px;
      color: white;
      font-weight: bold;
      cursor: pointer;
      margin-top: 1rem;
      transition: all 0.3s ease;
    }

    .save-btn:hover {
      background: var(--secondary);
    }

    /* Battle Arena */
    .battle-arena {
      position: relative;
      min-height: 85vh;
    }

    .battle-bg {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: 
        radial-gradient(circle at 20% 50%, rgba(237, 29, 36, 0.3), transparent 50%),
        radial-gradient(circle at 80% 50%, rgba(4, 118, 242, 0.3), transparent 50%);
      animation: battlePulse 4s ease-in-out infinite;
      z-index: 0;
    }

    @keyframes battlePulse {
      0%, 100% { opacity: 0.5; }
      50% { opacity: 1; }
    }

    .battle-content {
      position: relative;
      z-index: 1;
    }

    .battle-header {
      text-align: center;
      margin-bottom: 3rem;
    }

    .battle-header h2 {
      font-size: 3rem;
      background: linear-gradient(135deg, var(--marvel-red), var(--dc-blue));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 0.5rem;
    }

    .battle-setup {
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      gap: 2rem;
      align-items: center;
      margin-bottom: 3rem;
    }

    .fighter-select {
      background: rgba(26, 26, 46, 0.8);
      padding: 2rem;
      border-radius: 16px;
      border: 2px solid;
    }

    .fighter-select.fighter1 {
      border-color: var(--marvel-red);
    }

    .fighter-select.fighter2 {
      border-color: var(--dc-blue);
    }

    .fighter-select h3 {
      margin-bottom: 1rem;
      text-align: center;
    }

    .fighter-select select {
      width: 100%;
      padding: 1rem;
      background: rgba(15, 15, 35, 0.8);
      border: 1px solid rgba(107, 70, 193, 0.3);
      border-radius: 8px;
      color: var(--text);
      font-size: 1rem;
    }

    .vs-divider {
      font-size: 3rem;
      font-weight: bold;
      background: linear-gradient(135deg, var(--marvel-red), var(--dc-blue));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .start-battle-btn {
      display: block;
      margin: 0 auto 3rem;
      padding: 1.5rem 4rem;
      background: linear-gradient(135deg, var(--marvel-red), var(--dc-blue));
      border: none;
      border-radius: 16px;
      color: white;
      font-size: 1.5rem;
      font-weight: bold;
      cursor: pointer;
      animation: pulse 2s infinite;
      transition: transform 0.2s ease;
    }

    .start-battle-btn:hover {
      transform: scale(1.1);
    }

    .start-battle-btn:disabled {
      opacity: 0.5;
      cursor: not-allowed;
      animation: none;
    }

    .battle-result {
      display: none;
      text-align: center;
    }

    .battle-result.visible {
      display: block;
      animation: fadeIn 0.5s ease;
    }

    .power-bars {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
      margin-bottom: 2rem;
    }

    .power-bar-container {
      background: rgba(26, 26, 46, 0.8);
      padding: 1.5rem;
      border-radius: 12px;
    }

    .power-bar-label {
      margin-bottom: 0.5rem;
      font-weight: bold;
    }

    .power-bar {
      height: 40px;
      background: rgba(15, 15, 35, 0.8);
      border-radius: 20px;
      overflow: hidden;
      position: relative;
    }

    .power-bar-fill {
      height: 100%;
      transition: width 1s ease;
      position: relative;
    }

    .power-bar-fill.marvel {
      background: linear-gradient(90deg, var(--marvel-red), #ff6b6b);
    }

    .power-bar-fill.dc {
      background: linear-gradient(90deg, var(--dc-blue), #4dabf7);
    }

    .power-bar-value {
      position: absolute;
      right: 1rem;
      top: 50%;
      transform: translateY(-50%);
      font-weight: bold;
    }

    .winner-announcement {
      font-size: 2.5rem;
      font-weight: bold;
      margin: 2rem 0;
      animation: winnerGlow 1s ease-in-out infinite;
    }

    @keyframes winnerGlow {
      0%, 100% { text-shadow: 0 0 20px currentColor; }
      50% { text-shadow: 0 0 40px currentColor; }
    }

    .winner-announcement.marvel {
      color: var(--marvel-red);
    }

    .winner-announcement.dc {
      color: var(--dc-blue);
    }

    .winner-announcement.stalemate {
      background: linear-gradient(135deg, var(--marvel-red), var(--dc-blue));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .margin-badge {
      display: inline-block;
      padding: 0.5rem 1.5rem;
      background: rgba(107, 70, 193, 0.3);
      border-radius: 20px;
      margin: 1rem 0;
    }

    .trophy {
      font-size: 5rem;
      animation: trophyBounce 1s ease-in-out infinite;
    }

    @keyframes trophyBounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-20px); }
    }

    .battle-narrative {
      background: rgba(26, 26, 46, 0.8);
      padding: 2rem;
      border-radius: 12px;
      margin: 2rem 0;
      line-height: 1.8;
      text-align: left;
    }

    .battle-narrative p {
      margin-bottom: 1rem;
    }

    .new-battle-btn {
      padding: 1rem 2rem;
      background: var(--primary);
      border: none;
      border-radius: 8px;
      color: white;
      font-weight: bold;
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .new-battle-btn:hover {
      background: var(--secondary);
    }

    /* Responsive */
    @media (max-width: 768px) {
      .sidebar {
        width: 100%;
        transform: translateX(-100%);
      }

      .sidebar.open {
        transform: translateX(0);
      }

      .hamburger {
        display: flex;
      }

      .main-content {
        margin-left: 0;
      }

      .compare-container {
        grid-template-columns: 1fr;
        height: auto;
      }

      .compare-side {
        height: 60vh;
      }

      .battle-setup {
        grid-template-columns: 1fr;
      }

      .vs-divider {
        transform: rotate(90deg);
      }

      .side-panel {
        width: 100%;
        right: -100%;
      }
    }
  </style>
</head>
<body>
  <div class="cosmic-bg"></div>

  <button class="hamburger" id="hamburger">
    <span></span>
    <span></span>
    <span></span>
  </button>

  <aside class="sidebar" id="sidebar">
    <div class="logo">
      <div class="logo-icon">🌌</div>
      <h1>Cosmic Atlas</h1>
    </div>
    <nav>
      <ul class="nav-links">
        <li><a href="#/viz" data-route="viz"><span>🔮</span> Visualizer</a></li>
        <li><a href="#/battle" data-route="battle"><span>⚔️</span> Cosmic Battle</a></li>
        <li><a href="#/manage" data-route="manage"><span>🖼️</span> Manage Images</a></li>
      </ul>
    </nav>
  </aside>

  <main class="main-content" id="mainContent">
    <!-- Visualizer View -->
    <div class="view" id="vizView">
      <div class="viz-header">
        <h2>Cosmic Hierarchy</h2>
        <button class="battle-btn" onclick="window.location.hash = '#/battle'">⚔️ 1v1 BATTLE ARENA</button>
      </div>
      
      <div class="viz-controls">
        <button id="btnAll" class="active">All Universes</button>
        <button id="btnMarvel">Marvel Only</button>
        <button id="btnDC">DC Only</button>
        <button id="btnCompare" onclick="window.location.hash = '#/compare'">Compare View</button>
      </div>

      <div class="viz-container" id="vizContainer">
        <svg class="viz-canvas" id="vizCanvas"></svg>
        <div class="legend">
          <h4>Tiers</h4>
          <div class="legend-item">
            <div class="legend-color" style="background: var(--gold)"></div>
            <span>Top-Tier</span>
          </div>
          <div class="legend-item">
            <div class="legend-color" style="background: var(--purple)"></div>
            <span>Higher</span>
          </div>
          <div class="legend-item">
            <div class="legend-color" style="background: var(--orange)"></div>
            <span>Mid-Tier</span>
          </div>
          <div class="legend-item">
            <div class="legend-color" style="background: var(--green)"></div>
            <span>Lower</span>
          </div>
        </div>
        <div class="stats" id="stats">
          <div>Total Layers: <strong id="totalLayers">0</strong></div>
          <div>Zoom: <strong id="zoomLevel">100%</strong></div>
        </div>
        <div class="tooltip" id="tooltip"></div>
      </div>
    </div>

    <!-- Compare View -->
    <div class="view" id="compareView">
      <h2 style="text-align: center; margin-bottom: 2rem;">
        <span style="color: var(--marvel-red)">Marvel</span> vs 
        <span style="color: var(--dc-blue)">DC</span> Comparison
      </h2>
      <div class="compare-container">
        <div class="compare-side marvel">
          <div class="compare-header">MARVEL</div>
          <svg class="viz-canvas" id="compareMarvel"></svg>
        </div>
        <div class="compare-side dc">
          <div class="compare-header">DC</div>
          <svg class="viz-canvas" id="compareDC"></svg>
        </div>
      </div>
      <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 10;" id="compareLines"></svg>
    </div>

    <!-- Manage View -->
    <div class="view" id="manageView">
      <h2 style="margin-bottom: 2rem;">Image Manager</h2>
      <div class="manager-tabs">
        <button id="tabMarvel" class="active">Marvel</button>
        <button id="tabDC">DC</button>
      </div>
      <div class="manager-grid" id="managerGrid"></div>
    </div>

    <!-- Battle View -->
    <div class="view" id="battleView">
      <div class="battle-arena">
        <div class="battle-bg"></div>
        <div class="battle-

---
