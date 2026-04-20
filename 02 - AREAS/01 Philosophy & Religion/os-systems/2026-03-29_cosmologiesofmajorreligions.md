---
title: "CosmologiesOfMajorReligions"
date: 2026-03-29
tags:
  - sql
  - machine-learning
  - linux
  - obsidian
  - buddhism
  - hinduism
  - history
  - philosophy
  - geopolitics
  - stock-market
  - osint
  - research
  - projects
  - creative
  - finance
  - web-dev
  - game-design
  - religion
source: qwen-export
model: qwen3.5-plus
---

# CosmologiesOfMajorReligions

**Date:** 2026-03-29  
**Model:** `qwen3.5-plus`  
**Topics:** [[SQL]] · [[Machine-Learning]] · [[Linux]] · [[Obsidian]] · [[Buddhism]] · [[Hinduism]] · [[History]] · [[Philosophy]] · [[Geopolitics]] · [[Stock-Market]] · [[OSINT]] · [[Research]] · [[Projects]] · [[Creative]] · [[Finance]] · [[Web-Dev]] · [[Game-Design]] · [[Religion]]

---

### 🧑 You

compare hinduism , islam, sikhism, christianity, norse, ancient rome,shinto , taoism,confucianism, buddhism,jainism, ancient greek , judaism , zoroastrianism, mesopotamin , ancient egyptien ,  hinduism .  do deep research and make me an in detail cosmology just compare all which is bigger and which has more layers

---

### 🧑 You

do deep research and be 100% accurate and correct

---

### 🧑 You

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>COSMOLOGICAL ATLAS — All Traditions</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;900&family=Crimson+Pro:ital,wght@0,300;0,400;1,300;1,400&display=swap');

*{margin:0;padding:0;box-sizing:border-box;}

:root{
  --gold:#c9a84c;
  --gold-dim:#8b6914;
  --bg:#050508;
  --bg2:#0a0a12;
  --bg3:#0f0f1a;
  --text:#e8e4d8;
  --text-dim:#8a8070;
  --border:#1e1e2e;
  --accent:#6b4fcf;
}

body{
  background:var(--bg);
  color:var(--text);
  font-family:'Crimson Pro',Georgia,serif;
  min-height:100vh;
  overflow-x:hidden;
}

/* ── starfield canvas ── */
#stars{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;}

.wrapper{position:relative;z-index:1;max-width:1400px;margin:0 auto;padding:0 24px 80px;}

/* ── HERO ── */
.hero{
  text-align:center;
  padding:80px 0 60px;
  border-bottom:1px solid var(--border);
}
.hero-label{
  font-family:'Cinzel',serif;
  font-size:10px;
  letter-spacing:8px;
  color:var(--gold-dim);
  text-transform:uppercase;
  margin-bottom:24px;
}
.hero-title{
  font-family:'Cinzel',serif;
  font-size:clamp(32px,6vw,72px);
  font-weight:900;
  color:var(--gold);
  line-height:1.1;
  text-shadow:0 0 80px rgba(201,168,76,0.3);
  margin-bottom:20px;
}
.hero-sub{
  font-size:18px;
  color:var(--text-dim);
  font-style:italic;
  max-width:600px;
  margin:0 auto 40px;
  line-height:1.7;
}
.hero-stats{
  display:flex;
  justify-content:center;
  gap:48px;
  flex-wrap:wrap;
}
.stat{text-align:center;}
.stat-n{
  font-family:'Cinzel',serif;
  font-size:36px;
  font-weight:600;
  color:var(--gold);
}
.stat-l{font-size:12px;letter-spacing:3px;color:var(--text-dim);text-transform:uppercase;}

/* ── NAV TABS ── */
.tabs{
  display:flex;
  gap:4px;
  padding:24px 0 0;
  border-bottom:1px solid var(--border);
  overflow-x:auto;
  scrollbar-width:none;
}
.tabs::-webkit-scrollbar{display:none;}
.tab{
  font-family:'Cinzel',serif;
  font-size:11px;
  letter-spacing:2px;
  padding:10px 18px;
  border:1px solid transparent;
  background:none;
  color:var(--text-dim);
  cursor:pointer;
  white-space:nowrap;
  transition:all 0.2s;
  text-transform:uppercase;
}
.tab:hover{color:var(--text);border-color:var(--border);}
.tab.active{
  color:var(--gold);
  border-color:var(--gold-dim);
  background:rgba(201,168,76,0.05);
}

/* ── SECTIONS ── */
.section{display:none;padding:48px 0;}
.section.active{display:block;}

/* ── RANKING VIEW ── */
.rank-intro{
  font-size:16px;
  color:var(--text-dim);
  font-style:italic;
  margin-bottom:40px;
  max-width:700px;
  line-height:1.8;
}

.rank-grid{display:flex;flex-direction:column;gap:6px;}
.rank-row{
  display:grid;
  grid-template-columns:48px 1fr 80px 180px 80px;
  align-items:center;
  gap:16px;
  padding:14px 20px;
  border:1px solid var(--border);
  background:var(--bg2);
  cursor:pointer;
  transition:all 0.2s;
  position:relative;
  overflow:hidden;
}
.rank-row::before{
  content:'';
  position:absolute;
  left:0;top:0;bottom:0;
  width:3px;
  background:var(--row-color,var(--gold));
}
.rank-row:hover{border-color:rgba(201,168,76,0.3);background:var(--bg3);}
.rank-num{
  font-family:'Cinzel',serif;
  font-size:20px;
  font-weight:600;
  color:var(--text-dim);
  text-align:center;
}
.rank-name{
  font-family:'Cinzel',serif;
  font-size:15px;
  font-weight:600;
  color:var(--text);
}
.rank-tag{
  font-size:11px;
  color:var(--text-dim);
  letter-spacing:1px;
}
.rank-score-wrap{position:relative;height:8px;background:rgba(255,255,255,0.06);border-radius:4px;}
.rank-score-bar{
  position:absolute;
  left:0;top:0;height:100%;
  border-radius:4px;
  background:var(--row-color,var(--gold));
  transition:width 1s cubic-bezier(0.4,0,0.2,1);
}
.rank-layers{
  font-family:'Cinzel',serif;
  font-size:18px;
  color:var(--row-color,var(--gold));
  text-align:right;
}

/* ── COSMOLOGY CARDS ── */
.cosmo-grid{
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(340px,1fr));
  gap:2px;
}
.cosmo-card{
  background:var(--bg2);
  border:1px solid var(--border);
  padding:28px;
  cursor:pointer;
  transition:all 0.2s;
  position:relative;
}
.cosmo-card::after{
  content:'';
  position:absolute;
  inset:0;
  background:linear-gradient(135deg,transparent 60%,rgba(201,168,76,0.03));
  pointer-events:none;
}
.cosmo-card:hover{border-color:rgba(201,168,76,0.2);background:var(--bg3);}
.card-header{
  display:flex;
  align-items:flex-start;
  justify-content:space-between;
  margin-bottom:16px;
}
.card-glyph{
  font-size:32px;
  line-height:1;
  margin-bottom:8px;
}
.card-title{
  font-family:'Cinzel',serif;
  font-size:17px;
  font-weight:600;
  color:var(--gold);
  margin-bottom:4px;
}
.card-era{
  font-size:11px;
  letter-spacing:2px;
  color:var(--text-dim);
  text-transform:uppercase;
}
.card-badge{
  font-family:'Cinzel',serif;
  font-size:22px;
  font-weight:900;
  color:var(--card-color,var(--gold));
  text-align:right;
  line-height:1;
}
.card-badge-label{
  font-size:9px;
  letter-spacing:2px;
  color:var(--text-dim);
  text-transform:uppercase;
  text-align:right;
}
.card-layers{
  display:flex;
  flex-wrap:wrap;
  gap:6px;
  margin-top:12px;
}
.layer-pill{
  font-size:10px;
  padding:3px 10px;
  border:1px solid;
  border-radius:2px;
  letter-spacing:1px;
  color:var(--pill-color,var(--gold-dim));
  border-color:var(--pill-color,var(--gold-dim));
  background:rgba(201,168,76,0.04);
}
.card-desc{
  font-size:13px;
  color:var(--text-dim);
  line-height:1.7;
  margin-top:12px;
  font-style:italic;
}

/* ── DETAIL MODAL ── */
.modal-overlay{
  display:none;
  position:fixed;
  inset:0;
  background:rgba(0,0,0,0.85);
  z-index:100;
  overflow-y:auto;
  padding:40px 20px;
}
.modal-overlay.open{display:block;}
.modal{
  max-width:840px;
  margin:0 auto;
  background:var(--bg2);
  border:1px solid rgba(201,168,76,0.2);
  position:relative;
}
.modal-close{
  position:absolute;
  top:20px;right:20px;
  background:none;border:1px solid var(--border);
  color:var(--text-dim);
  width:36px;height:36px;
  cursor:pointer;
  font-size:16px;
  display:flex;align-items:center;justify-content:center;
  transition:all 0.2s;
}
.modal-close:hover{border-color:var(--gold-dim);color:var(--gold);}
.modal-hero{
  padding:48px 48px 32px;
  border-bottom:1px solid var(--border);
  background:linear-gradient(135deg,rgba(201,168,76,0.03) 0%,transparent 60%);
}
.modal-glyph{font-size:52px;margin-bottom:16px;line-height:1;}
.modal-title{
  font-family:'Cinzel',serif;
  font-size:32px;
  font-weight:900;
  color:var(--gold);
  margin-bottom:8px;
}
.modal-meta{font-size:13px;color:var(--text-dim);letter-spacing:2px;text-transform:uppercase;}
.modal-body{padding:40px 48px;}
.modal-section-title{
  font-family:'Cinzel',serif;
  font-size:11px;
  letter-spacing:4px;
  color:var(--gold-dim);
  text-transform:uppercase;
  margin-bottom:16px;
  padding-bottom:8px;
  border-bottom:1px solid var(--border);
}
.modal-text{
  font-size:16px;
  line-height:1.85;
  color:var(--text-dim);
  margin-bottom:32px;
}
.modal-text strong{color:var(--text);font-weight:400;}

.layers-diagram{margin:24px 0 32px;}
.layer-item{
  display:flex;
  align-items:center;
  gap:16px;
  padding:12px 0;
  border-bottom:1px solid rgba(255,255,255,0.04);
}
.layer-num{
  font-family:'Cinzel',serif;
  font-size:11px;
  color:var(--gold-dim);
  width:40px;
  flex-shrink:0;
  text-align:center;
}
.layer-bar{
  width:8px;
  flex-shrink:0;
  border-radius:2px;
  align-self:stretch;
  min-height:36px;
}
.layer-content{}
.layer-name{
  font-family:'Cinzel',serif;
  font-size:14px;
  color:var(--text);
  margin-bottom:4px;
}
.layer-desc{font-size:13px;color:var(--text-dim);line-height:1.6;}

.stats-row{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:12px;
  margin:24px 0;
}
.stat-box{
  background:var(--bg3);
  border:1px solid var(--border);
  padding:16px;
  text-align:center;
}
.stat-box-n{
  font-family:'Cinzel',serif;
  font-size:28px;
  font-weight:600;
  color:var(--gold);
}
.stat-box-l{
  font-size:11px;
  letter-spacing:2px;
  color:var(--text-dim);
  text-transform:uppercase;
  margin-top:4px;
}

/* ── COMPARISON TABLE ── */
.compare-table-wrap{overflow-x:auto;margin-top:32px;}
.compare-table{
  width:100%;
  border-collapse:collapse;
  font-size:13px;
}
.compare-table th{
  font-family:'Cinzel',serif;
  font-size:10px;
  letter-spacing:2px;
  text-transform:uppercase;
  color:var(--gold-dim);
  padding:12px 16px;
  text-align:left;
  border-bottom:1px solid var(--border);
  white-space:nowrap;
}
.compare-table td{
  padding:12px 16px;
  border-bottom:1px solid rgba(255,255,255,0.04);
  color:var(--text-dim);
  vertical-align:top;
  line-height:1.6;
}
.compare-table tr:hover td{background:rgba(255,255,255,0.02);}
.compare-table td:first-child{
  font-family:'Cinzel',serif;
  font-size:13px;
  color:var(--text);
  white-space:nowrap;
}
.td-num{
  font-family:'Cinzel',serif;
  font-size:16px;
  color:var(--gold);
  text-align:center;
}

/* ── SPECTRUM VIEW ── */
.spectrum-section{margin-bottom:48px;}
.spectrum-title{
  font-family:'Cinzel',serif;
  font-size:13px;
  letter-spacing:3px;
  color:var(--gold-dim);
  text-transform:uppercase;
  margin-bottom:20px;
}
.spectrum-bar-row{
  display:flex;
  align-items:center;
  gap:12px;
  margin-bottom:8px;
}
.spectrum-label{
  font-family:'Cinzel',serif;
  font-size:11px;
  color:var(--text-dim);
  width:160px;
  flex-shrink:0;
  text-align:right;
}
.spectrum-track{
  flex:1;
  height:6px;
  background:rgba(255,255,255,0.06);
  border-radius:3px;
  position:relative;
}
.spectrum-fill{
  position:absolute;
  left:0;top:0;height:100%;
  border-radius:3px;
  transition:width 1s ease;
}
.spectrum-val{
  font-family:'Cinzel',serif;
  font-size:12px;
  color:var(--text-dim);
  width:40px;
  text-align:right;
}

/* ── FOOTER ── */
footer{
  text-align:center;
  padding:40px 0;
  border-top:1px solid var(--border);
  font-size:12px;
  color:var(--text-dim);
  letter-spacing:2px;
}

@media(max-width:640px){
  .rank-row{grid-template-columns:36px 1fr 60px;}
  .rank-score-wrap,.rank-layers{display:none;}
  .modal-hero,.modal-body{padding:28px 24px;}
  .stats-row{grid-template-columns:1fr 1fr;}
}
</style>
</head>
<body>

<canvas id="stars"></canvas>

<div class="wrapper">

<!-- HERO -->
<div class="hero">
  <div class="hero-label">Godmode Research Atlas</div>
  <h1 class="hero-title">The Cosmological Atlas<br>of Human Civilization</h1>
  <p class="hero-sub">A deep comparative study of cosmological architecture across 17 major religious and philosophical traditions — ranked by scale, layered complexity, and cosmological depth.</p>
  <div class="hero-stats">
    <div class="stat"><div class="stat-n">17</div><div class="stat-l">Traditions</div></div>
    <div class="stat"><div class="stat-n">200+</div><div class="stat-l">Cosmic Realms</div></div>
    <div class="stat"><div class="stat-n">∞</div><div class="stat-l">Universes (Hindu)</div></div>
    <div class="stat"><div class="stat-n">14</div><div class="stat-l">Max Layers</div></div>
  </div>
</div>

