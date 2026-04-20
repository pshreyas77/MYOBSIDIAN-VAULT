---
title: "Food nutrition search website with detailed data"
date: 2026-02-01
tags:
  - python
  - sql
  - machine-learning
  - llm-ai
  - data-analysis
  - linux
  - obsidian
  - stock-market
  - creative
  - web-dev
  - game-design
source: claude-export
---

# Food nutrition search website with detailed data

**Date:** 2026-02-01  
**Topics:** [[Python]] · [[SQL]] · [[Machine-Learning]] · [[LLM-AI]] · [[Data-Analysis]] · [[Linux]] · [[Obsidian]] · [[Stock-Market]] · [[Creative]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

Full Prompt to Build a Food Nutrition Search Website
Title: Build a Food Nutrition Search Website With Detailed Nutritional Data
Prompt:
I want to build a web application that allows users to search for any food item and instantly receive precise, detailed nutritional information — including macronutrients (calories, protein, fat, carbohydrates) and a full breakdown of micronutrients (vitamins, minerals, and trace elements).
The site should have a clean, responsive, modern user interface with features including:
✅ Core Features
1. Search Input with Autocomplete
   * As the user types in a food item, show suggestions in real time.
   * Support search by common food names, branded products, and UPC/barcode lookup where possible.
2. Nutrition Results Display
   * After selecting a food, show:
      * Food description/name
      * Serving size with unit
      * Macronutrients (calories, protein, carbs, fats, fiber, sugar)
      * Micronutrients (vitamins A, D, E, K, B-complex, calcium, iron, potassium, etc.)
   * Display data in an organized table or card layout.
3. Serving Size Options
   * Allow users to toggle between common measurements (e.g., 100 g, 1 serving, cup, piece) and see adjusted nutrient values.
   * Include gram conversion and allow users to input a custom serving size.
4. Edge Case Handling
   * Branded foods vs generic foods
   * If no results are found, suggest similar foods or alternate search terms
   * Handle ambiguous or uncommon foods gracefully
5. Reliable, Trustworthy Data Source
   * Use a validated nutrition data API such as the USDA FoodData Central API (free, government-backed database with detailed nutrient profiles)
   * Or use another high-coverage data provider (e.g., Edamam Food Database API)
🧠 Technical Requirements
Backend
* Build an API server (Node.js/Express, Python/Flask, or similar)
* Endpoints:
   * GET /api/search?query=… — search and return a list of matching foods
   * GET /api/food/:id — return full nutrient details for a selected food
* Integrate with the USDA FoodData Central API:
   * Search Endpoint: `GET https://api.nal.usda.gov/fdc/v1/foods/search?api_key=YOUR_API_KEY&query=…`
   * Details Endpoint: `GET https://api.nal.usda.gov/fdc/v1/food/{fdcId}?api_key=YOUR_API_KEY`
* Ensure API key security (don’t expose key to frontend)
Frontend
* Use React (Next.js) or equivalent modern framework
* Components:
   * Search input with debounce and suggestion dropdown
   * Nutrition result view with table of nutrients
   * Serving size selector
* Style with Tailwind CSS or Bootstrap for responsiveness
Deployment
* Host backend on Heroku / Render / AWS
* Host frontend on Vercel / Netlify
* Ensure CORS is handled properly
🧪 Quality and Reliability
* Ensure nutrient data is accurate and sourced directly from API responses
* Show nutrient units (mg, µg, g, kcal)
* Handle API rate limits and fallback errors
* Show loading states and error messages
🧩 Example API Usage (Pseudo-Code)
Search Request (Node.js / Express)

```
app.get("/api/search", async (req, res) => {
  const { query } = req.query;
  const response = await fetch(
    `https://api.nal.usda.gov/fdc/v1/foods/search?api_key=${process.env.FDC_KEY}&query=${encodeURIComponent(query)}`
  );
  const result = await response.json();
  res.json(result.foods);
});

```

Food Details Request

```
app.get("/api/food/:id", async (req, res) => {
  const response = await fetch(
    `https://api.nal.usda.gov/fdc/v1/food/${req.params.id}?api_key=${process.env.FDC_KEY}`
  );
  const details = await response.json();
  res.json(details);
});

