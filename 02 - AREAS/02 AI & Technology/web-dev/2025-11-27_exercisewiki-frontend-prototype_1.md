---
title: "ExerciseWiki Frontend Prototype"
date: 2025-11-27
tags:
  - sql
  - machine-learning
  - obsidian
  - stock-market
  - web-dev
  - game-design
  - religion
source: qwen-export
model: qwen3-max-2025-10-20
---

# ExerciseWiki Frontend Prototype

**Date:** 2025-11-27  
**Model:** `qwen3-max-2025-10-20`  
**Topics:** [[SQL]] · [[Machine-Learning]] · [[Obsidian]] · [[Stock-Market]] · [[Web-Dev]] · [[Game-Design]] · [[Religion]]

---

### 🧑 You

You are an expert full-stack developer.  
Build me an open-source MuscleWiki clone named “ExerciseWiki”.

STACK
- Frontend: Vite + React + TypeScript + TailwindCSS + react-hls-player
- Backend:  Node.js + Express + Mongoose + Redis
- DB:       MongoDB Atlas (free)
- Videos:   Cloudinary HLS (free)
- Deploy:   Render (server) + Cloudflare Pages (client)

REQUIREMENTS
1. Exact URL compatibility:  
   https://myapp.com/?muscle=4&equipment=7   must work like musclewiki.com
2. Re-use the provided SVG body-maps (male/female, front/back).  
   Clicking a muscle updates URL query param `muscle=id`.
3. Exercise grid page:  
   - Infinite scroll (react-intersection-observer)  
   - Filters: muscle, equipment, difficulty, force  
   - Cards show name, primary muscle, equipment icon, difficulty badge
4. Detail page:  
   - Auto-play muted HLS video (male/female toggle)  
   - Step-by-step instructions (numbered list)  
   - “Save to workout” button (localStorage fallback, sync when logged in)
5. API routes (cached 60 s):  
   GET /api/v2/exercises  
   GET /api/v2/exercises/:id  
   GET /api/v2/muscles  
   GET /api/v2/equipment  
6. Seed script: read `sample-data/exercises.json` and insert into Mongo.
7. PWA: offline fallback page, install prompt, icons generated via vite-pwa-plugin
8. Env file template and docker-compose for zero-config local dev.
9. MIT license, README with screenshots, “Deploy to Render” button.

OUTPUT
- GitHub repo folder structure  
- All source files (React pages, Express routes, Mongoose models)  
- Dockerfile + docker-compose.yml  
- GitHub Actions YAML for CI/CD  
- Render blueprint file `render.yaml`  
- One-line deploy commands in README
--------------------------------------------------------

---