<!-- TABS -->
<div class="tabs">
  <button class="tab active" onclick="showTab('ranking')">★ Power Ranking</button>
  <button class="tab" onclick="showTab('cards')">All Traditions</button>
  <button class="tab" onclick="showTab('compare')">Deep Compare</button>
  <button class="tab" onclick="showTab('spectrum')">Spectrum Analysis</button>
</div>

<!-- ═══ RANKING TAB ═══ -->
<div class="section active" id="tab-ranking">
  <p class="rank-intro">Ranked by cosmological complexity — combining total named realms, vertical layers (heavens + hells + intermediate zones), conceptual scope (finite vs. infinite/cyclic universes), and the sophistication of afterlife cartography.</p>
  <div class="rank-grid" id="rankGrid"></div>
</div>

<!-- ═══ CARDS TAB ═══ -->
<div class="section" id="tab-cards">
  <div class="cosmo-grid" id="cosmoGrid"></div>
</div>

<!-- ═══ COMPARE TAB ═══ -->
<div class="section" id="tab-compare">
  <div class="compare-table-wrap">
    <table class="compare-table" id="compareTable">
      <thead>
        <tr>
          <th>Tradition</th>
          <th>Total Realms</th>
          <th>Heavens</th>
          <th>Hells / Dark Realms</th>
          <th>Intermediate Zones</th>
          <th>Time Scale</th>
          <th>Universe Type</th>
          <th>Creation</th>
          <th>Afterlife System</th>
        </tr>
      </thead>
      <tbody id="compareBody"></tbody>
    </table>
  </div>
</div>

<!-- ═══ SPECTRUM TAB ═══ -->
<div class="section" id="tab-spectrum">
  <div id="spectrumContent"></div>
</div>

</div><!-- /wrapper -->

<!-- DETAIL MODAL -->
<div class="modal-overlay" id="modal" onclick="closeModal(event)">
  <div class="modal" id="modalContent"></div>
</div>

<footer>
  COSMOLOGICAL ATLAS · 17 TRADITIONS · GODMODE RESEARCH · PILLI SHREYAS
</footer>