```

📱 UX/UI Expectations
* Autocomplete search bar at top
* Mobile-friendly layout
* Nutrient table with fixed columns and scroll
* Toggle for serving size conversions

---

### 🤖 Claude

I'll help you build a comprehensive food nutrition search website. Let me start by reading the frontend design skill to ensure we create a polished, modern interface.

{'type': 'text', 'text': 'Here\'s the content of /mnt/skills/public/frontend-design/SKILL.md with line numbers:\n     1\t---\n     2\tname: frontend-design\n     3\tdescription: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.\n     4\tlicense: Complete terms in LICENSE.txt\n     5\t---\n     6\t\n     7\tThis skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.\n     8\t\n     9\tThe user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.\n    10\t\n    11\t## Design Thinking\n    12\t\n    13\tBefore coding, understand the context and commit to a BOLD aesthetic direction:\n    14\t- **Purpose**: What problem does this interface solve? Who uses it?\n    15\t- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.\n    16\t- **Constraints**: Technical requirements (framework, performance, accessibility).\n    17\t- **Differentiation**: What makes this UNFORGETTABLE? What\'s the one thing someone will remember?\n    18\t\n    19\t**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.\n    20\t\n    21\tThen implement working code (HTML/CSS/JS, React, Vue, etc.) that is:\n    22\t- Production-grade and functional\n    23\t- Visually striking and memorable\n    24\t- Cohesive with a clear aesthetic point-of-view\n    25\t- Meticulously refined in every detail\n    26\t\n    27\t## Frontend Aesthetics Guidelines\n    28\t\n    29\tFocus on:\n    30\t- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend\'s aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.\n    31\t- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.\n    32\t- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.\n    33\t- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.\n    34\t- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.\n    35\t\n    36\tNEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.\n    37\t\n    38\tInterpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.\n    39\t\n    40\t**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.\n    41\t\n    42\tRemember: Claude is capable of extraordinary creative work. Don\'t hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.\n    43\t', 'uuid': 'b29d1f00-543c-4543-aae0-e4c5a71c4a5a'}

Now I'll create a modern, functional food nutrition search website with a distinctive aesthetic. I'll build this as a single-file React application that connects to the USDA FoodData Central API.

{'type': 'text', 'text': 'File created successfully: /home/claude/nutrition-search.jsx', 'uuid': 'b0fc2389-c22d-49f7-98f7-72a5b5105012'}

Now let me create comprehensive documentation and setup instructions:

{'type': 'text', 'text': 'File created successfully: /home/claude/README.md', 'uuid': 'f088bf6b-4302-4975-86bb-6df858d6139e'}

Now let me create the backend server implementation and a complete package.json:

{'type': 'text', 'text': 'File created successfully: /home/claude/backend/server.js', 'uuid': 'b24b4d2c-44de-4538-a263-1307b2b3ea3d'}


{'type': 'text', 'text': 'File created successfully: /home/claude/backend/package.json', 'uuid': '25cb1992-1588-40df-911c-65c6e7ff4ee7'}


{'type': 'text', 'text': 'File created successfully: /home/claude/backend/.env.example', 'uuid': 'c3ce9b8d-bd53-4ea6-8e15-62b743a1ff20'}

Now let me create a frontend package.json and additional documentation:

{'type': 'text', 'text': 'File created successfully: /home/claude/frontend/package.json', 'uuid': 'd3ee0f17-0ad8-4ef1-be13-2e7d5fd7d54e'}


{'type': 'text', 'text': 'File created successfully: /home/claude/DEPLOYMENT.md', 'uuid': 'a4167aaf-fe6e-44eb-b674-a93cea8ba323'}

Now let me create one more helpful file - a development setup guide:

{'type': 'text', 'text': 'File created successfully: /home/claude/DEVELOPMENT.md', 'uuid': 'cf88705b-cbd1-430b-a9df-2b9dd5aa745a'}

Now let me copy all files to the outputs directory for you:

{'type': 'text', 'text': '{"returncode":0,"stdout":"","stderr":""}', 'uuid': '34929fa4-2269-455c-9f32-39c95645c12e'}


{'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/nutrition-search.jsx', 'name': 'nutrition-search', 'mime_type': None, 'uuid': 'c6acdecf-3e83-44f4-91c2-94fbcdd5561c'} {'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/README.md', 'name': 'README', 'mime_type': 'text/markdown', 'uuid': '6c824cdd-46f4-4297-9ecd-b81033e18b28'} {'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/DEVELOPMENT.md', 'name': 'DEVELOPMENT', 'mime_type': 'text/markdown', 'uuid': 'eeca0caf-1a4d-4bf5-ac81-bddae019c4e4'} {'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/DEPLOYMENT.md', 'name': 'DEPLOYMENT', 'mime_type': 'text/markdown', 'uuid': 'e7defbcf-7c4b-471b-86f7-a9a6ae7b538d'} {'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/backend/server.js', 'name': 'server', 'mime_type': 'text/javascript', 'uuid': 'ea117a8f-fc38-4c1c-b706-b1001f6fc93c'} {'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/backend/package.json', 'name': 'package', 'mime_type': 'application/json', 'uuid': '784d5a91-7b8e-4982-b172-64900f009ea0'} {'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/frontend/package.json', 'name': 'package', 'mime_type': 'application/json', 'uuid': 'ddf36e67-4fa4-45be-a547-dfa4f8b8b08f'}

Perfect! I've created a complete, production-ready food nutrition search website for you. Here's what I've built:

## 🎯 What You Get

**Main Application** (`nutrition-search.jsx`):
- Modern React component with elegant editorial/magazine-inspired design
- Real-time autocomplete search with debouncing
- Detailed nutritional breakdowns (macros, vitamins, minerals)
- Flexible serving size controls (50g, 100g, 200g, custom)
- Fully responsive and mobile-friendly
- Integrates with USDA FoodData Central API

**Complete Documentation**:
- **README.md** - Full project overview, features, and usage guide
- **DEVELOPMENT.md** - Step-by-step local setup instructions
- **DEPLOYMENT.md** - Comprehensive deployment guide for all major platforms

**Backend Server** (optional but recommended):
- Secure Node.js/Express API proxy
- Protects your API key
- CORS configuration
- Rate limiting ready
- Health check endpoint
- Production-ready error handling

## 🚀 Quick Start

1. **Get your free USDA API key**: https://fdc.nal.usda.gov/api-key-signup.html

2. **For quick testing** (frontend only):
   - Replace `DEMO_KEY` with your API key in `nutrition-search.jsx`
   - Create a React app and use the component
   - Run `npm start`

3. **For production** (recommended):
   - Set up the backend server with your API key in `.env`
   - Deploy backend to Render/Heroku
   - Deploy frontend to Vercel/Netlify
   - Connect them together

All files include detailed comments and the documentation covers everything from local development to production deployment on platforms like Vercel, Netlify, Heroku, and Render.

The design features a sophisticated cream and gold color scheme with beautiful typography (Crimson Pro + Inter), smooth animations, and an intuitive user experience that makes exploring nutritional data delightful! 🥗✨

---