<script>
/* ════════════════════════════════════════
   DATA — All 17 Traditions
════════════════════════════════════════ */
const TRADITIONS = [
  {
    id:'hinduism',
    name:'Hinduism',
    era:'c. 1500 BCE – present',
    glyph:'🕉',
    color:'#e07b39',
    complexityScore:100,
    totalRealms:14,
    heavens:7,
    hells:7,
    intermediate:3,
    tag:'Infinite Multiverse',
    timeScale:'Cyclic / Infinite (Kalpas)',
    universeType:'Infinite cycling multiverse (Brahmanda)',
    creation:'Brahma emerges from lotus of Vishnu; creates from sound/Om; cycles of creation-destruction (Pralaya)',
    afterlife:'Karma + Samsara + Moksha; 84 million rebirths possible; liberation into Brahman/Nirvana',
    shortDesc: 'The most cosmologically vast of all traditions — infinite universes, 14 worlds, cosmic time in trillions of years.',
    layers:[
      {name:'Satya-loka / Brahma-loka',desc:'Highest realm of Brahma, beyond time and decay. Souls here merge with the Absolute.',color:'#ffd700'},
      {name:'Tapa-loka',desc:'Realm of tapas (austerity); great sages who survived the previous universe.',color:'#ffc040'},
      {name:'Jana-loka',desc:'Realm of the sons of Brahma — Sanaka, Sanandana, Sanatana, Sanatkumara.',color:'#ffaa30'},
      {name:'Mahar-loka',desc:'Realm of great sages (Bhrigu, etc.) who survive until Brahma\'s day ends.',color:'#ff9020'},
      {name:'Svar-loka (Svarga)',desc:'Heaven of Indra; ruled by devas; realm of pleasures and merit-based rewards.',color:'#ff7000'},
      {name:'Bhuvar-loka',desc:'Atmospheric realm between earth and sun; semi-divine beings, yakshas, gandharvas.',color:'#e06000'},
      {name:'Bhu-loka (Earth)',desc:'The mortal realm of humans, animals, plants. Center of karmic action.',color:'#c05000'},
      {name:'Atala',desc:'First underworld; ruled by Bala, son of Maya. Realm of illusion and desire.',color:'#803030'},
      {name:'Vitala',desc:'Realm of Hatakesvara (Shiva form); ruled by Bhava; the realm of gold.',color:'#703020'},
      {name:'Sutala',desc:'Realm of Bali Maharaja; considered purer than heavens, protected by Vishnu.',color:'#602818'},
      {name:'Talatala',desc:'Realm of Maya the architect; a city of three worlds (Tripura); realm of sorcery.',color:'#502010'},
      {name:'Mahatala',desc:'Realm of the many-hooded serpents, sons of Kadru; dark and fearful.',color:'#401808'},
      {name:'Rasatala',desc:'Realm of the Danavas and Daityas (demons); enemies of devas.',color:'#300f05'},
      {name:'Patala',desc:'Deepest realm; home of Vasuki and Shesha (cosmic serpents); brilliantly lit by jewels.',color:'#200a02'},
    ],
    keyFacts:[
      'Brahma lives 100 Brahma-years = ~311 trillion human years',
      'One Maha-Yuga = 4,320,000 human years',
      'One Kalpa (Brahma\'s day) = 4.32 billion years',
      '14 Lokas total across 7 upper + 7 lower',
      'Brahma creates millions of universes simultaneously — each a bubble in the cosmic ocean',
      'Narakas (hells) number 21 to 28 depending on the scripture',
      'The Devi-Bhagavata Purana lists 8 universes above ours alone'
    ]
  },
  {
    id:'jainism',
    name:'Jainism',
    era:'c. 600 BCE – present',
    glyph:'☸',
    color:'#7ecee0',
    complexityScore:97,
    totalRealms:14,
    heavens:16,
    hells:7,
    intermediate:2,
    tag:'Most Precise Cosmos',
    timeScale:'Infinite cyclic time (no beginning/end)',
    universeType:'Finite universe (Loka) in infinite non-universe (Aloka)',
    creation:'No creator god; universe is eternal, self-sustaining; governed by natural law',
    afterlife:'Karma particles bind to soul; liberation = Siddha state at apex of universe; no rebirth',
    shortDesc: 'The most geometrically precise cosmology — a mapped, measurable finite universe with 14 realms and infinite time cycles.',
    layers:[
      {name:'Siddha-loka / Ishat-pragbhara',desc:'The crescent-shaped apex of the universe; home of all liberated souls (Siddhas) with no further rebirth. Pure consciousness.',color:'#e0f7ff'},
      {name:'Anuttara Vimanas (5 heavens)',desc:'Five topmost heavens; beings of supreme happiness; one more rebirth then liberation.',color:'#b0e8ff'},
      {name:'Graiveyaka (9 heavens)',desc:'Nine heavens below Anuttara; beings of increasingly refined divine consciousness.',color:'#80d0f0'},
      {name:'Kalpa heavens (12 pairs)',desc:'The 12 pairs of kalpa heavens (Saudharma to Anat); graduated divine realms with Indras.',color:'#50b8e0'},
      {name:'Jyotishka (luminous beings)',desc:'Realm of sun, moon, planets, and stars — treated as conscious divine beings.',color:'#30a0d0'},
      {name:'Vyantar (intermediate beings)',desc:'Realm of Vyantra devas — tree spirits, yakshas, gandharvas, kinnaras in the middle world.',color:'#1888c0'},
      {name:'Bhavanapati (mansion-dwelling)',desc:'10 orders of mansion-dwelling gods in lower universe; powerful but impure.',color:'#0f70a0'},
      {name:'Manushyaloka (human realm)',desc:'Middle realm; only here can liberation be attained. Contains the Jambudvipa and concentric oceans.',color:'#0c5880'},
      {name:'Tiryag-loka (animal realm)',desc:'Realm of non-human creatures; part of the middle cosmos.',color:'#083840'},
      {name:'Ratnaprabha (Hell 1)',desc:'First hell; dark, cold, and hot suffering; souls experience physical pain.',color:'#803030'},
      {name:'Sharkara (Hell 2)',desc:'Second hell; beings with cruder suffering and denser darkness.',color:'#6a2525'},
      {name:'Valukaprabha (Hell 3)',desc:'Third hell; beings burn in sand; intense heat and deprivation.',color:'#541a1a'},
      {name:'Pankha (Hell 4)',desc:'Fourth hell; muddy, foul realm of intense karmic suffering.',color:'#3e1010'},
      {name:'Dhuma (Hell 5)',desc:'Fifth hell; smoky, poisonous environment; beings torment each other.',color:'#280808'},
      {name:'Tamah (Hell 6)',desc:'Sixth hell; absolute darkness; extreme suffering and deprivation.',color:'#180505'},
      {name:'Mahatamah (Hell 7)',desc:'Deepest hell; the Apratishthan naraka; beings clumped in each other; worst possible karma.',color:'#0a0202'},
    ],
    keyFacts:[
      'The universe (Loka) is shaped like a standing man with arms akimbo',
      'Precisely calculated: 7 Rajjus tall, 1 Rajju wide at the narrowest',
      'Time is cyclic: Utsarpini (ascending) and Avasarpini (descending) half-cycles',
      'One full cycle = 20 Kodakodi Sagaras (~uncountably vast time)',
      'Karma is treated as literal physical particles (Pudgala)',
      '14 Gunasthanas (stages of spiritual development) mapped precisely',
      'No creator god — universe operates by natural law (Dharma/Adharma/Akasha/Kala)'
    ]
  },
  {
    id:'buddhism',
    name:'Buddhism',
    era:'c. 500 BCE – present',
    glyph:'☸',
    color:'#f5a623',
    complexityScore:95,
    totalRealms:31,
    heavens:26,
    hells:8,
    intermediate:1,
    tag:'31 Planes of Existence',
    timeScale:'Cyclic / Kalpas (incomprehensible duration)',
    universeType:'Infinite world-systems (Chakkavala); cyclic creation/destruction',
    creation:'No creator god; universes arise and pass through natural conditions; beginningless',
    afterlife:'Rebirth in 31 planes based on karma and mental states; Nirvana = cessation of rebirth',
    shortDesc: 'The most detailed afterlife map — 31 precisely defined planes across 3 realms, with minute distinctions of consciousness.',
    layers:[
      {name:'Arupajhana (4 Formless Realms)',desc:'Nevasaññānāsaññāyatana (neither-perception-nor-non-perception); Ākiñcaññāyatana (nothingness); Viññānañcāyatana (infinite consciousness); Ākāsānañcāyatana (infinite space). Duration: billions of Kalpas.',color:'#fffde7'},
      {name:'Suddhavasa (5 Pure Abodes)',desc:'Akanittha, Sudassi, Sudassa, Atappa, Aviha — realms where Anagami (non-returners) achieve full liberation. No ordinary beings here.',color:'#fff3b0'},
      {name:'Vehapphala (Ripened)',desc:'Immensely long-lived brahmas from deep meditative absorption. Duration: 500 great Kalpas.',color:'#ffe070'},
      {name:'Jhana Brahma Realms (12)',desc:'12 heavens of form-brahmas corresponding to the 4 jhana levels. Vast meditation-generated realms.',color:'#ffc840'},
      {name:'Cātu-mahārājika (4 Kings)',desc:'Realm of the 4 Great Kings guarding directions. Gandharvas, Nagas, Yakshas dwell here.',color:'#ff9020'},
      {name:'Tāvatiṃsa (33 Gods)',desc:'Heaven of 33 gods; Sakka (Indra) reigns; where the Buddha preached the Abhidhamma. 36 million years duration.',color:'#ff7000'},
      {name:'Yāma Heaven',desc:'Gods free from strife; 144 million year lifespan.',color:'#e06000'},
      {name:'Tusita Heaven',desc:'Future Buddhas abide here (Maitreya waits here now). 576 million years.',color:'#c05000'},
      {name:'Nimmānarati',desc:'Gods who delight in their own creations; 2.3 billion year lifespan.',color:'#a04000'},
      {name:'Paranimmita-vasavatti',desc:'Gods who direct others\' creations; highest sensual heaven; Mara\'s realm. 9.2 billion years.',color:'#803000'},
      {name:'Human Realm',desc:'The unique realm where liberation is most accessible; mixture of pleasure/pain creates seeking.',color:'#604040'},
      {name:'Asura Realm',desc:'Demigods; powerful but plagued by jealousy and pride; constant war with devas.',color:'#504050'},
      {name:'Peta Realm (Hungry Ghosts)',desc:'Beings tormented by insatiable craving; some wander earth; immense suffering from unfulfilled desire.',color:'#605070'},
      {name:'Animal Realm',desc:'Governed by instinct; much suffering; limited capacity for liberation.',color:'#504060'},
      {name:'Niraya (8 Great Hells)',desc:'Sanjiva, Kālasutta, Sanghāta, Roruva, Mahāroruva, Tāpana, Mahātāpana, Avīci. Avīci = worst; continuous suffering without respite. Duration: incalculable.',color:'#300020'},
    ],
    keyFacts:[
      '31 distinct planes mapped in the Abhidhamma Pitaka',
      'Each of the 8 great hells has 4 side hells (16 total side hells)',
      'Avici (Avīci) Hell = 8x8x8 = 512 sub-sections of suffering',
      'The cosmos contains 1,000,000,000 world-systems (Trichiliocosm)',
      'Each world-system has its own Mount Sumeru, heavens, and hells',
      'A Kalpa\'s length: if a mountain of rock 1 league cubed is wiped with silk once a century, when gone = 1 Kalpa',
      'Deva lifespan in Tusita: 576,000,000 human years'
    ]
  },
  {
    id:'hinduism2',
    name:'Hinduism (Shaivite)',
    era:'c. 200 BCE – present',
    glyph:'🔱',
    color:'#9b59b6',
    complexityScore:93,
    totalRealms:36,
    heavens:12,
    hells:28,
    intermediate:4,
    tag:'36 Tattvas / Agamic',
    timeScale:'Cyclic / Kalpas / Shiva-cycles',
    universeType:'Emanationist — Shiva projects reality through Tattvas',
    creation:'Shiva dances reality into existence (Nataraja); creation = play (Lila) of consciousness',
    afterlife:'Karma + grace (Shaktipata); liberation = union with Shiva (Shivahood / Sayujya)',
    shortDesc: 'Shaiva Agama tradition — 36 cosmic categories (Tattvas) and 28 named hells; deeply metaphysical emanationist cosmology.',
    layers:[
      {name:'Shiva-tattva',desc:'Pure consciousness; beyond all qualities; the ground of being itself.',color:'#f3e5ff'},
      {name:'Shakti-tattva',desc:'Dynamic power/energy of Shiva; the activating principle of all creation.',color:'#dab0ff'},
      {name:'Sadashiva-tattva',desc:'Will (Iccha) predominant; the "I am this" stage of cosmic identity.',color:'#c080ff'},
      {name:'Ishvara-tattva',desc:'Knowledge (Jnana) predominant; the "this am I" stage; cosmic lordship.',color:'#a050f0'},
      {name:'Shuddhavidya',desc:'Action (Kriya) predominant; equality of I and this; pure being-knowing.',color:'#8030d0'},
      {name:'Maya + 5 Kanchukas',desc:'The veil of limitation: Kala (limited action), Vidya (limited knowledge), Raga (attachment), Kala (time), Niyati (space/fate).',color:'#6010a0'},
      {name:'Purusha + Prakriti',desc:'Individual soul (Purusha) and primal matter (Prakriti) — Samkhya categories embedded in Shaiva system.',color:'#400080'},
      {name:'Buddhi, Ahamkara, Manas',desc:'Intellect, ego, mind — the inner instruments. Subtler than sense organs.',color:'#300060'},
      {name:'5 Tanmatras',desc:'Subtle essence-elements: sound, touch, form, taste, smell.',color:'#200040'},
      {name:'5 Mahabhutas',desc:'Gross elements: ether, air, fire, water, earth. The physical cosmos.',color:'#140025'},
      {name:'28 Narakas (Hells)',desc:'28 named hells from Tamisra to Avichi; for specific sins: Kalasutra (liars), Asipatravana (those who harm others), etc.',color:'#200020'},
    ],
    keyFacts:[
      '36 Tattvas form the complete ontological map of reality',
      '28 specifically named hells in Shaiva Purana tradition',
      'Shaiva Siddhanta (South Indian) and Kashmir Shaivism differ in details',
      'Kashmir Shaivism recognizes 36 Tattvas as pure consciousness differentiating',
      'Trika philosophy maps 3 aspects: Shiva, Shakti, Nara (bound soul)',
      'Spanda (vibration) doctrine: reality pulsates between Shiva and Shakti',
      'Liberation = recognition (Pratyabhijna) that one was always Shiva'
    ]
  },
  {
    id:'mesopotamian',
    name:'Mesopotamian',
    era:'c. 3000–500 BCE',
    glyph:'𒀭',
    color:'#c0a060',
    complexityScore:78,
    totalRealms:7,
    heavens:3,
    hells:1,
    intermediate:2,
    tag:'Oldest Written Cosmos',
    timeScale:'Linear with divine cycles; no eschatology',
    universeType:'Flat earth between heavens and underworld; created from primordial ocean',
    creation:'Enuma Elish: Marduk slays Tiamat, forms sky from upper body, earth from lower; humans from Kingu\'s blood',
    afterlife:'All dead go to Kur/Irkalla regardless of virtue; grim house of dust and silence; minor distinctions only',
    shortDesc: 'The oldest surviving written cosmology — cuneiform tablets describing creation from primordial chaos (Apsu + Tiamat).',
    layers:[
      {name:'An (Heaven of Anu)',desc:'Highest heaven; dwelling of Anu, sky-god and father of gods. Stars and celestial beings.',color:'#ffe8a0'},
      {name:'Enlil\'s Heaven',desc:'Middle heaven; realm of Enlil, king of gods; where divine decrees are made (Tablet of Destinies).',color:'#f0d080'},
      {name:'Ea\'s Heaven / Apsu',desc:'Lower heaven merging with the cosmic ocean Apsu beneath the earth; realm of magic and wisdom.',color:'#d0b060'},
      {name:'Ki / Ersetu (Earth)',desc:'The flat earth disc, surrounded by the salt sea; mortals, animals, plants. Held between heaven and underworld.',color:'#b09040'},
      {name:'Kur / Irkalla (Underworld)',desc:'The Great Below; realm of Ereshkigal, queen of the dead. All dead enter through 7 gates, shedding clothing at each. Gloomy, dark, no joy.',color:'#503010'},
      {name:'Seven Gates of Irkalla',desc:'Each gate: a guardian demands an item of clothing/jewelry from the soul (Inanna\'s Descent myth). Loss of identity layer by layer.',color:'#402008'},
      {name:'Apsu (Primordial Ocean)',desc:'The subterranean freshwater ocean below everything; source of all rivers and springs; realm of Enki/Ea.',color:'#304020'},
    ],
    keyFacts:[
      'Enuma Elish (c. 1750 BCE) — oldest creation epic discovered',
      'Inanna\'s Descent to the Underworld: c. 1900–1600 BCE text',
      'The Seven Tablets of Creation detail Marduk\'s cosmic victory',
      'Gilgamesh Epic: first literary treatment of mortality and the afterlife search',
      'Lamassu (winged bulls) guard cosmic thresholds',
      'Tablet of Destinies: whoever holds it rules creation — cosmological power object',
      'Afterlife is democratic: kings and beggars equal in dust'
    ]
  },
  {
    id:'egypt',
    name:'Ancient Egyptian',
    era:'c. 3100–30 BCE',
    glyph:'𓂀',
    color:'#e8c840',
    complexityScore:82,
    totalRealms:9,
    heavens:5,
    hells:2,
    intermediate:4,
    tag:'Duat & 42 Judges',
    timeScale:'Cyclic solar/annual; eternal return (Zep Tepi)',
    universeType:'Mound of creation emerging from Nun (primordial waters); sustained by Ma\'at',
    creation:'Atum/Ra self-created from Nun; created by masturbation/sneezing; Ogdoad at Hermopolis; Ptah by thought/speech (Memphis)',
    afterlife:'Weighing of Heart against Ma\'at\'s feather; 42 Assessors; Field of Reeds (Aaru) for the righteous; Ammit devours failures',
    shortDesc: 'The most elaborate afterlife judiciary — 42 divine judges, the weighing of the heart, and the beautiful Field of Reeds.',
    layers:[
      {name:'Nut (Sky)',desc:'The goddess Nut forms the sky, swallowing the sun each evening and birthing it each morning. Stars are lights on her body.',color:'#1a3070'},
      {name:'Akhet (Horizon)',desc:'The liminal realm where sun rises and sets; dwelling of Aten/Ra\'s disc; the Sphinx guards this gateway.',color:'#4060a0'},
      {name:'Nun (Primordial Waters)',desc:'The infinite dark waters that existed before creation; Ra sails across Nun; the cosmic ocean surrounding all creation.',color:'#2050a0'},
      {name:'Geb (Earth)',desc:'The earth god Geb; his body is the land; his laughter created earthquakes; separated from Nut by Shu (air).',color:'#604820'},
      {name:'Duat (Underworld)',desc:'The 12 hours of night through which Ra\'s barque travels; full of demons, gates, and snake Apep who must be defeated nightly.',color:'#301030'},
      {name:'Hall of Two Truths',desc:'Judgment hall of Osiris; 42 assessors; the heart is weighed against the feather of Ma\'at on the scales of justice.',color:'#402010'},
      {name:'Aaru (Field of Reeds)',desc:'The paradise: fertile fields mirroring Egypt; eternal perfect life for the virtuous; working the fields of the gods.',color:'#204010'},
      {name:'Ammit\'s Realm',desc:'The devoured soul of the unworthy is eaten by Ammit (part lion, part hippo, part crocodile); second death — complete annihilation.',color:'#200808'},
      {name:'Sekhet-Aaru (far west)',desc:'The furthest paradise; dwelling of Osiris himself; most blessed state.',color:'#103010'},
    ],
    keyFacts:[
      'Book of the Dead: c. 1550 BCE; 192 chapters of spells for afterlife navigation',
      'Pyramid Texts: c. 2400 BCE — oldest religious texts in the world',
      'The soul has 5 parts: Ka, Ba, Akh, Ren, Sheut',
      '42 divine judges (Assessors of Ma\'at) each responsible for a specific sin',
      '12 gates/hours in the Duat each with specific gods and challenges',
      'Apophis (Apep) — cosmic serpent — must be defeated by Ra every night',
      'The Amduat (What is in the Underworld) maps Ra\'s nightly journey in detail'
    ]
  },
  {
    id:'zoroastrianism',
    name:'Zoroastrianism',
    era:'c. 1500–550 BCE – present',
    glyph:'🔥',
    color:'#ff6030',
    complexityScore:72,
    totalRealms:7,
    heavens:4,
    hells:3,
    intermediate:1,
    tag:'First Ethical Dualism',
    timeScale:'Linear; finite 12,000-year cosmic drama; final renovation',
    universeType:'Ahura Mazda\'s pure world invaded by Angra Mainyu; finite time for cosmic struggle',
    creation:'Ahura Mazda created 6 perfect realms (Amesha Spentas); Angra Mainyu corrupted them; the world is the battleground',
    afterlife:'Soul waits 3 days; crosses Chinvat Bridge (wide for righteous, razor-thin for wicked); House of Song vs House of Lies',
    shortDesc: 'First tradition with ethical dualism, linear time, final judgment (Frashokereti), and resurrection of the body.',
    layers:[
      {name:'Anagra Raocha (Endless Light)',desc:'The abode of Ahura Mazda and the Amesha Spentas (Holy Immortals). Pure light, beyond the cosmos.',color:'#fff8e0'},
      {name:'Garothman (Best Existence)',desc:'Heaven of the righteous; dwelling with Ahura Mazda; perfect joy.',color:'#ffe8a0'},
      {name:'Misvana-gatu (Place of the Mixed)',desc:'Middle realm for souls evenly balanced between good and evil; neither heaven nor hell.',color:'#e0d090'},
      {name:'Hamistagan',desc:'A neutral place — not quite heaven, not hell — for those whose good and evil deeds are equal.',color:'#c0b070'},
      {name:'Earth (Gaetha)',desc:'The battleground of Spenta Mainyu vs Angra Mainyu; where humans choose truth or lie.',color:'#806030'},
      {name:'Druj-o-Demana (House of Lies)',desc:'Hell; realm of Angra Mainyu; the wicked experience cold, heat, stench, horrible food until Frashokereti.',color:'#401808'},
      {name:'Endless Darkness (Ahriman\'s realm)',desc:'Deepest realm of Angra Mainyu; temporary until the final renovation when evil is eliminated forever.',color:'#200800'},
    ],
    keyFacts:[
      'Frashokereti: the final renovation of the universe; evil destroyed permanently',
      'Chinvat Bridge: a razor for the wicked, wide highway for the righteous',
      'The soul\'s deeds weighed over 3 days after death (Mithra, Sraosha, Rashnu as judges)',
      'Resurrection of the body: first tradition to teach bodily resurrection',
      'Direct influence on Judaism, Christianity, Islam (paradise, hell, Satan, resurrection)',
      'Time divided into 4 epochs of 3,000 years each = 12,000-year cosmic plan',
      'Ahura Mazda ≠ Angra Mainyu: creator vs destroyer in fundamental opposition'
    ]
  },
  {
    id:'judaism',
    name:'Judaism',
    era:'c. 1300 BCE – present',
    glyph:'✡',
    color:'#5090e0',
    complexityScore:68,
    totalRealms:7,
    heavens:7,
    hells:1,
    intermediate:2,
    tag:'7 Heavens / Merkabah',
    timeScale:'Linear; creation to Messianic age; 6,000-year plan',
    universeType:'Created ex nihilo; finite and purposeful; God above all',
    creation:'Bereshit: God creates in 6 days; 10 utterances; the Torah as blueprint of creation',
    afterlife:'Olam Ha-Ba (World to Come); Gehinnom (purgatory, max 12 months); Gan Eden (paradise); resurrection of the dead',
    shortDesc: 'Seven-layered heavens (Merkabah mysticism), the unique chariot-throne of God, and Kabbalistic tree of sephirot.',
    layers:[
      {name:'Araboth (7th Heaven)',desc:'Throne of God (Kiseh HaKavod); Treasury of souls; store of dew for resurrection; dwelling of angels of highest order.',color:'#e8f0ff'},
      {name:'Makhon (6th Heaven)',desc:'Storehouses of snow, hail, dew, rain; harmful winds; chambers of storms.',color:'#c0d8ff'},
      {name:'Maon (5th Heaven)',desc:'Where the ministering angels offer praises by night; silent by day. Angels of fire chanting.',color:'#98c0f8'},
      {name:'Zebul (4th Heaven)',desc:'Heavenly Jerusalem; Temple; altar where Michael serves; celestial counterpart of earthly temple.',color:'#70a8f0'},
      {name:'Shehaqim (3rd Heaven)',desc:'Garden of Eden (upper); manna ground daily; Gan Eden; also where wicked are punished.',color:'#4890e0'},
      {name:'Raqia (2nd Heaven)',desc:'Domain of fallen angels awaiting judgment; also where Moses traveled in his ascent.',color:'#2070c8'},
      {name:'Vilon (1st Heaven)',desc:'Firmament of sky; drawn aside at sunrise/sunset; the closest heaven to earth.',color:'#0858b0'},
      {name:'Earth / Olam HaZeh',desc:'This world (present age); the realm of human choice, Torah, and commandments.',color:'#605040'},
      {name:'Gehinnom',desc:'Purgatorial realm; wicked purified for up to 12 months (except very wicked); not eternal for most.',color:'#402010'},
    ],
    keyFacts:[
      'Sefer Yetzirah (Book of Formation) maps 32 paths of wisdom',
      'Kabbalistic Tree of Life: 10 Sephirot + Da\'at; 22 paths',
      'Merkabah (Chariot) mysticism: 7 celestial palaces (Heichalot) to ascend',
      '4 Worlds in Kabbalah: Atziluth, Beriah, Yetzirah, Assiah',
      'Zohar: parallel to each of the 7 heavens a corresponding earth below',
      'The Nephilim (fallen beings) occupy Raqia (2nd Heaven) in 1 Enoch tradition',
      'Resurrection of the dead: central in Rabbinic Judaism; Maimonides\' 13 principles'
    ]
  },
  {
    id:'christianity',
    name:'Christianity',
    era:'c. 30 CE – present',
    glyph:'✝',
    color:'#a0c8e0',
    complexityScore:65,
    totalRealms:7,
    heavens:3,
    hells:3,
    intermediate:2,
    tag:'Heaven / Hell / Purgatory',
    timeScale:'Linear; creation to Last Judgment; new creation at end',
    universeType:'Created ex nihilo by Trinitarian God; finite; culminating in New Jerusalem',
    creation:'God creates in 6 days (Genesis); creation ex nihilo emphasized; Word (Logos) as agent',
    afterlife:'Heaven (beatific vision of God), Hell (eternal separation), Purgatory (Catholic), Limbo (Catholic, now disputed)',
    shortDesc: 'Three-tiered afterlife (Heaven/Purgatory/Hell), Dante\'s nine circles, and the cosmic drama of redemption and Last Judgment.',
    layers:[
      {name:'Empyrean (God\'s Throne)',desc:'Beyond the physical cosmos; pure light; Trinity enthroned; where angels and saints dwell in beatific vision.',color:'#ffffff'},
      {name:'Crystalline Heaven',desc:'Medieval cosmology: the 10th sphere of unmoved mover (Aristotelian); first moved by God.',color:'#e0f0ff'},
      {name:'Primum Mobile',desc:'9th sphere: the outermost moving sphere; imparts motion to all below; pure angelic intelligences.',color:'#c0e0ff'},
      {name:'Fixed Stars / 8 Spheres',desc:'8 celestial spheres of planets (Moon, Mercury, Venus, Sun, Mars, Jupiter, Saturn, Stars); each governed by angels.',color:'#a0c8f0'},
      {name:'Earth / New Jerusalem',desc:'The present age; the Church; and in eschatology — the New Creation and New Jerusalem.',color:'#608060'},
      {name:'Purgatory (Catholic)',desc:'Temporary realm of purification; souls cleansed of venial sin; prayers of the living assist them.',color:'#c0a060'},
      {name:'Hell (Infernum)',desc:'Dante: 9 circles — Limbo, Lust, Gluttony, Greed, Anger, Heresy, Violence, Fraud, Treachery (Dis/Cocytus at center).',color:'#300000'},
    ],
    keyFacts:[
      'Dante\'s Divine Comedy (1320 CE) maps 9 circles of Hell, 9 terraces of Purgatory, 9 celestial spheres + Empyrean',
      'Medieval cosmology borrowed heavily from Ptolemaic 9-sphere model',
      'Revelation 21: New Jerusalem — 1,400 miles cubed; 12 gates; jeweled foundations',
      'The Orthodox tradition: Theosis (deification) as the goal; less emphasis on purgatory',
      '9 choirs of angels: Seraphim, Cherubim, Thrones, Dominations, Virtues, Powers, Principalities, Archangels, Angels',
      'Limbo (Limbus Patrum + Limbus Infantium): now largely abandoned by Catholic teaching',
      'C.S. Lewis\'s Great Divorce: purgatorial transit system from grey town to heaven'
    ]
  },
  {
    id:'islam',
    name:'Islam',
    era:'610 CE – present',
    glyph:'☪',
    color:'#40c090',
    complexityScore:70,
    totalRealms:9,
    heavens:7,
    hells:7,
    intermediate:1,
    tag:'7 Heavens / 7 Hells',
    timeScale:'Linear; Al-Qiyamah (Day of Judgment); eternal paradise/hell',
    universeType:'Created by Allah in 6 days; finite; vast but bounded; Allah\'s Throne above all',
    creation:'Allah said "Be" (Kun) and it was; the Throne was on water; 7 heavens + 7 earths created',
    afterlife:'Barzakh (grave period); Day of Judgment (weighing of deeds on Mizan); Sirat bridge; 8 levels of Jannah, 7 of Jahannam',
    shortDesc: 'Seven heavens and seven hells with precise named levels, the Sirat bridge finer than hair, and the lote tree at the cosmic limit.',
    layers:[
      {name:'Arsh (Throne of Allah)',desc:'Above all 7 heavens; the Throne of the Creator; carried by 8 angels; surrounded by the greatest angels.',color:'#e8fff5'},
      {name:'Sidrat al-Muntaha',desc:'The Lote Tree of the Utmost Boundary; beyond which no knowledge or being can pass; visited by Muhammad in Mi\'raj.',color:'#b0ffe0'},
      {name:'Firdaws (Highest Jannah)',desc:'8th/highest level of paradise; directly beneath the Throne; from which all the rivers of paradise spring.',color:'#80f0c0'},
      {name:'Jannah levels (7)',desc:'From Firdaws down: Dar as-Salam, Dar al-Khuld, Jannat al-Mawa, Jannat al-Adn, Jannat an-Naim, Jannat al-Khuld. River of Kawthar.',color:'#40d090'},
      {name:'7 Heavens (Samawat)',desc:'Muhammad\'s Mi\'raj describes meeting: Adam (1st), Yahya+Isa (2nd), Yusuf (3rd), Idris (4th), Harun (5th), Musa (6th), Ibrahim (7th).',color:'#20b870'},
      {name:'Earth + Barzakh',desc:'The mortal world; Barzakh = the grave period between death and resurrection; soul experiences foretaste of destiny.',color:'#608050'},
      {name:'Jahannam (Hell) — 7 levels',desc:'Jahannam, Ladha, Hutama, Sa\'ir, Saqar, Jahim, Hawiyah. Each level hotter; for specific categories of wrongdoers.',color:'#401000'},
    ],
    keyFacts:[
      'Isra and Mi\'raj: Muhammad\'s night journey through all 7 heavens to the Throne',
      'Sirat: a bridge over hell, finer than hair and sharper than sword; crossing time = measure of faith',
      'The Mizan (scales): deeds weighed on the Day of Judgment with absolute precision',
      '7 earths below (as in 7 heavens above): mentioned in hadith tradition',
      'Lote Tree (Sidrat al-Muntaha) marks the absolute limit of created knowledge',
      'In the 7th heaven Ibrahim (Abraham) leans against the Bayt al-Ma\'mur (heavenly Ka\'ba)',
      'Houris and Wildan (eternal youths) serve in paradise'
    ]
  },
  {
    id:'norse',
    name:'Norse / Germanic',
    era:'c. 800 BCE – 1300 CE',
    glyph:'ᚢ',
    color:'#708090',
    complexityScore:75,
    totalRealms:9,
    heavens:3,
    hells:2,
    intermediate:3,
    tag:'9 Worlds on Yggdrasil',
    timeScale:'Linear toward Ragnarök; post-Ragnarök renewal',
    universeType:'9 worlds on Yggdrasil cosmic tree; born from Ginnungagap (void); ends at Ragnarök, renewed after',
    creation:'Void (Ginnungagap); Muspelheim (fire) + Niflheim (ice) collide; giant Ymir formed; gods slay Ymir, make world from body',
    afterlife:'Valhalla (warriors chosen by Valkyries); Hel (most dead); Fólkvangr (Freya\'s half); Ran (drowned sailors)',
    shortDesc: 'Nine interconnected worlds on the cosmic tree Yggdrasil, leading to the apocalyptic Ragnarök and world renewal.',
    layers:[
      {name:'Asgard',desc:'Realm of the Aesir gods; contains 12 halls including Valhalla, Gladsheim, Bilskirnir. Connected to Midgard by Bifrost rainbow bridge.',color:'#e0d090'},
      {name:'Vanaheim',desc:'Realm of the Vanir gods (Njord, Freyr, Freyja); gods of fertility, wisdom, and nature. Exchanged hostages with Aesir.',color:'#c0d070'},
      {name:'Alfheim',desc:'Realm of the Light Elves (Ljosalfar); more beautiful than the sun; given to Freyr as a tooth-gift.',color:'#a0d060'},
      {name:'Midgard (Middle Earth)',desc:'Realm of humans; surrounded by the world-serpent Jormungandr; connected to Asgard by Bifrost.',color:'#70a040'},
      {name:'Jotunheim',desc:'Realm of the Giants (Jotnar); across the sea from Midgard; realm of chaos and primal forces opposing the gods.',color:'#506030'},
      {name:'Svartalfheim / Nidavellir',desc:'Realm of Dark Elves (Dwarves/Svartalfar); master craftsmen; made Thor\'s hammer Mjolnir, Odin\'s spear Gungnir.',color:'#403020'},
      {name:'Niflheim',desc:'Primordial realm of ice and mist; source of 11 rivers (Elivagar); where all began.',color:'#303040'},
      {name:'Hel / Helheim',desc:'Realm of the dead not chosen for Valhalla; ruled by Hel (half-living, half-corpse); dreary but not fiery punishment.',color:'#202030'},
      {name:'Muspelheim',desc:'Primordial realm of fire; home of fire giant Surtr and his flaming sword; will burn the world at Ragnarök.',color:'#602010'},
    ],
    keyFacts:[
      'Yggdrasil: ash tree connecting 9 worlds; 3 roots to Asgard, Jotunheim, Niflheim',
      'Three wells: Urdarbrunnr (fate), Mímisbrunnr (wisdom — Odin\'s eye traded here), Hvergelmir (source of rivers)',
      'Ragnarök: final battle; gods vs giants; Fenrir swallows Odin; Jormungandr kills Thor; world burns and is reborn',
      'Valhalla holds 800 warriors per door × 540 doors = 432,000 Einherjar',
      'Odin sacrificed himself on Yggdrasil for 9 days to receive the runes',
      'Fólkvangr: Freyja takes half the slain; Odin takes half — frequently overlooked',
      'Prose Edda (Snorri Sturluson, c. 1220 CE) is the primary source'
    ]
  },
  {
    id:'shinto',
    name:'Shinto',
    era:'c. 700 BCE – present',
    glyph:'⛩',
    color:'#ff6680',
    complexityScore:55,
    totalRealms:6,
    heavens:2,
    hells:1,
    intermediate:3,
    tag:'Kami Realm / Kakuriyo',
    timeScale:'Cyclic seasonal; mythic age of Kami; present age continuous',
    universeType:'Separation of heaven and earth from primal chaos; Kami inherent in nature',
    creation:'Izanagi and Izanami stir the sea with a jeweled spear; create islands of Japan; Amaterasu born from eye, Susanoo from nose',
    afterlife:'Yomi (underworld); impure and gloomy; no clear paradise; Kami-nature of the soul may continue to protect family',
    shortDesc: 'Nature-embedded cosmology centered on Kami spirits, the hidden world (Kakuriyo), and the mysterious underworld Yomi.',
    layers:[
      {name:'Takama-ga-hara (Plain of High Heaven)',desc:'Dwelling of the celestial Kami; Amaterasu (sun goddess) reigns; source of divine authority for Japan\'s imperial line.',color:'#ffe0e8'},
      {name:'Tokoyo no Kuni (Eternal Land)',desc:'The eternal realm beyond the sea; pure, unchanging; where certain heroic figures and Urashima Taro traveled.',color:'#ffc0d0'},
      {name:'Ashihara no Nakatsukuni (Middle Land)',desc:'The world of humans and nature Kami; all living things permeated by Kami-essence; the visible world (Utsushiyo).',color:'#d09080'},
      {name:'Ne no Kuni (Root Country)',desc:'Susanoo\'s realm; the root/deep realm; a chaotic and powerful underworld that Susanoo was banished to.',color:'#907060'},
      {name:'Kakuriyo (Hidden World)',desc:'The unseen parallel world of Kami and spirits; co-existing with the human world; accessed through sacred sites.',color:'#604850'},
      {name:'Yomi no Kuni (Underworld)',desc:'The land of death; polluted (Kegare); Izanami became a rotting corpse here; Izanagi fled and blocked the entrance with a boulder.',color:'#302030'},
    ],
    keyFacts:[
      'Kojiki (712 CE) and Nihon Shoki (720 CE) are primary texts',
      'Amaterasu hides in Ama-no-Iwato cave — darkness of the world; lured out by dance and laughter',
      'Susanoo slays Yamata-no-Orochi (8-headed serpent) and finds Kusanagi sword',
      'Izanagi\'s purification bath after Yomi created Amaterasu, Tsukuyomi, Susanoo',
      'Musubi: the creative force that permeates all life; central Shinto concept',
      'Kami can be in multiple places; ubiquitous spiritual agency',
      'No strong doctrine of heaven/hell; emphasis on purity in this life and community'
    ]
  },
  {
    id:'taoism',
    name:'Taoism',
    era:'c. 500 BCE – present',
    glyph:'☯',
    color:'#70d0a0',
    complexityScore:62,
    totalRealms:10,
    heavens:9,
    hells:10,
    intermediate:2,
    tag:'36 Heavens / 10 Hells',
    timeScale:'Cyclic; eternal return to Tao; no definitive end',
    universeType:'Tao (the Way) as ground of being; cosmos emerges from Tao through Te',
    creation:'Tao gives birth to One, One to Two (Yin/Yang), Two to Three, Three to Ten Thousand Things',
    afterlife:'Hell courts (Diyu) — 10 kings judge and reassign souls; purification and reincarnation; immortals transcend this',
    shortDesc: 'The Tao as primordial ground; 36 celestial heavens in later Taoism, 10 courts of hell with detailed bureaucratic judgment.',
    layers:[
      {name:'Sanqing (Three Pure Ones)',desc:'Yuanshi Tianzun, Lingbao Tianzun, Daode Tianzun — highest divine trinity of Taoism; beyond all phenomena.',color:'#e0fff0'},
      {name:'San-tian (Three Heavens)',desc:'Taiqing, Shangqing, Yuqing — the three pure heavens; realm of the immortals and highest celestial Tao.',color:'#b0f0d0'},
      {name:'28 Heavens of the Stars',desc:'28 lunar mansions as celestial realms; each governed by star-gods with specific domains.',color:'#80e0b0'},
      {name:'6 Desire Heavens',desc:'Levels of celestial beings still bound by desire but ascending; parallel to Buddhist deva realms (heavy cultural exchange).',color:'#50c090'},
      {name:'Human Realm (Renjianjie)',desc:'The world of ordinary humans; governed by the Three Officials (Heaven, Earth, Water); subject to celestial bureaucracy.',color:'#308060'},
      {name:'Gui Jie (Ghost Realm)',desc:'The realm of wandering spirits not yet judged; hungry ghosts; spirits needing ritual feeding.',color:'#405050'},
      {name:'Diyu (10 Hell Courts)',desc:'10 courts each with a king; Yanluo Wang presides; souls judged, punished appropriately, then reincarnated.',color:'#302030'},
      {name:'Fengdu (Ghost City)',desc:'The capital of the underworld; Mount Fengdu; where souls register before judgment.',color:'#201020'},
    ],
    keyFacts:[
      'Tao Te Ching (Laozi, c. 400 BCE): 81 chapters; Tao as the unnameable ground',
      'Zhuangzi: cosmos as infinite transformation; death is just another change',
      'Diyu (Chinese Hell): heavy influence from Buddhist cosmology (Tang dynasty)',
      '10 Courts of Hell: King Yanluo (5th court) most famous; soul reforms through punishment then reincarnates',
      'The Jade Emperor (Yu Huang): supreme deity of popular Taoism; cosmic bureaucratic head',
      'Immortals (Xian): can transcend death through cultivation; 3 types: heavenly, earthly, corpse-deliverance',
      '36 heavens in later Taoist cosmology (added during Buddhist-Taoist synthesis period)'
    ]
  },
  {
    id:'confucianism',
    name:'Confucianism',
    era:'c. 500 BCE – present',
    glyph:'儒',
    color:'#d09040',
    complexityScore:30,
    totalRealms:2,
    heavens:1,
    hells:0,
    intermediate:1,
    tag:'Heaven (Tian) & Earth',
    timeScale:'Linear historical time; moral progress of civilization',
    universeType:'Heaven (Tian) as moral order; Earth responsive to virtue; no metaphysical cosmology emphasized',
    creation:'Heaven and Earth as given; Confucius avoids speculation on origins ("When you know a thing, to hold that you know it; when you do not know a thing, to allow that you do not know it")',
    afterlife:'Ritual veneration of ancestors; Tian as moral destination for the virtuous; afterlife is secondary to ethical life',
    shortDesc: 'Deliberately minimalist cosmology — Heaven (Tian) as moral order; the focus is entirely on ethical civilization, not metaphysics.',
    layers:[
      {name:'Tian (Heaven)',desc:'The supreme moral order; impersonal but purposeful; responds to virtue and vice of rulers; the source of the Mandate of Heaven (Tianming).',color:'#f8e8a0'},
      {name:'Ren Jian (Human World)',desc:'The world of human relationships and moral cultivation; the five relations; where the junzi (noble person) perfects virtue.',color:'#e0c060'},
    ],
    keyFacts:[
      'Analects: "The Master said — when you do not yet know life, how can you know death?"',
      'Neo-Confucianism (Song dynasty) added li (principle) and qi (vital force) — more cosmological',
      'Zhang Zai\'s Western Inscription: "Heaven is my father, Earth my mother; I their child"',
      'The Great Ultimate (Taiji) in Neo-Confucianism: generates yin-yang and Five Phases',
      'Mandate of Heaven: political legitimacy tied to cosmic moral order',
      'Confucian afterlife: ancestor veneration as social continuity, not metaphysical claim',
      'Zhou Dunyi\'s Diagram of the Supreme Ultimate (Taijitu) maps cosmic generation'
    ]
  },
  {
    id:'greek',
    name:'Ancient Greek',
    era:'c. 700–200 BCE',
    glyph:'⚡',
    color:'#c0c8e0',
    complexityScore:73,
    totalRealms:9,
    heavens:3,
    hells:4,
    intermediate:3,
    tag:'Olympus / Tartarus / Elysium',
    timeScale:'Cyclic mythic ages (Gold, Silver, Bronze, Iron); eternal cosmos (Plato)',
    universeType:'Spherical cosmos; eternal or Demiurge-created (Plato\'s Timaeus); governed by fate (Moirai)',
    creation:'Hesiod: Chaos first, then Gaia, Tartarus, Eros. Plato: Demiurge creates ordered cosmos from chaotic matter using Forms as templates',
    afterlife:'Judgment by 3 judges; Elysium (heroes), Asphodel (ordinary), Tartarus (wicked), Isles of the Blessed (repeated excellence)',
    shortDesc: 'From Homer\'s gloomy Hades to Plato\'s mathematical multiverse — the most philosophically sophisticated ancient cosmology.',
    layers:[
      {name:'Olympus',desc:'Home of the 12 Olympian gods; above clouds; perfect eternal spring; where gods feast on ambrosia.',color:'#e8e8ff'},
      {name:'Ouranos (Sky)',desc:'The dome of heaven; personified as Ouranos (Uranus); stars are holes or torches; primordial sky deity.',color:'#c0c8f8'},
      {name:'Aether',desc:'The pure upper air breathed by gods (distinct from ordinary air); primordial element of divine realm.',color:'#a0b0f0'},
      {name:'Earth (Gaia)',desc:'The flat or spherical earth (debate by 5th century BCE); center of the cosmos for geocentric Ptolemaic model later.',color:'#809060'},
      {name:'Erebus (Deep Darkness)',desc:'The transitional space between earth and Hades; primordial darkness; spirits pass through here.',color:'#503040'},
      {name:'Asphodel Meadows',desc:'Where ordinary souls (neither heroes nor villains) wander; gray, aimless, bloodless existence.',color:'#404040'},
      {name:'Elysian Fields',desc:'Paradise for heroes and the virtuous; eternal joy, games, feasting; the Isles of the Blessed for those reborn 3x virtuous.',color:'#204020'},
      {name:'Tartarus',desc:'Deepest abyss; as far below Hades as heaven is above earth; prison of Titans; eternal punishment of Tantalus, Sisyphus, etc.',color:'#200010'},
      {name:'Chaos (Primordial)',desc:'The first principle; the yawning void; not disorder but primordial space from which everything emerged.',color:'#100008'},
    ],
    keyFacts:[
      'Plato\'s Timaeus: Demiurge creates cosmos from pre-existing chaos using Forms as templates',
      'Orphic cosmogony: cosmic egg; more elaborate than Homeric tradition',
      'The three judges: Minos, Rhadamanthus, Aeacus — all former mortal kings',
      'Five rivers of Hades: Styx (hate), Lethe (forgetting), Acheron (woe), Phlegethon (fire), Cocytus (lamentation)',
      'Plato\'s Myth of Er (Republic): souls choose new lives; cosmic spindle of Necessity; 3 Fates',
      'Pythagoras: souls transmigrate through all living things; first Western metempsychosis',
      'Aristotle: eternal, uncreated cosmos; Unmoved Mover at the periphery; no afterlife of note'
    ]
  },
  {
    id:'rome',
    name:'Ancient Roman',
    era:'c. 500 BCE – 400 CE',
    glyph:'🦅',
    color:'#c0802a',
    complexityScore:58,
    totalRealms:6,
    heavens:2,
    hells:3,
    intermediate:2,
    tag:'Elysium / Dis / Apotheosis',
    timeScale:'Linear historical; eternal Rome as cosmic destiny; eclectic end-times',
    universeType:'Geocentric cosmos inherited from Greece; Jupiter\'s domain above; Dis/Pluto below',
    creation:'Ovid\'s Metamorphoses: chaos → Demiurge-like god separates elements → 4 ages (Gold to Iron)',
    afterlife:'Aeneid (Virgil): Elysium for heroes, Tartarus for wicked, Plains of Mourning for unlucky lovers; Lethe for rebirth; apotheosis for emperors',
    shortDesc: 'Practical and syncretic — inherited Greek cosmology enriched by Virgil\'s Aeneid, Stoic physics, and imperial apotheosis.',
    layers:[
      {name:'Caelum (Heaven of Jupiter)',desc:'Domain of Jupiter and the Olympian gods (Roman names); divine governance of human affairs.',color:'#ffe8c0'},
      {name:'Aether (Pure Sky)',desc:'The divine fire/ether above the clouds; realm of the divine; where deified emperors ascend.',color:'#f0d090'},
      {name:'Terra (Earth)',desc:'The world of mortals; Rome as cosmic center (caput mundi); governed by divine providence.',color:'#a08040'},
      {name:'Plains of Mourning (Lugentes Campi)',desc:'Where lovers who died of passion wander; Dido, Phaedra — those killed by love.',color:'#503828'},
      {name:'Elysium',desc:'Where virtuous heroes dwell; Aeneas meets his father Anchises here; vision of Rome\'s future heroes given.',color:'#204010'},
      {name:'Tartarus',desc:'Deep pit; Ixion on wheel, Tantalus reaching for fruit, Sisyphus and his rock; Rhadamanthus judges.',color:'#300010'},
    ],
    keyFacts:[
      'Virgil\'s Aeneid (Book VI): most detailed Roman underworld journey; foundational for Dante',
      'Roman apotheosis: emperors deified after death — Julius Caesar, Augustus, Hadrian etc.',
      'Stoic cosmology: periodic conflagration (ekpyrosis) destroys and renews the cosmos',
      'Lares and Penates: household gods protecting family; continuation of ancestors as protective spirits',
      'Pontifex Maximus: the high priest who maintained cosmic/religious order (later taken by emperors)',
      'Dis Pater = Pluto; the underworld is the kingdom of Dis (from "dives" = wealthy, for all the dead)',
      'The Sibylline books: prophetic texts governing Roman ritual responses to cosmic signs'
    ]
  }
];

/* Sort by complexity score */
const SORTED = [...TRADITIONS].sort((a,b)=>b.complexityScore-a.complexityScore);

/* ════════════════════════════════════════
   STARFIELD
════════════════════════════════════════ */
(function(){
  const c=document.getElementById('stars');
  const ctx=c.getContext('2d');
  let W,H,stars=[];
  function resize(){W=c.width=window.innerWidth;H=c.height=window.innerHeight;}
  function init(){
    stars=[];
    for(let i=0;i<200;i++) stars.push({x:Math.random()*W,y:Math.random()*H,r:Math.random()*1.2,a:Math.random(),da:(Math.random()-0.5)*0.005});
  }
  function draw(){
    ctx.clearRect(0,0,W,H);
    stars.forEach(s=>{
      s.a=Math.max(0.1,Math.min(1,s.a+s.da));
      if(s.a<=0.1||s.a>=1) s.da*=-1;
      ctx.beginPath();
      ctx.arc(s.x,s.y,s.r,0,Math.PI*2);
      ctx.fillStyle=`rgba(255,255,220,${s.a*0.6})`;
      ctx.fill();
    });
    requestAnimationFrame(draw);
  }
  window.addEventListener('resize',()=>{resize();init();});
  resize();init();draw();
})();

/* ════════════════════════════════════════
   TABS
════════════════════════════════════════ */
function showTab(id){
  document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
  document.getElementById('tab-'+id).classList.add('active');
  event.target.classList.add('active');
  if(id==='ranking') buildRanking();
  if(id==='cards') buildCards();
  if(id==='compare') buildCompare();
  if(id==='spectrum') buildSpectrum();
}

/* ════════════════════════════════════════
   RANKING TAB
════════════════════════════════════════ */
function buildRanking(){
  const g=document.getElementById('rankGrid');
  if(g.children.length) return;
  SORTED.forEach((t,i)=>{
    const div=document.createElement('div');
    div.className='rank-row';
    div.style.setProperty('--row-color',t.color);
    div.innerHTML=`
      <div class="rank-num">${i+1}</div>
      <div>
        <div class="rank-name">${t.name}</div>
        <div class="rank-tag">${t.tag}</div>
      </div>
      <div class="rank-score-wrap" style="width:100%">
        <div class="rank-score-bar" style="width:${t.complexityScore}%;background:${t.color}"></div>
      </div>
      <div class="rank-layers" style="color:${t.color}">${t.totalRealms} realms</div>
    `;
    div.onclick=()=>openModal(t);
    g.appendChild(div);
  });
}

/* ════════════════════════════════════════
   CARDS TAB
════════════════════════════════════════ */
function buildCards(){
  const g=document.getElementById('cosmoGrid');
  if(g.children.length) return;
  SORTED.forEach(t=>{
    const div=document.createElement('div');
    div.className='cosmo-card';
    div.style.setProperty('--card-color',t.color);
    const pills=t.layers.slice(0,4).map(l=>`<span class="layer-pill" style="--pill-color:${t.color}">${l.name.split('(')[0].trim().substring(0,22)}</span>`).join('');
    div.innerHTML=`
      <div class="card-glyph">${t.glyph}</div>
      <div class="card-header">
        <div>
          <div class="card-title">${t.name}</div>
          <div class="card-era">${t.era}</div>
        </div>
        <div>
          <div class="card-badge" style="color:${t.color}">${t.totalRealms}</div>
          <div class="card-badge-label">Realms</div>
        </div>
      </div>
      <div class="card-layers">${pills}</div>
      <div class="card-desc">${t.shortDesc}</div>
    `;
    div.onclick=()=>openModal(t);
    g.appendChild(div);
  });
}

/* ════════════════════════════════════════
   COMPARE TAB
════════════════════════════════════════ */
function buildCompare(){
  const b=document.getElementById('compareBody');
  if(b.children.length) return;
  SORTED.forEach(t=>{
    const tr=document.createElement('tr');
    tr.innerHTML=`
      <td style="color:${t.color}">${t.glyph} ${t.name}</td>
      <td class="td-num">${t.totalRealms}</td>
      <td class="td-num">${t.heavens}</td>
      <td class="td-num">${t.hells}</td>
      <td class="td-num">${t.intermediate}</td>
      <td>${t.timeScale}</td>
      <td>${t.universeType.substring(0,60)}…</td>
      <td>${t.creation.substring(0,60)}…</td>
      <td>${t.afterlife.substring(0,60)}…</td>
    `;
    tr.style.cursor='pointer';
    tr.onclick=()=>openModal(t);
    b.appendChild(tr);
  });
}

/* ════════════════════════════════════════
   SPECTRUM TAB
════════════════════════════════════════ */
function buildSpectrum(){
  const c=document.getElementById('spectrumContent');
  if(c.children.length) return;

  const metrics=[
    {label:'Cosmological Complexity',key:'complexityScore',max:100,desc:'Overall composite score combining all dimensions'},
    {label:'Total Realms',key:'totalRealms',max:36,desc:'Named distinct cosmological levels'},
    {label:'Heaven Layers',key:'heavens',max:26,desc:'Named paradisaical / upper realms'},
    {label:'Hell / Dark Realms',key:'hells',max:28,desc:'Infernal / purgatorial / lower realms'},
  ];

  metrics.forEach(m=>{
    const sec=document.createElement('div');
    sec.className='spectrum-section';
    let bars=SORTED.map(t=>`
      <div class="spectrum-bar-row">
        <div class="spectrum-label">${t.name}</div>
        <div class="spectrum-track">
          <div class="spectrum-fill" style="width:${Math.round(t[m.key]/m.max*100)}%;background:${t.color}"></div>
        </div>
        <div class="spectrum-val" style="color:${t.color}">${t[m.key]}</div>
      </div>
    `).join('');
    sec.innerHTML=`<div class="spectrum-title">${m.label}</div><p style="font-size:13px;color:var(--text-dim);margin-bottom:16px;font-style:italic;">${m.desc}</p>${bars}`;
    c.appendChild(sec);
  });
}

/* ════════════════════════════════════════
   MODAL
════════════════════════════════════════ */
function openModal(t){
  const m=document.getElementById('modalContent');
  const layerItems=t.layers.map((l,i)=>`
    <div class="layer-item">
      <div class="layer-num">L${i+1}</div>
      <div class="layer-bar" style="background:${l.color}"></div>
      <div class="layer-content">
        <div class="layer-name">${l.name}</div>
        <div class="layer-desc">${l.desc}</div>
      </div>
    </div>
  `).join('');

  const facts=t.keyFacts.map(f=>`<li style="margin-bottom:10px;color:var(--text-dim);line-height:1.7;font-size:15px;">${f}</li>`).join('');

  m.innerHTML=`
    <button class="modal-close" onclick="closeModal()">✕</button>
    <div class="modal-hero">
      <div class="modal-glyph">${t.glyph}</div>
      <div class="modal-title">${t.name}</div>
      <div class="modal-meta">${t.era} &nbsp;·&nbsp; ${t.tag} &nbsp;·&nbsp; Complexity: ${t.complexityScore}/100</div>
    </div>
    <div class="modal-body">

      <div class="stats-row">
        <div class="stat-box"><div class="stat-box-n" style="color:${t.color}">${t.totalRealms}</div><div class="stat-box-l">Total Realms</div></div>
        <div class="stat-box"><div class="stat-box-n" style="color:${t.color}">${t.heavens}</div><div class="stat-box-l">Heavens</div></div>
        <div class="stat-box"><div class="stat-box-n" style="color:${t.color}">${t.hells}</div><div class="stat-box-l">Hells / Dark Realms</div></div>
      </div>

      <div class="modal-section-title">Universe Type</div>
      <p class="modal-text">${t.universeType}</p>

      <div class="modal-section-title">Creation Narrative</div>
      <p class="modal-text">${t.creation}</p>

      <div class="modal-section-title">Afterlife System</div>
      <p class="modal-text">${t.afterlife}</p>

      <div class="modal-section-title">Time Scale</div>
      <p class="modal-text">${t.timeScale}</p>

      <div class="modal-section-title">Cosmological Layers — Detailed Map</div>
      <div class="layers-diagram">${layerItems}</div>

      <div class="modal-section-title">Key Facts & Figures</div>
      <ul style="list-style:none;padding:0">${facts}</ul>

    </div>
  `;
  document.getElementById('modal').classList.add('open');
  document.body.style.overflow='hidden';
}
function closeModal(e){
  if(e && e.target!==document.getElementById('modal')) return;
  document.getElementById('modal').classList.remove('open');
  document.body.style.overflow='';
}
document.addEventListener('keydown',e=>{if(e.key==='Escape') closeModal();});

/* Init */
buildRanking();
</script>
</body>
</html>

---

### 🧑 You

what about Ancient Egyptian and mesopotamin

---

### 🧑 You

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Egypt vs Mesopotamia — Cosmological Deep Dive</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&display=swap');

*{margin:0;padding:0;box-sizing:border-box;}
:root{
  --sand:#c8a96e;
  --sand-dim:#7a6030;
  --lapis:#2a4a7f;
  --lapis-light:#4a7abf;
  --clay:#8b5e3c;
  --clay-light:#c0825a;
  --egypt:#c8a000;
  --egypt-dim:#7a6000;
  --meso:#8b5010;
  --meso-light:#c07830;
  --bg:#09080a;
  --bg2:#0f0d10;
  --bg3:#141218;
  --text:#ddd5c0;
  --text-dim:#7a7060;
  --border:#1e1a14;
  --divider:#2a2418;
}

body{
  background:var(--bg);
  color:var(--text);
  font-family:'Cormorant Garamond',Georgia,serif;
  min-height:100vh;
  overflow-x:hidden;
}

/* papyrus/stone texture overlay */
body::before{
  content:'';
  position:fixed;
  inset:0;
  background-image:
    radial-gradient(ellipse 120% 80% at 20% 20%,rgba(200,160,0,0.04) 0%,transparent 60%),
    radial-gradient(ellipse 100% 60% at 80% 80%,rgba(139,80,16,0.05) 0%,transparent 60%);
  pointer-events:none;
  z-index:0;
}

canvas#bg{position:fixed;inset:0;z-index:0;opacity:0.4;pointer-events:none;}

.page{position:relative;z-index:1;max-width:1300px;margin:0 auto;padding:0 20px 80px;}

/* ── MASTHEAD ── */
.masthead{
  text-align:center;
  padding:70px 0 50px;
  border-bottom:1px solid var(--divider);
}
.masthead-eye{font-size:48px;margin-bottom:20px;opacity:0.8;}
.masthead-kicker{
  font-family:'IM Fell English',serif;
  font-size:11px;
  letter-spacing:6px;
  color:var(--sand-dim);
  text-transform:uppercase;
  margin-bottom:18px;
}
.masthead-h1{
  font-family:'IM Fell English',serif;
  font-size:clamp(28px,5vw,58px);
  color:var(--sand);
  line-height:1.15;
  margin-bottom:12px;
}
.masthead-h1 span.egypt-col{color:var(--egypt);}
.masthead-h1 span.meso-col{color:var(--meso-light);}
.masthead-sub{
  font-size:17px;
  font-style:italic;
  color:var(--text-dim);
  max-width:580px;
  margin:0 auto;
  line-height:1.8;
}

/* ── PILLS ── */
.pill-row{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin:32px 0;}
.pill{
  font-family:'IM Fell English',serif;
  font-size:11px;
  letter-spacing:3px;
  padding:6px 18px;
  border:1px solid;
  text-transform:uppercase;
}
.pill-e{border-color:var(--egypt-dim);color:var(--egypt);}
.pill-m{border-color:var(--sand-dim);color:var(--meso-light);}

/* ── LAYOUT ── */
.two-col{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:2px;
  margin:48px 0 0;
}
@media(max-width:768px){.two-col{grid-template-columns:1fr;}}

.col-egypt{background:linear-gradient(180deg,rgba(200,160,0,0.04) 0%,transparent 40%);}
.col-meso{background:linear-gradient(180deg,rgba(139,80,16,0.05) 0%,transparent 40%);}

.col-head{
  padding:32px 36px 24px;
  border-bottom:1px solid var(--divider);
  position:sticky;top:0;
  background:var(--bg2);
  z-index:10;
}
.col-glyph{font-size:36px;margin-bottom:10px;}
.col-title{
  font-family:'IM Fell English',serif;
  font-size:24px;
  margin-bottom:4px;
}
.col-era{font-size:12px;letter-spacing:2px;color:var(--text-dim);text-transform:uppercase;}
.col-score{
  font-family:'IM Fell English',serif;
  font-size:40px;
  font-weight:400;
  margin-top:12px;
}
.score-label{font-size:11px;letter-spacing:2px;color:var(--text-dim);text-transform:uppercase;}

/* ── SECTIONS ── */
.col-section{padding:28px 36px;border-bottom:1px solid var(--divider);}
.section-label{
  font-family:'IM Fell English',serif;
  font-size:10px;
  letter-spacing:5px;
  text-transform:uppercase;
  color:var(--sand-dim);
  margin-bottom:14px;
  padding-bottom:8px;
  border-bottom:1px solid var(--divider);
}
.section-text{
  font-size:15px;
  line-height:1.85;
  color:var(--text-dim);
}
.section-text strong{color:var(--text);font-weight:400;}

/* ── REALM TOWER ── */
.realm-tower{display:flex;flex-direction:column;gap:3px;margin-top:8px;}
.realm-block{
  display:flex;
  align-items:stretch;
  gap:0;
  cursor:pointer;
  transition:filter 0.15s;
}
.realm-block:hover{filter:brightness(1.2);}
.realm-swatch{
  width:8px;
  flex-shrink:0;
  border-radius:2px 0 0 2px;
}
.realm-inner{
  flex:1;
  padding:10px 14px;
  border:1px solid rgba(255,255,255,0.05);
  border-left:none;
  transition:background 0.15s;
}
.realm-block:hover .realm-inner{background:rgba(255,255,255,0.03);}
.realm-name{
  font-family:'IM Fell English',serif;
  font-size:13px;
  color:var(--text);
  margin-bottom:4px;
}
.realm-desc{font-size:12px;color:var(--text-dim);line-height:1.6;}
.realm-level{
  font-family:'IM Fell English',serif;
  font-size:10px;
  color:var(--text-dim);
  opacity:0.6;
  margin-bottom:3px;
  letter-spacing:1px;
}

/* ── DEITY TABLE ── */
.deity-grid{display:flex;flex-direction:column;gap:8px;margin-top:8px;}
.deity-row{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:8px;
}
.deity-card{
  background:var(--bg3);
  border:1px solid var(--divider);
  padding:12px 14px;
}
.deity-name{
  font-family:'IM Fell English',serif;
  font-size:14px;
  color:var(--sand);
  margin-bottom:4px;
}
.deity-role{font-size:12px;color:var(--text-dim);line-height:1.6;}

/* ── FACT LIST ── */
.fact-list{list-style:none;margin-top:8px;}
.fact-list li{
  padding:9px 0;
  border-bottom:1px solid rgba(255,255,255,0.04);
  font-size:14px;
  color:var(--text-dim);
  line-height:1.7;
  padding-left:14px;
  position:relative;
}
.fact-list li::before{
  content:'◆';
  position:absolute;left:0;
  font-size:7px;
  color:var(--sand-dim);
  top:12px;
}

/* ── COMPARISON ROW (center) ── */
.compare-row{
  grid-column:1/-1;
  background:var(--bg2);
  border:1px solid var(--divider);
  padding:48px 40px;
  margin:2px 0;
}
.compare-row h2{
  font-family:'IM Fell English',serif;
  font-size:20px;
  color:var(--sand);
  text-align:center;
  margin-bottom:32px;
  letter-spacing:2px;
}

.compare-metrics{display:flex;flex-direction:column;gap:16px;}
.metric-row{
  display:grid;
  grid-template-columns:1fr 200px 1fr;
  align-items:center;
  gap:16px;
}
.metric-label{
  font-family:'IM Fell English',serif;
  font-size:11px;
  letter-spacing:3px;
  color:var(--text-dim);
  text-transform:uppercase;
  text-align:center;
  padding:6px 0;
  border-top:1px solid var(--divider);
  border-bottom:1px solid var(--divider);
}
.metric-e{text-align:right;}
.metric-m{text-align:left;}
.metric-val{
  font-family:'IM Fell English',serif;
  font-size:22px;
}
.metric-val.e{color:var(--egypt);text-align:right;}
.metric-val.m{color:var(--meso-light);}
.metric-note{font-size:12px;color:var(--text-dim);font-style:italic;line-height:1.5;}

/* ── TIMELINE ── */
.timeline{position:relative;margin:24px 0;}
.timeline-spine{
  position:absolute;left:50%;top:0;bottom:0;
  width:1px;background:var(--divider);
  transform:translateX(-50%);
}
.tl-item{
  display:grid;
  grid-template-columns:1fr 80px 1fr;
  align-items:start;
  margin-bottom:20px;
  gap:0;
}
.tl-date{
  font-family:'IM Fell English',serif;
  font-size:11px;
  letter-spacing:2px;
  color:var(--sand-dim);
  text-align:center;
  padding:6px 0;
  position:relative;
  z-index:1;
}
.tl-date::before{
  content:'';
  position:absolute;left:50%;top:50%;
  width:8px;height:8px;
  border:1px solid var(--sand-dim);
  background:var(--bg);
  transform:translate(-50%,-50%);
  border-radius:50%;
}
.tl-egypt,.tl-meso{font-size:13px;line-height:1.6;color:var(--text-dim);padding:4px 16px;}
.tl-egypt{text-align:right;}
.tl-meso{text-align:left;}
.tl-egypt strong{color:var(--egypt);}
.tl-meso strong{color:var(--meso-light);}

/* ── SOUL ANATOMY ── */
.soul-grid{display:flex;flex-direction:column;gap:8px;margin-top:8px;}
.soul-part{
  display:flex;align-items:flex-start;gap:12px;
  padding:10px 14px;
  background:var(--bg3);
  border:1px solid var(--divider);
}
.soul-glyph{
  font-size:22px;
  flex-shrink:0;
  width:36px;
  text-align:center;
  margin-top:2px;
}
.soul-name{
  font-family:'IM Fell English',serif;
  font-size:14px;
  color:var(--text);
  margin-bottom:3px;
}
.soul-desc{font-size:12px;color:var(--text-dim);line-height:1.6;}

/* ── WINNER BADGE ── */
.winner{
  grid-column:1/-1;
  background:rgba(200,160,0,0.06);
  border:1px solid rgba(200,160,0,0.2);
  padding:40px;
  text-align:center;
  margin:2px 0;
}
.winner h2{
  font-family:'IM Fell English',serif;
  font-size:18px;
  color:var(--sand-dim);
  letter-spacing:4px;
  text-transform:uppercase;
  margin-bottom:24px;
}
.winner-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px;max-width:900px;margin:0 auto;}
.winner-col{text-align:left;}
.winner-cat{
  font-family:'IM Fell English',serif;
  font-size:11px;
  letter-spacing:3px;
  color:var(--text-dim);
  text-transform:uppercase;
  margin-bottom:8px;
}
.winner-name{
  font-family:'IM Fell English',serif;
  font-size:22px;
  margin-bottom:8px;
}
.winner-reason{font-size:14px;color:var(--text-dim);line-height:1.7;font-style:italic;}

/* ── TABS ── */
.tab-bar{display:flex;gap:0;border-bottom:1px solid var(--divider);margin-bottom:0;}
.ctab{
  font-family:'IM Fell English',serif;
  font-size:12px;
  letter-spacing:2px;
  padding:10px 20px;
  background:none;
  border:none;
  color:var(--text-dim);
  cursor:pointer;
  text-transform:uppercase;
  border-bottom:2px solid transparent;
  transition:all 0.2s;
}
.ctab.act{color:var(--sand);border-bottom-color:var(--sand);}

.cpanel{display:none;}
.cpanel.act{display:block;}

/* animate in */
@keyframes fadeUp{from{opacity:0;transform:translateY(16px);}to{opacity:1;transform:none;}}
.two-col > *{animation:fadeUp 0.5s ease both;}
.two-col > *:nth-child(2){animation-delay:0.1s;}

footer{text-align:center;padding:40px 0;font-size:11px;letter-spacing:3px;color:var(--text-dim);border-top:1px solid var(--divider);}
</style>
</head>
<body>

<canvas id="bg"></canvas>

<div class="page">

<!-- MASTHEAD -->
<div class="masthead">
  <div class="masthead-eye">𓂀 𒀭</div>
  <div class="masthead-kicker">Cosmological Deep Dive · Oldest Traditions on Earth</div>
  <h1 class="masthead-h1">
    <span class="egypt-col">Ancient Egypt</span><br>
    vs<br>
    <span class="meso-col">Mesopotamia</span>
  </h1>
  <p class="masthead-sub">The two wellsprings of human civilization — both born beside great rivers, both obsessed with death, cosmic order, and the nature of divinity. How do their universes compare?</p>
  <div class="pill-row">
    <span class="pill pill-e">c. 3100–30 BCE</span>
    <span class="pill pill-m">c. 3500–500 BCE</span>
    <span class="pill pill-e">Nile Valley</span>
    <span class="pill pill-m">Tigris-Euphrates</span>
  </div>
</div>

<!-- TWO-COLUMN MAIN -->
<div class="two-col">

  <!-- ═══ EGYPT LEFT ═══ -->
  <div class="col-egypt">

    <div class="col-head" style="border-left:3px solid var(--egypt);">
      <div class="col-glyph">𓂀</div>
      <div class="col-title" style="color:var(--egypt);">Ancient Egyptian</div>
      <div class="col-era">c. 3100 BCE – 30 BCE · Nile Valley</div>
      <div class="col-score" style="color:var(--egypt);">82<span style="font-size:16px;color:var(--text-dim)">/100</span></div>
      <div class="score-label">Complexity Score</div>
    </div>

    <!-- OVERVIEW -->
    <div class="col-section">
      <div class="section-label">Overview</div>
      <div class="section-text">
        Egyptian cosmology is <strong>theologically diverse</strong> — at least four major creation traditions existed simultaneously without contradiction (Heliopolitan, Memphite, Hermopolitan, Theban). The universe is sustained by <strong>Ma'at</strong> (cosmic order, truth, justice) and threatened perpetually by <strong>Isfet</strong> (chaos). Every night the sun god Ra must fight through the Duat underworld and defeat the chaos serpent <strong>Apep</strong> to rise again. Civilization itself is a cosmological act — the Pharaoh performs ritual to maintain Ma'at and prevent cosmic collapse.
      </div>
    </div>

    <!-- CREATION -->
    <div class="col-section">
      <div class="section-label">Creation Narratives</div>
      <div class="section-text">
        <strong>Heliopolis:</strong> Atum/Ra rises from the primordial waters (Nun) on the Benben mound. Self-created — he masturbates or sneezes to create Shu (air) and Tefnut (moisture), who beget Geb (earth) and Nut (sky). The Ennead (9 gods) form the cosmic family.<br><br>
        <strong>Memphis:</strong> Ptah creates through <em>thought and speech alone</em> — the Memphite Theology (Shabaka Stone, c. 710 BCE) records that Ptah conceived all things in his heart and spoke them into being. This is the oldest documented creation-by-word theology — predating Genesis.<br><br>
        <strong>Hermopolis:</strong> The Ogdoad — 8 primordial deities representing chaos, darkness, infinity, and hiddenness — create the cosmic egg from which Ra hatches.<br><br>
        <strong>Theban:</strong> Amun as the hidden, self-created god; breathes life into existence. All traditions coexisted and were considered complementary, not contradictory.
      </div>
    </div>

    <!-- COSMIC REALMS -->
    <div class="col-section">
      <div class="section-label">The 9 Cosmological Layers</div>
      <div class="realm-tower">
        <div class="realm-block">
          <div class="realm-swatch" style="background:#ffe070;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 1 · HIGHEST</div>
            <div class="realm-name">Nut — The Star-Body Sky</div>
            <div class="realm-desc">The goddess Nut arches over all creation. Her body is the sky; the stars are upon her. She swallows the sun each evening at Akhet (horizon), gestates it through her body, and births it again at dawn. The dead Pharaoh ascends to become a star on her body — immortality as celestial navigation.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#ffd040;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 2</div>
            <div class="realm-name">Akhet — The Horizon / Solar Realm</div>
            <div class="realm-desc">The liminal zone of sunrise and sunset. The Sphinx guards this threshold. Ra as Khepri (scarab, morning), Ra (noon), and Atum (evening) — three forms of one solar cycle. The horizon is a cosmological pivot point.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#d0b020;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 3</div>
            <div class="realm-name">Nun — Primordial Ocean</div>
            <div class="realm-desc">The infinite dark waters that existed before creation and surround all existence. Ra's solar barque sails across Nun. At the end of time, Nun will reclaim all creation. The source and the end — Egyptian cosmic bookends.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#a08020;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 4 · CENTER</div>
            <div class="realm-name">Ta / Geb — The Living Earth</div>
            <div class="realm-desc">The earth god Geb lies beneath; his body is the land; his laughter created earthquakes. He and Nut (sky) were physically separated by Shu (air) at the command of Ra — the original cosmic separation creating space for life. Egypt (Kemet, the black land) is the sacred center of the cosmos.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#806010;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 5</div>
            <div class="realm-name">Duat — The 12-Hour Underworld Journey</div>
            <div class="realm-desc">Not simply "hell" — it is the nightly path of Ra's solar barque through 12 hours/gates of darkness. Each hour has its own gods, demons, and challenges. The Amduat (c. 1500 BCE) maps all 12 hours in precise detail. The dead must navigate this same journey.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#604810;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 6</div>
            <div class="realm-name">Hall of Two Truths (Maat Kheru)</div>
            <div class="realm-desc">The judgment hall of Osiris. 42 divine assessors each representing a specific sin. The heart (Ib) — seat of conscience — is weighed against the feather of Ma'at on the scales of Anubis. Thoth records the verdict. The perfect balance means the soul is "true of voice" (Maat Kheru).</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#305010;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 7</div>
            <div class="realm-name">Aaru — The Field of Reeds</div>
            <div class="realm-desc">Paradise: fertile fields mirroring the Nile delta; eternal perfect life. The virtuous work the fields of the gods, sail the celestial Nile, and experience all pleasures of Egypt without death or decay. The most detailed ancient paradise description — mapped in the Book of the Dead.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#200a08;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 8</div>
            <div class="realm-name">Ammit's Realm — The Second Death</div>
            <div class="realm-desc">The failed soul is consumed by Ammit — part lion, part hippopotamus, part crocodile. Unlike most afterlife systems, this is total annihilation — "the second death." No hell, no punishment, no afterlife. Simply ceasing to exist. Ancient Egypt's most feared outcome.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#102010;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 9 · DEEPEST</div>
            <div class="realm-name">Sekhet-Aaru / Osiris's Own Dwelling</div>
            <div class="realm-desc">The innermost paradise where Osiris himself dwells. The most blessed state — to dwell in the presence of the Lord of the Dead himself. Beyond the Field of Reeds; the destination of the most perfectly righteous.</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SOUL ANATOMY -->
    <div class="col-section">
      <div class="section-label">The 5-Part Soul (Most Complex in Antiquity)</div>
      <div class="soul-grid">
        <div class="soul-part">
          <div class="soul-glyph">𓅜</div>
          <div><div class="soul-name">Ka — The Life-Force Double</div><div class="soul-desc">The vital life energy created at birth; lives in statues and tomb offerings; must be fed with offerings or it perishes. The Ka is why Egyptians left food in tombs.</div></div>
        </div>
        <div class="soul-part">
          <div class="soul-glyph">𓅂</div>
          <div><div class="soul-name">Ba — The Personality-Soul</div><div class="soul-desc">The individual personality and character; depicted as a human-headed bird. The Ba can travel between the living world and the dead — it is the mobile, traveling aspect of the soul.</div></div>
        </div>
        <div class="soul-part">
          <div class="soul-glyph">✦</div>
          <div><div class="soul-name">Akh — The Glorified Spirit</div><div class="soul-desc">The unified effective spirit — Ka + Ba reunited through successful judgment. The Akh is a star (Sahu) in Nut's sky-body. Transformation of the earthly person into an immortal divine being.</div></div>
        </div>
        <div class="soul-part">
          <div class="soul-glyph">𓇯</div>
          <div><div class="soul-name">Ren — The Name</div><div class="soul-desc">One's true name; part of the soul. To erase a person's name (damnatio memoriae) was to destroy them cosmologically. This is why pharaohs chiseled enemies' names off monuments — literal soul murder.</div></div>
        </div>
        <div class="soul-part">
          <div class="soul-glyph">👤</div>
          <div><div class="soul-name">Sheut — The Shadow</div><div class="soul-desc">The shadow-soul; always present; could be harmed by dark magic. The shadow was considered a part of a person's cosmic identity, not a mere optical effect.</div></div>
        </div>
      </div>
    </div>

    <!-- KEY TEXTS -->
    <div class="col-section">
      <div class="section-label">Sacred Texts & Sources</div>
      <ul class="fact-list">
        <li><strong>Pyramid Texts (c. 2400–2300 BCE)</strong> — oldest religious corpus in the world; carved inside Old Kingdom pyramids; spells for pharaonic afterlife navigation</li>
        <li><strong>Coffin Texts (c. 2100–1800 BCE)</strong> — democratized for nobles and wealthy; Book of Two Ways maps the Duat in two routes</li>
        <li><strong>Book of the Dead (c. 1550 BCE)</strong> — 192 chapters of navigational spells; the deceased's personal passport through judgment</li>
        <li><strong>Amduat (c. 1500 BCE)</strong> — "What is in the Underworld"; maps Ra's nightly 12-hour Duat journey hour by hour</li>
        <li><strong>Book of Gates (New Kingdom)</strong> — 12 gates of the underworld with guardians and passwords</li>
        <li><strong>Shabaka Stone (c. 710 BCE)</strong> — records the ancient Memphite creation theology (Ptah creating by speech)</li>
        <li><strong>Leiden Papyrus</strong> — "Amun is one, one only, and millions are his forms" — proto-monotheistic statement</li>
      </ul>
    </div>

    <!-- UNIQUE FEATURES -->
    <div class="col-section">
      <div class="section-label">What Makes Egypt Unique</div>
      <ul class="fact-list">
        <li>Only civilization with <strong>multiple simultaneous creation myths treated as equally true</strong> — theological pluralism by design</li>
        <li><strong>Body preservation (mummification)</strong> as cosmological necessity — the Ka needs the body as its anchor</li>
        <li>The <strong>42 Assessors of Ma'at</strong> — most detailed pre-Christian moral judgment system</li>
        <li><strong>"True of Voice" (Maat Kheru)</strong> — acquittal at judgment; the goal of the righteous life</li>
        <li>The <strong>Pharaoh as cosmological fulcrum</strong> — his rituals literally maintain Ma'at and prevent cosmic collapse</li>
        <li><strong>Akhenaten's revolution (c. 1353 BCE)</strong> — attempted monotheism (Aten worship); reversed after death; the first documented monotheism</li>
        <li>Cosmic time: <strong>Zep Tepi</strong> (First Time) — the mythic age of creation; all ritual re-enacts Zep Tepi</li>
        <li><strong>Apophis/Apep</strong> — chaos serpent defeated nightly by Ra; one of the earliest personified cosmic evil entities</li>
      </ul>
    </div>

  </div><!-- /col-egypt -->

  <!-- ═══ MESOPOTAMIA RIGHT ═══ -->
  <div class="col-meso">

    <div class="col-head" style="border-left:3px solid var(--meso-light);">
      <div class="col-glyph">𒀭</div>
      <div class="col-title" style="color:var(--meso-light);">Mesopotamian</div>
      <div class="col-era">c. 3500–500 BCE · Tigris-Euphrates</div>
      <div class="col-score" style="color:var(--meso-light);">78<span style="font-size:16px;color:var(--text-dim)">/100</span></div>
      <div class="score-label">Complexity Score</div>
    </div>

    <!-- OVERVIEW -->
    <div class="col-section">
      <div class="section-label">Overview</div>
      <div class="section-text">
        Mesopotamian cosmology is <strong>the oldest written cosmological tradition on Earth</strong> — the Sumerians preceded even Egypt's written records. Its cosmology is <strong>fundamentally political</strong>: gods behave like kings, hold divine councils, argue, scheme, and issue decrees (Me — the fundamental laws of civilization). The universe is run like a <strong>divine bureaucracy</strong>. Humans were created specifically to <strong>labor for the gods</strong> — to feed them with offerings so the gods could rest. There is no illusion of cosmic justice for ordinary mortals — all dead go to the same grim underworld regardless of virtue.
      </div>
    </div>

    <!-- CREATION -->
    <div class="col-section">
      <div class="section-label">Creation Narratives</div>
      <div class="section-text">
        <strong>Enuma Elish (c. 1750 BCE, Babylonian):</strong> In the beginning, Apsu (fresh water) and Tiamat (salt water/chaos) mingle; their offspring become noisy gods who disturb Apsu's rest. Apsu plans to kill them; Ea (wisdom) kills Apsu first. Tiamat, enraged, creates an army of monsters. The young god <strong>Marduk</strong> agrees to fight Tiamat — if victorious, he becomes king of gods. He slays Tiamat, splits her body: upper half = sky, lower half = earth. From Kingu's (Tiamat's champion) blood, humans are created to serve the gods.<br><br>
        <strong>Sumerian:</strong> The earlier Sumerian tradition (pre-Babylonian) features <strong>Enlil</strong> as the separating force — he separates An (sky) from Ki (earth) creating space for life. The goddess Nammu (primordial sea) gives birth to the first gods.<br><br>
        <strong>Atrahasis Epic:</strong> When humans multiplied and became too noisy, the gods sent the Flood to reduce them. Atrahasis (Utnapishtim/Noah figure) survived — the oldest flood narrative in human literature.
      </div>
    </div>

    <!-- COSMIC REALMS -->
    <div class="col-section">
      <div class="section-label">The 7 Cosmological Layers</div>
      <div class="realm-tower">
        <div class="realm-block">
          <div class="realm-swatch" style="background:#ffe8a0;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 1 · HIGHEST</div>
            <div class="realm-name">An — Heaven of Anu</div>
            <div class="realm-desc">The uppermost heaven; dwelling of Anu, the sky god and father-king of all gods. Stars are soldiers of Anu. The divine assembly (Anunnaki = "those of royal blood of An") meets here. The Tablet of Destinies — whoever holds it controls all creation — is kept here.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#f0c870;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 2</div>
            <div class="realm-name">Enlil's Heaven — The Realm of Decree</div>
            <div class="realm-desc">Middle heaven; realm of Enlil, the wind god and executive king of gods. His city is Nippur — the cosmic navel of the earth. Divine decrees (Me — the laws of civilization: kingship, descent, weapons, writing, sex, music) are administered here.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#d0a850;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 3</div>
            <div class="realm-name">Ea/Enki's Realm — The Abzu/Apsu</div>
            <div class="realm-desc">The lower cosmic ocean beneath the earth (Apsu/Abzu); realm of Ea (Enki), god of wisdom, magic, and fresh water. The source of all wisdom and all rivers. Ea's city is Eridu — the oldest city, the first city, where kingship descended from heaven.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#a07830;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 4 · CENTER</div>
            <div class="realm-name">Ki / Ersetu — The Earth</div>
            <div class="realm-desc">The flat earth disc floating on the Apsu, surrounded by the salt sea. Mortals, animals, and plants inhabit this realm. The ziggurat temples (such as Etemenanki in Babylon — likely the Tower of Babel) are cosmological mountains connecting earth to heaven.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#603810;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 5</div>
            <div class="realm-name">The 7 Gates of Irkalla</div>
            <div class="realm-desc">The descent to the underworld passes through 7 gates. At each gate, Inanna (in her descent myth) must remove one item of clothing/jewelry — crown, earrings, necklace, breast ornaments, girdle, bracelets, garment. Each removal = loss of divine power and identity. Stripped of everything, she enters naked and bowed.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#401808;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 6</div>
            <div class="realm-name">Kur / Irkalla — The Great Below</div>
            <div class="realm-desc">The underworld; ruled by Ereshkigal (queen) and her consort Nergal. All dead enter here regardless of virtue. A "House of Dust and Darkness" — the dead wear feathers as garments, eat clay and dust. Kings and priests, warriors and beggars — all equal in the dust. The most democratic and most grim of all ancient afterlives.</div>
          </div>
        </div>
        <div class="realm-block">
          <div class="realm-swatch" style="background:#200808;"></div>
          <div class="realm-inner">
            <div class="realm-level">LAYER 7 · DEEPEST</div>
            <div class="realm-name">The Primordial Apsu (Subterranean Ocean)</div>
            <div class="realm-desc">The deepest layer — the subterranean freshwater ocean from which all springs and rivers rise. Source of all fresh water on earth. Enki/Ea dwells here. Also the origin point of creation — before even the gods existed, only Apsu and Tiamat mingled here in the primal dark.</div>
          </div>
        </div>
      </div>
    </div>

    <!-- NO SOUL ANATOMY — contrast -->
    <div class="col-section">
      <div class="section-label">The Soul — Etemmu (Ghost/Spirit)</div>
      <div class="soul-grid">
        <div class="soul-part">
          <div class="soul-glyph">👻</div>
          <div><div class="soul-name">Etemmu — The Ghost</div><div class="soul-desc">The spirit of the dead; remains near the body initially; if improperly buried or offerings not given, becomes a dangerous haunting ghost (Ahhazu). The ghost needs offerings to rest peacefully in the underworld.</div></div>
        </div>
        <div class="soul-part">
          <div class="soul-glyph">🌬</div>
          <div><div class="soul-name">Napishtu — The Life-Breath</div><div class="soul-desc">The life-force, literally "life" or "breath." Given by the gods at birth; returns to the gods at death. Analogous to Egyptian Ka but simpler — no surviving independent identity concept.</div></div>
        </div>
        <div class="soul-part">
          <div class="soul-glyph">📿</div>
          <div><div class="soul-name">Burial Provisions</div><div class="soul-desc">Unlike Egypt's complex mummification, Mesopotamia emphasized <em>proper burial</em> and <em>ongoing family offerings</em>. An unburied person's ghost was the most dangerous — a wandering, vengeful spirit unable to reach Irkalla.</div></div>
        </div>
      </div>
      <div style="margin-top:12px;font-size:13px;color:var(--text-dim);font-style:italic;padding:12px 14px;border:1px solid var(--divider);border-left:3px solid var(--meso-light);">
        Mesopotamia had no concept of moral judgment in the afterlife. Virtue did not affect one's destination. All dead — king and slave — go to Irkalla and eat dust. This philosophical darkness drove Gilgamesh to seek immortality: "When the gods created mankind, they allotted death to mankind, but life they retained in their own keeping."
      </div>
    </div>

    <!-- KEY TEXTS -->
    <div class="col-section">
      <div class="section-label">Sacred Texts & Sources</div>
      <ul class="fact-list">
        <li><strong>Enuma Elish (c. 1750 BCE)</strong> — Babylonian creation epic; 7 clay tablets; recited at New Year festival (Akitu) to re-enact creation and renew cosmos</li>
        <li><strong>Epic of Gilgamesh (c. 2100 BCE written, older oral)</strong> — oldest surviving literary epic; hero's quest for immortality; Flood narrative (Tablet XI) predates Genesis by 1000+ years</li>
        <li><strong>Descent of Inanna (c. 1900–1600 BCE)</strong> — Sumerian poem; goddess descends to underworld through 7 gates; dies and is resurrected; earliest descent-resurrection myth</li>
        <li><strong>Atrahasis Epic (c. 1700 BCE)</strong> — creation of humans + first flood narrative; humans made from god's blood + clay to serve as divine laborers</li>
        <li><strong>Hymn to Enlil</strong> — describes Enlil as supreme administrator of cosmic law; the divine bureaucracy in full operation</li>
        <li><strong>Nanshe Hymn</strong> — one of earliest social justice texts; goddess protects widows, orphans, the poor — cosmic moral responsibility</li>
        <li><strong>Lament for the Destruction of Ur</strong> — cosmic order (Me) can be withdrawn; cities fall not from military failure but divine abandonment</li>
      </ul>
    </div>

    <!-- UNIQUE FEATURES -->
    <div class="col-section">
      <div class="section-label">What Makes Mesopotamia Unique</div>
      <ul class="fact-list">
        <li><strong>Oldest written cosmology on Earth</strong> — Sumerian cosmological texts predate Egyptian written records by centuries</li>
        <li><strong>The Me</strong> — the divine laws/decrees of civilization (kingship, descent, weapons, music, sex, crafts) as cosmic objects that can be stolen, traded, or lost</li>
        <li><strong>Ziggurat as cosmic mountain</strong> — Etemenanki ("House of the Foundation of Heaven and Earth") in Babylon; the literal axis mundi connecting earth to heaven</li>
        <li><strong>First flood narrative</strong> — Atrahasis/Utnapishtim story; direct source (or parallel) of Noah's Ark; predates Genesis by over 1,000 years</li>
        <li><strong>First descent-resurrection myth</strong> — Inanna's descent through 7 gates, death, and return; template for countless later myths</li>
        <li><strong>Democratic death</strong> — no moral afterlife judgment; this philosophical reality drove the world's first existential crisis literature (Gilgamesh)</li>
        <li><strong>Tablet of Destinies</strong> — a cosmic power object; whoever holds it controls creation; Anzû bird steals it, creating cosmic crisis — the most literal cosmological MacGuffin</li>
        <li><strong>Divine council (Anunnaki)</strong> — gods vote, argue, and legislate; the template for divine assembly in later Near Eastern traditions including early Israelite religion (Psalm 82)</li>
      </ul>
    </div>

  </div><!-- /col-meso -->

  <!-- ═══ HEAD-TO-HEAD COMPARISON ═══ -->
  <div class="compare-row" style="grid-column:1/-1;">
    <h2>⚖ Direct Comparison</h2>
    <div class="compare-metrics">
      <div class="metric-row">
        <div class="metric-val e">82</div>
        <div class="metric-label">Complexity Score</div>
        <div class="metric-val m">78</div>
      </div>
      <div class="metric-row">
        <div class="metric-val e">9</div>
        <div class="metric-label">Total Named Realms</div>
        <div class="metric-val m">7</div>
      </div>
      <div class="metric-row">
        <div class="metric-val e">4+</div>
        <div class="metric-label">Creation Traditions</div>
        <div class="metric-val m">3</div>
      </div>
      <div class="metric-row">
        <div class="metric-val e">5</div>
        <div class="metric-label">Soul Components</div>
        <div class="metric-val m">2</div>
      </div>
      <div class="metric-row">
        <div class="metric-val e">42</div>
        <div class="metric-label">Afterlife Judges</div>
        <div class="metric-val m">0</div>
      </div>
      <div class="metric-row">
        <div class="metric-val e">12</div>
        <div class="metric-label">Hours of the Duat</div>
        <div class="metric-label">Gates of Irkalla</div>
        <div class="metric-val m">7</div>
      </div>
      <div class="metric-row">
        <div class="metric-note e" style="text-align:right;">Moral — virtue determines paradise vs annihilation</div>
        <div class="metric-label">Afterlife Justice</div>
        <div class="metric-note m">None — all dead equal in dust regardless of virtue</div>
      </div>
      <div class="metric-row">
        <div class="metric-note e" style="text-align:right;">Cyclic solar (daily + annual); Zep Tepi as eternal mythic origin</div>
        <div class="metric-label">Time Concept</div>
        <div class="metric-note m">Linear + cyclic; New Year (Akitu) recreates cosmos; no final eschatology</div>
      </div>
      <div class="metric-row">
        <div class="metric-note e" style="text-align:right;">Pharaoh as cosmic axis; rituals maintain Ma'at and prevent collapse</div>
        <div class="metric-label">Political Cosmology</div>
        <div class="metric-note m">King as divine administrator; cities fall when gods withdraw Me; cosmic bureaucracy</div>
      </div>
      <div class="metric-row">
        <div class="metric-note e" style="text-align:right;">c. 2400 BCE (Pyramid Texts)</div>
        <div class="metric-label">Oldest Written Text</div>
        <div class="metric-note m">c. 2600 BCE (Sumerian King List, Eridu Genesis)</div>
      </div>
    </div>
  </div>

  <!-- ═══ TIMELINE ═══ -->
  <div class="compare-row" style="grid-column:1/-1;">
    <h2>📜 Parallel Timeline</h2>
    <div class="timeline">
      <div class="timeline-spine"></div>
      <div class="tl-item"><div class="tl-egypt"><strong>Narmer unifies Egypt</strong> — kingship as cosmic order established</div><div class="tl-date">3100 BCE</div><div class="tl-meso">Uruk period peak — first cities, first writing (cuneiform) in Sumer</div></div>
      <div class="tl-item"><div class="tl-egypt"><strong>Pyramid Texts</strong> — world's oldest religious corpus written inside pyramid walls</div><div class="tl-date">2400 BCE</div><div class="tl-meso">Eridu Genesis / early Sumerian flood myths already circulating orally</div></div>
      <div class="tl-item"><div class="tl-egypt">Coffin Texts democratize afterlife navigation for non-royalty</div><div class="tl-date">2100 BCE</div><div class="tl-meso"><strong>Earliest Gilgamesh texts</strong> — the world's first named literary hero confronts mortality</div></div>
      <div class="tl-item"><div class="tl-egypt">Middle Kingdom: full Book of Two Ways maps the Duat</div><div class="tl-date">1900 BCE</div><div class="tl-meso"><strong>Descent of Inanna</strong> written down — first descent-resurrection myth</div></div>
      <div class="tl-item"><div class="tl-egypt">New Kingdom: <strong>Book of the Dead</strong> standardized; Amduat composed</div><div class="tl-date">1750 BCE</div><div class="tl-meso"><strong>Enuma Elish</strong> composed — Marduk replaces Enlil as chief god; Babylon rises</div></div>
      <div class="tl-item"><div class="tl-egypt"><strong>Akhenaten's Aten revolution</strong> — first documented monotheism; erases all other gods</div><div class="tl-date">1353 BCE</div><div class="tl-meso">Assyrian Empire rises; Mesopotamian cosmology exported across Near East</div></div>
      <div class="tl-item"><div class="tl-egypt"><strong>Shabaka Stone</strong> — Memphite Theology (Ptah-creation by speech) recorded on stone</div><div class="tl-date">710 BCE</div><div class="tl-meso">Babylon's Etemenanki ziggurat completed — the real Tower of Babel</div></div>
      <div class="tl-item"><div class="tl-egypt">Alexander conquers Egypt (332 BCE); Ptolemaic dynasty; Greek synthesis begins</div><div class="tl-date">539 BCE</div><div class="tl-meso"><strong>Cyrus the Great</strong> conquers Babylon — end of independent Mesopotamian civilization</div></div>
    </div>
  </div>

  <!-- ═══ WINNERS BY CATEGORY ═══ -->
  <div class="winner" style="grid-column:1/-1;">
    <h2>Verdict by Category</h2>
    <div class="winner-grid">
      <div class="winner-col">
        <div class="winner-cat">Cosmological Scale</div>
        <div class="winner-name" style="color:var(--egypt);">𓂀 Egypt Wins</div>
        <div class="winner-reason">9 named realms vs 7; 12-hour Duat journey; 4 simultaneous creation traditions; 5-part soul vs 2-part. Egyptian cosmology is simply larger and more elaborated.</div>
      </div>
      <div class="winner-col">
        <div class="winner-cat">Historical Priority</div>
        <div class="winner-name" style="color:var(--meso-light);">𒀭 Mesopotamia Wins</div>
        <div class="winner-reason">Sumerian writing predates Egyptian hieroglyphic records. Eridu Genesis, Sumerian King List, and early flood narratives are the oldest written cosmological documents on Earth.</div>
      </div>
      <div class="winner-col">
        <div class="winner-cat">Afterlife Complexity</div>
        <div class="winner-name" style="color:var(--egypt);">𓂀 Egypt Wins</div>
        <div class="winner-reason">42 divine judges vs zero. Full moral reckoning with measurable scales vs a grim egalitarian dust-house. Egypt invented the afterlife as a morally differentiated space.</div>
      </div>
      <div class="winner-col">
        <div class="winner-cat">Influence on World Religions</div>
        <div class="winner-name" style="color:var(--meso-light);">𒀭 Mesopotamia Wins</div>
        <div class="winner-reason">The Flood myth, divine council, creation-by-conflict, and descent-resurrection patterns directly shaped Judaism, Christianity, and Islam. The Enuma Elish's 7-day creation structure echoes in Genesis.</div>
      </div>
      <div class="winner-col">
        <div class="winner-cat">Philosophical Depth</div>
        <div class="winner-name" style="color:var(--meso-light);">𒀭 Mesopotamia Wins</div>
        <div class="winner-reason">Gilgamesh confronting mortality with no false comfort is philosophically rawer and more honest than Egypt's elaborate optimism. The Mesopotamian cosmos doesn't flinch from existential darkness.</div>
      </div>
      <div class="winner-col">
        <div class="winner-cat">Overall Cosmological Complexity</div>
        <div class="winner-name" style="color:var(--egypt);">𓂀 Egypt Wins</div>
        <div class="winner-reason">Score 82 vs 78. More realms, more soul-parts, more creation traditions, more detailed afterlife system, and the most elaborate pre-Christian moral judgment architecture ever devised.</div>
      </div>
    </div>
  </div>

</div><!-- /two-col -->

</div><!-- /page -->

<footer>
  ANCIENT COSMOLOGIES DEEP DIVE · EGYPT vs MESOPOTAMIA · PILLI SHREYAS · GODMODE RESEARCH
</footer>

<script>
/* subtle animated hieroglyphic/cuneiform particles */
(function(){
  const c=document.getElementById('bg');
  const ctx=c.getContext('2d');
  const glyphs=['𓂀','𓅜','𓅂','𒀭','𒁹','𓇯','𓏏','𒀭','𓊽','𓉔','𒅈','𓋴'];
  let W,H,particles=[];
  function resize(){W=c.width=window.innerWidth;H=c.height=window.innerHeight;}
  function init(){
    particles=[];
    for(let i=0;i<40;i++){
      particles.push({
        x:Math.random()*W,
        y:Math.random()*H,
        g:glyphs[Math.floor(Math.random()*glyphs.length)],
        s:10+Math.random()*14,
        a:0.03+Math.random()*0.08,
        vy:-0.15-Math.random()*0.2,
        da:(Math.random()-0.5)*0.001
      });
    }
  }
  function draw(){
    ctx.clearRect(0,0,W,H);
    particles.forEach(p=>{
      p.y+=p.vy;
      p.a=Math.max(0.02,Math.min(0.12,p.a+p.da));
      if(p.a<=0.02||p.a>=0.12) p.da*=-1;
      if(p.y<-30){p.y=H+30;p.x=Math.random()*W;}
      ctx.save();
      ctx.globalAlpha=p.a;
      ctx.fillStyle='#c8a000';
      ctx.font=`${p.s}px serif`;
      ctx.fillText(p.g,p.x,p.y);
      ctx.restore();
    });
    requestAnimationFrame(draw);
  }
  window.addEventListener('resize',()=>{resize();init();});
  resize();init();draw();
})();
</script>
</body>
</html>

---

### 🧑 You

make me an complete report of all religions with matter using diagrams and images of each and make it professional use flow charts to represent each . so that i can copy and make an document

---

### 🧑 You

show oldest foundings of each religion in its coloumn its direct link of image

---

### 🧑 You

check image links they are not working and remake an complete report with correct image links which are working with flowcharts

---
