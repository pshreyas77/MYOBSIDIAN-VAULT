#!/usr/bin/env python3
"""
Shreyas's Second Brain — Professional Knowledge Graph  v2
==========================================================
D3.js force-directed graph with dark theme, domain coloring,
hub glow, animated edges, nebula background, tooltips, zoom/pan.

Output: obsidian_graph.html (open in any browser)
"""
import re, json
from pathlib import Path
import networkx as nx
from collections import Counter

# ── Config ──────────────────────────────────────────────────────────────────────
VAULT   = Path("E:/_Knowledge/ObsidianVault")
OUT     = VAULT / "obsidian_graph.html"
MAX_NODES = 400   # smooth physics cap

# ── Vibrant domain palette (name → hex) ────────────────────────────────────────
DOMAIN_PALETTE = {
    "Indian Political History":  "#ff6b6b",
    "Dravidian Politics / Tamil Nadu": "#ee5a5a",
    "Aryan Migration / IVC / DNA": "#a855f7",
    "RSS / Hindutva / Sangh Parivar": "#f97316",
    "Philosophy & Religion": "#c084fc",
    "Buddhism / Shramana": "#fb923c",
    "Anti-Caste / Ambedkar / Phule": "#22d3ee",
    "AI & Technology / PKM": "#38bdf8",
    "Health & Fitness": "#4ade80",
    "Agentic Systems": "#fbbf24",
    "Maps / MOCs": "#818cf8",
    "Daily Notes / Logs": "#60a5fa",
    "Sources / Literature": "#fcd34d",
    "Output / Analyses": "#2dd4bf",
    "Projects / PARA": "#f472b6",
    "System / Infrastructure": "#34d399",
    "Second Brain / LLM Wiki": "#22d3ee",
    "tag": "#e2e8f0",
    "default": "#475569",
}

# ── Glow colors per domain (for hub nodes) ─────────────────────────────────────
DOMAIN_GLOW = {
    "Indian Political History":  "#ff6b6b",
    "Dravidian Politics / Tamil Nadu": "#ee5a5a",
    "Aryan Migration / IVC / DNA": "#a855f7",
    "RSS / Hindutva / Sangh Parivar": "#f97316",
    "Philosophy & Religion": "#c084fc",
    "Buddhism / Shramana": "#fb923c",
    "Anti-Caste / Ambedkar / Phule": "#22d3ee",
    "AI & Technology / PKM": "#38bdf8",
    "Health & Fitness": "#4ade80",
    "Agentic Systems": "#fbbf24",
    "Maps / MOCs": "#818cf8",
    "Daily Notes / Logs": "#60a5fa",
    "Sources / Literature": "#fcd34d",
    "Output / Analyses": "#2dd4bf",
    "Projects / PARA": "#f472b6",
    "System / Infrastructure": "#34d399",
    "Second Brain / LLM Wiki": "#22d3ee",
    "tag": "#e2e8f0",
    "default": "#475569",
}

def classify_node(name: str) -> str:
    n = name.lower()
    if n.startswith("#"):
        return "tag"
    if any(k in n for k in ["indian political history moc","justice party","periyar","karunanidhi","anna dmk","m.gr","kamaraj","neethi","bjp south","election","dmk","aiadmk","tamil nadu","tamil politics","dravidian"]):
        return "Indian Political History" if any(k in n for k in ["indian political","periyar","justice","karunanidhi","anna","m.gr","kamaraj","neethi","election","bjp south"]) else "Dravidian Politics / Tamil Nadu"
    if any(k in n for k in ["aryan","indus valley","ivc","steppe","rakhigarhi","harappan","pre-aryan","migration","ancient dna"]):
        return "Aryan Migration / IVC / DNA"
    if any(k in n for k in ["rss","hindutva","sangh","hindu"]):
        return "RSS / Hindutva / Sangh Parivar"
    if any(k in n for k in ["philosophy","vedanta","kant","shankara"," Advaita"," Advaita"]):
        return "Philosophy & Religion"
    if any(k in n for k in ["buddhism","buddha","buddhist","dhamma","sangha","mahayana","theravada"]):
        return "Buddhism / Shramana"
    if any(k in n for k in ["anti-caste","ambedkar","dalit","phule","jyotirao","maharashtra"]):
        return "Anti-Caste / Ambedkar / Phule"
    if any(k in n for k in ["agentic","autonomous agent","genericagent","night shift"]):
        return "Agentic Systems"
    if any(k in n for k in ["health","fitness","supplement","workout","tier","ppl","gym"]):
        return "Health & Fitness"
    if any(k in n for k in ["moc","map of content","maps","index"]):
        return "Maps / MOCs"
    if any(k in n for k in ["04 - daily","daily note","night-shift-log"]):
        return "Daily Notes / Logs"
    if any(k in n for k in ["01 - literature","literature","articles","research"]):
        return "Sources / Literature"
    if any(k in n for k in ["06 - outputs","outputs","analysis","synthesis"]):
        return "Output / Analyses"
    if any(k in n for k in ["03 - projects","project","cross-domain"]):
        return "Projects / PARA"
    if any(k in n for k in ["07 - system","system","vault-health","ai-first"]):
        return "System / Infrastructure"
    if any(k in n for k in ["ai","llm","claude","obsidian","second brain","zettel","pkm","wiki","knowledge graph","note-taking"]):
        return "AI & Technology / PKM"
    return "default"


def get_links(text):
    return re.findall(r'\[\[(.*?)\]\]', text)

def get_tags(text):
    return re.findall(r'(?<!\\w)#([\w/-]+)', text)

EXCLUDE = {'.obsidian', '.smart-env', '.git', 'node_modules', '_trash', '.graphify', 'trash', '.trash'}

G = nx.Graph()
nodes_meta = {}

for md in VAULT.glob("**/*.md"):
    name = str(md.relative_to(VAULT)).replace(".md", "")
    if any(e in name for e in EXCLUDE):
        continue
    try:
        text = md.read_text(encoding="utf-8", errors="ignore")
        domain = classify_node(name)
        nodes_meta[name] = {"domain": domain, "links": [], "tags": []}
        G.add_node(name)

        for tag in get_tags(text):
            tn = f"#{tag}"
            if tn not in nodes_meta:
                G.add_node(tn)
                nodes_meta[tn] = {"domain": "tag", "links": [], "tags": []}
            G.add_edge(name, tn)
            nodes_meta[name]["tags"].append(tag)

        for link in get_links(text):
            target = link.split("|")[0].split("#")[0].strip()
            if target:
                G.add_edge(name, target)
                nodes_meta[name]["links"].append(target)
    except Exception:
        pass

print(f"Raw: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# ── Prune to top nodes ─────────────────────────────────────────────────────────
deg = dict(G.degree())
all_nodes = sorted(G.nodes(), key=lambda n: deg.get(n, 0), reverse=True)
if len(all_nodes) > MAX_NODES:
    keep = set(all_nodes[:MAX_NODES])
    for n in list(G.nodes()):
        if n not in keep:
            G.remove_node(n)
    print(f"Pruned → {G.number_of_nodes()} nodes")
print(f"Graph built: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# ── Enrich meta ─────────────────────────────────────────────────────────────────
for n in G.nodes():
    nodes_meta.setdefault(n, {"domain": classify_node(n), "links": [], "tags": []})
    nodes_meta[n]["degree"] = deg.get(n, 0)

# ── Community detection (fast — greedy modularity) ─────────────────────────────
try:
    from networkx.algorithms.community import greedy_modularity_communities
    comms = list(greedy_modularity_communities(G.to_undirected()))
    communities = {}
    for i, c in enumerate(comms):
        for n in c:
            communities[n] = i
    mod = nx_comm.greedy_modularity_communities
    print(f"Communities (greedy): {len(comms)}")
except Exception:
    communities = {n: i % 12 for i, n in enumerate(G.nodes())}
    print(f"Communities (fallback): {len(set(communities.values()))}")

# ── Build node/edge lists ───────────────────────────────────────────────────────
for n, cid in communities.items():
    nodes_meta.setdefault(n, {"domain": "default", "links": [], "tags": []})
    nodes_meta[n]["community"] = cid

node_list = []
for n in G.nodes():
    m = nodes_meta.get(n, {})
    domain = m.get("domain", "default")
    color = DOMAIN_PALETTE.get(domain, DOMAIN_PALETTE["default"])
    deg_val = m.get("degree", 1)
    is_tag = n.startswith("#")
    size = 3 if is_tag else max(5, min(40, 5 + deg_val * 1.8))
    label = n.split("/")[-1][:70]
    node_list.append({
        "id": n,
        "label": label,
        "domain": domain,
        "color": color,
        "glow": DOMAIN_GLOW.get(domain, "#475569"),
        "size": size,
        "degree": deg_val,
        "community": m.get("community", 0),
        "links": m.get("links", [])[:10],
        "tags": m.get("tags", [])[:8],
    })

edge_list = []
for u, v in G.edges():
    edge_list.append({"source": u, "target": v, "weight": 1})

graph_data = {"nodes": node_list, "links": edge_list}

# ── HTML ────────────────────────────────────────────────────────────────────────
html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🧠 Second Brain — Knowledge Graph</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  background: #070810;
  font-family: 'Inter', sans-serif;
  color: #e2e8f0;
  overflow: hidden;
  height: 100vh;
  width: 100vw;
}

/* ── Animated nebula background ── */
#bg-canvas {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
}

/* ── Header ── */
#header {
  position: fixed;
  top: 0; left: 0; right: 0;
  height: 54px;
  background: rgba(7,8,16,0.85);
  border-bottom: 1px solid rgba(255,255,255,0.07);
  display: flex;
  align-items: center;
  padding: 0 24px;
  z-index: 100;
  backdrop-filter: blur(20px);
  gap: 20px;
}
#header h1 {
  font-size: 15px;
  font-weight: 700;
  color: #e2e8f0;
  letter-spacing: 0.02em;
  display: flex;
  align-items: center;
  gap: 8px;
}
#header h1 .emoji { font-size: 18px; }
#header h1 .accent { color: #a855f7; }
#stats {
  font-size: 11px;
  color: #64748b;
  margin-left: 4px;
}
#controls {
  display: flex;
  gap: 8px;
  align-items: center;
  margin-left: auto;
}
#search {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 8px;
  color: #e2e8f0;
  padding: 6px 14px;
  font-size: 12px;
  font-family: 'Inter', sans-serif;
  width: 220px;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}
#search:focus {
  border-color: #a855f7;
  box-shadow: 0 0 0 3px rgba(168,85,247,0.15);
}
#search::placeholder { color: #475569; }
.btn {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 8px;
  color: #94a3b8;
  font-size: 11px;
  font-family: 'Inter', sans-serif;
  padding: 6px 14px;
  cursor: pointer;
  transition: all 0.15s;
}
.btn:hover { background: rgba(255,255,255,0.1); color: #e2e8f0; }
.btn.active { background: rgba(168,85,247,0.15); border-color: rgba(168,85,247,0.3); color: #a855f7; }

/* ── Graph canvas ── */
#graph {
  position: fixed;
  top: 54px; left: 0; right: 0; bottom: 0;
  z-index: 1;
}

/* ── Legend ── */
#legend {
  position: fixed;
  bottom: 28px;
  left: 24px;
  background: rgba(7,8,16,0.9);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  padding: 18px 22px;
  z-index: 100;
  backdrop-filter: blur(24px);
  min-width: 230px;
  box-shadow: 0 8px 40px rgba(0,0,0,0.4);
}
#legend h3 {
  font-size: 9px;
  font-weight: 700;
  color: #475569;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 14px;
}
.legend-item {
  display: flex;
  align-items: center;
  gap: 9px;
  margin-bottom: 7px;
  font-size: 11px;
  color: #94a3b8;
  cursor: pointer;
  border-radius: 6px;
  padding: 3px 6px;
  transition: background 0.15s, opacity 0.15s;
}
.legend-item:hover { background: rgba(255,255,255,0.05); }
.legend-item.inactive { opacity: 0.3; }
.legend-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
  box-shadow: 0 0 8px currentColor;
}

/* ── Tooltip ── */
#tooltip {
  position: fixed;
  display: none;
  background: rgba(10,12,24,0.97);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 12px;
  padding: 16px 20px;
  z-index: 300;
  max-width: 340px;
  backdrop-filter: blur(24px);
  box-shadow: 0 12px 48px rgba(0,0,0,0.6), 0 0 0 1px rgba(255,255,255,0.04);
  pointer-events: none;
}
#tooltip h4 {
  font-size: 13px;
  font-weight: 600;
  color: #f1f5f9;
  margin-bottom: 8px;
  line-height: 1.35;
  max-width: 300px;
}
#tooltip .domain-badge {
  display: inline-block;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 3px 9px;
  border-radius: 20px;
  margin-bottom: 10px;
}
#tooltip .meta {
  font-size: 11px;
  color: #64748b;
  line-height: 1.7;
}
#tooltip .meta strong { color: #94a3b8; }
#tooltip .links-row, #tooltip .tags-row {
  margin-top: 8px;
  font-size: 10px;
  color: #475569;
  word-break: break-all;
}
#tooltip .links-row span, #tooltip .tags-row span {
  background: rgba(255,255,255,0.06);
  border-radius: 4px;
  padding: 2px 6px;
  margin: 2px;
  display: inline-block;
  color: #94a3b8;
  font-size: 10px;
}

/* ── Zoom hint ── */
#zoom-hint {
  position: fixed;
  bottom: 28px;
  right: 24px;
  font-size: 10px;
  color: #334155;
  z-index: 100;
}

/* ── Loading ── */
#loading {
  position: fixed;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #070810;
  z-index: 999;
  transition: opacity 0.8s;
}
#loading.fade { opacity: 0; pointer-events: none; }
.loading-title { font-size: 22px; font-weight: 700; color: #e2e8f0; margin-bottom: 10px; }
.loading-title .accent { color: #a855f7; }
.loading-sub { font-size: 13px; color: #475569; margin-bottom: 28px; }
.spinner {
  width: 40px; height: 40px;
  border: 3px solid rgba(168,85,247,0.12);
  border-top-color: #a855f7;
  border-radius: 50%;
  animation: spin 0.9s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* ── Comm badge in legend ── */
.comm-header {
  font-size: 9px;
  font-weight: 700;
  color: #334155;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin: 14px 0 8px 6px;
  border-top: 1px solid rgba(255,255,255,0.05);
  padding-top: 10px;
}
</style>
</head>
<body>

<canvas id="bg-canvas"></canvas>

<div id="loading">
  <div class="loading-title">🧠 Second Brain <span class="accent">Graph</span></div>
  <div class="loading-sub">Rendering knowledge…</div>
  <div class="spinner"></div>
</div>

<div id="header">
  <h1><span class="emoji">🧠</span> <span>Second Brain</span> <span class="accent">Knowledge Graph</span></h1>
  <div id="stats"></div>
  <div id="controls">
    <input id="search" type="text" placeholder="🔍 Search notes…">
    <button class="btn" id="reset-zoom">Reset View</button>
    <button class="btn" id="toggle-tags">Tags: On</button>
    <button class="btn" id="toggle-communities">Communities</button>
  </div>
</div>

<div id="graph"></div>

<div id="legend">
  <h3>Domains</h3>
  <div id="legend-items"></div>
</div>

<div id="zoom-hint">Scroll to zoom · Drag to pan · Hover for details</div>

<div id="tooltip">
  <h4 id="tt-title"></h4>
  <div id="tt-domain"></div>
  <div class="meta" id="tt-meta"></div>
  <div class="links-row" id="tt-links"></div>
  <div class="tags-row" id="tt-tags"></div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<script>
// ── Nebula background ─────────────────────────────────────────────────────────
(function() {
  const canvas = document.getElementById('bg-canvas');
  const ctx = canvas.getContext('2d');
  let W, H, stars = [], nebula = [];

  function resize() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  // Stars
  for (let i = 0; i < 200; i++) {
    stars.push({
      x: Math.random() * W, y: Math.random() * H,
      r: Math.random() * 1.2 + 0.2,
      speed: Math.random() * 0.003 + 0.001,
      opacity: Math.random() * 0.4 + 0.1,
    });
  }

  // Nebula blobs (colored radial gradients)
  const nebulaColors = [
    'rgba(168,85,247,',   // purple
    'rgba(56,189,248,',   // blue
    'rgba(34,211,238,',   // cyan
    'rgba(244,114,182,',  // pink
    'rgba(251,191,36,',   // amber
  ];
  for (let i = 0; i < 5; i++) {
    nebula.push({
      x: Math.random() * W,
      y: Math.random() * H,
      r: Math.random() * 300 + 150,
      color: nebulaColors[i % nebulaColors.length],
      opacity: Math.random() * 0.04 + 0.02,
      speed: Math.random() * 0.0003 + 0.0001,
    });
  }

  let t = 0;
  function draw() {
    ctx.clearRect(0, 0, W, H);
    t += 0.001;

    // Nebula
    nebula.forEach((n, i) => {
      const offset = Math.sin(t * 2 + i) * 20;
      const g = ctx.createRadialGradient(n.x + offset, n.y + Math.cos(t + i) * 15, 0, n.x + offset, n.y + Math.cos(t + i) * 15, n.r);
      g.addColorStop(0, n.color + (n.opacity * 2).toFixed(3) + ')');
      g.addColorStop(1, n.color + '0)');
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(n.x + offset, n.y + Math.cos(t + i) * 15, n.r, 0, Math.PI * 2);
      ctx.fill();
    });

    // Stars
    stars.forEach(s => {
      s.opacity += Math.sin(t * 10 + s.r * 10) * 0.002;
      s.opacity = Math.max(0.05, Math.min(0.5, s.opacity));
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255,255,255,${s.opacity.toFixed(3)})`;
      ctx.fill();
    });

    requestAnimationFrame(draw);
  }
  draw();
})();
</script>

<script>
const GRAPH_DATA = __GRAPH_DATA__;

// ── Prep ───────────────────────────────────────────────────────────────────────
const nodes = GRAPH_DATA.nodes.map(n => ({...n}));
const links = GRAPH_DATA.links.map(l => ({...l}));

const nodeCount = nodes.length;
const edgeCount = links.length;
const domainCount = [...new Set(nodes.map(n => n.domain))].length;
document.getElementById('stats').textContent =
  `${nodeCount} nodes  ·  ${edgeCount} edges  ·  ${domainCount} domains`;

// ── Legend ─────────────────────────────────────────────────────────────────────
const DOMAIN_COLORS = __DOMAIN_COLORS_JSON__;
const allDomains = Object.keys(DOMAIN_COLORS).filter(d => d !== 'tag' && d !== 'default');
allDomains.sort();

const legendEl = document.getElementById('legend-items');
const activeDomains = new Set(allDomains);

allDomains.forEach(domain => {
  const color = DOMAIN_COLORS[domain] || '#475569';
  const item = document.createElement('div');
  item.className = 'legend-item';
  item.dataset.domain = domain;
  item.innerHTML = `<div class="legend-dot" style="background:${color};color:${color}"></div><span>${domain}</span>`;
  item.addEventListener('click', () => {
    if (activeDomains.has(domain)) {
      activeDomains.delete(domain);
      item.classList.add('inactive');
    } else {
      activeDomains.add(domain);
      item.classList.remove('inactive');
    }
    updateVisibility();
  });
  legendEl.appendChild(item);
});

// ── Force simulation ──────────────────────────────────────────────────────────
const width  = window.innerWidth;
const height = window.innerHeight - 54;

const svgEl = document.getElementById('graph');
const svg = d3.select(svgEl)
  .append('svg')
  .attr('width', width)
  .attr('height', height);

const defs = svg.append('defs');

// Glow filter (stronger)
const makeGlow = (id, blur, color) => {
  const f = defs.append('filter').attr('id', id).attr('x', '-100%').attr('y', '-100%').attr('width', '300%').attr('height', '300%');
  f.append('feGaussianBlur').attr('stdDeviation', blur).attr('result', 'blur');
  const merge = f.append('feMerge');
  merge.append('feMergeNode').attr('in', 'blur');
  merge.append('feMergeNode').attr('in', 'SourceGraphic');
};

makeGlow('glow-sm', 3, 'currentColor');
makeGlow('glow-md', 6, 'currentColor');
makeGlow('glow-lg', 12, 'currentColor');

// Radial gradient for tags
const tagGrad = defs.append('radialGradient').attr('id','tag-grad');
tagGrad.append('stop').attr('offset','0%').attr('stop-color','#ffffff').attr('stop-opacity','0.95');
tagGrad.append('stop').attr('offset','100%').attr('stop-color','#94a3b8').attr('stop-opacity','0.5');

// Community color scale
const commIds = [...new Set(nodes.map(n => n.community))];
const commColor = d3.scaleOrdinal()
  .domain(commIds)
  .range(d3.schemeTableau10);

// Background gradient
const bgGrad = defs.append('radialGradient').attr('id','bg-grad').attr('cx','50%').attr('cy','35%').attr('r','65%');
bgGrad.append('stop').attr('offset','0%').attr('stop-color','#0f1525');
bgGrad.append('stop').attr('offset','100%').attr('stop-color','#070810');

svg.append('rect')
  .attr('width', width).attr('height', height)
  .attr('fill', 'url(#bg-grad)');

// Container for zoom
const g = svg.append('g');

// Zoom
const zoom = d3.zoom()
  .scaleExtent([0.05, 15])
  .on('zoom', e => g.attr('transform', e.transform));
svg.call(zoom);

d3.select('#reset-zoom').on('click', () => svg.transition().duration(700).call(zoom.transform, d3.zoomIdentity));

// ── Links ─────────────────────────────────────────────────────────────────────
const link = g.append('g').attr('class','links')
  .selectAll('line')
  .data(links)
  .join('line')
  .attr('stroke', d => {
    const src = nodes.find(n => n.id === (d.source.id || d.source));
    if (!src) return 'rgba(100,116,139,0.15)';
    return src.color + '30';
  })
  .attr('stroke-width', 1)
  .attr('stroke-opacity', 0.5)
  .attr('stroke-linecap', 'round');

// ── Nodes ─────────────────────────────────────────────────────────────────────
const node = g.append('g').attr('class','nodes')
  .selectAll('circle')
  .data(nodes)
  .join('circle')
  .attr('r', d => d.size)
  .attr('fill', d => {
    if (d.id.startsWith('#')) return 'url(#tag-grad)';
    return d.color;
  })
  .attr('stroke', d => {
    if (d.id.startsWith('#')) return 'rgba(255,255,255,0.2)';
    if (d.degree > 15) return d.color;
    return 'rgba(255,255,255,0.12)';
  })
  .attr('stroke-width', d => {
    if (d.id.startsWith('#')) return 0.5;
    if (d.degree > 15) return 2;
    return 1;
  })
  .attr('filter', d => {
    if (d.id.startsWith('#')) return null;
    if (d.degree > 20) return 'url(#glow-lg)';
    if (d.degree > 12) return 'url(#glow-md)';
    if (d.degree > 6) return 'url(#glow-sm)';
    return null;
  })
  .attr('cursor', 'pointer')
  .attr('opacity', d => (d.id.startsWith('#') && !activeDomains.has('tag')) ? 0.2 : 1);

// ── Community rings ────────────────────────────────────────────────────────────
let showCommunities = false;
let commRing = g.append('g').attr('class','comm-rings').style('display', 'none');

function renderCommRings() {
  commRing.selectAll('circle').remove();
  if (!showCommunities) return;
  const commNodes = d3.group(nodes, d => d.community);
  commNodes.forEach((members, cid) => {
    if (members.length < 3) return;
    const cx = d3.mean(members, n => n.x || 0);
    const cy = d3.mean(members, n => n.y || 0);
    const r = d3.max(members, n => {
      const dx = (n.x || 0) - cx, dy = (n.y || 0) - cy;
      return Math.sqrt(dx*dx + dy*dy);
    }) + 20;
    commRing.append('circle')
      .attr('cx', cx).attr('cy', cy).attr('r', r)
      .attr('fill', 'none')
      .attr('stroke', commColor(cid))
      .attr('stroke-width', 1.5)
      .attr('stroke-opacity', 0.25)
      .attr('stroke-dasharray', '4,4');
  });
}

d3.select('#toggle-communities').on('click', function() {
  showCommunities = !showCommunities;
  this.classList.toggle('active', showCommunities);
  commRing.style('display', showCommunities ? null : 'none');
  if (showCommunities) renderCommRings();
});

// ── Labels ────────────────────────────────────────────────────────────────────
const label = g.append('g').attr('class','labels')
  .selectAll('text')
  .data(nodes.filter(n => n.degree > 6 && !n.id.startsWith('#')))
  .join('text')
  .text(d => d.label)
  .attr('font-size', d => Math.min(11, 6 + d.degree * 0.25))
  .attr('font-family', 'Inter, sans-serif')
  .attr('font-weight', '600')
  .attr('fill', d => d.color)
  .attr('opacity', 0.9)
  .attr('pointer-events', 'none')
  .attr('text-anchor', 'middle')
  .attr('dy', d => -d.size - 5)
  .attr('paint-order', 'stroke')
  .attr('stroke', '#070810')
  .attr('stroke-width', 3)
  .attr('stroke-linejoin', 'round');

// ── Tooltip ───────────────────────────────────────────────────────────────────
const tooltip = document.getElementById('tooltip');
const ttTitle  = document.getElementById('tt-title');
const ttDomain = document.getElementById('tt-domain');
const ttMeta   = document.getElementById('tt-meta');
const ttLinks  = document.getElementById('tt-links');
const ttTags   = document.getElementById('tt-tags');

node.on('mousemove', (event, d) => {
  tooltip.style.display = 'block';
  tooltip.style.left = (event.clientX + 18) + 'px';
  tooltip.style.top  = (event.clientY - 10) + 'px';

  ttTitle.textContent = d.label;
  const color = d.color;
  ttDomain.innerHTML  = `<span class="domain-badge" style="background:${color}22;color:${color};border:1px solid ${color}44">${d.domain}</span>`;
  ttMeta.innerHTML    = `<strong>Degree</strong> ${d.degree} &nbsp;·&nbsp; <strong>Community</strong> ${d.community} &nbsp;·&nbsp; <strong>Links</strong> ${d.links.length}`;

  const linkNames = d.links.slice(0, 6).map(l => {
    const name = l.split('|')[0].split('/').pop().substring(0, 30);
    return `<span>${name}</span>`;
  }).join('');
  ttLinks.innerHTML = linkNames ? `<strong>Links:</strong> ${linkNames}` : '';

  const tagNames = d.tags.slice(0, 6).map(t => `<span>#${t}</span>`).join('');
  ttTags.innerHTML = tagNames ? `<strong>Tags:</strong> ${tagNames}` : '';

  // Keep tooltip on screen
  const rect = tooltip.getBoundingClientRect();
  if (rect.right > window.innerWidth)  tooltip.style.left = (event.clientX - rect.width - 18) + 'px';
  if (rect.bottom > window.innerHeight) tooltip.style.top  = (event.clientY - rect.height - 10) + 'px';
})
.on('mouseleave', () => { tooltip.style.display = 'none'; });

// ── Drag ─────────────────────────────────────────────────────────────────────
const drag = d3.drag()
  .on('start', (e, d) => {
    if (!e.active) sim.alphaTarget(0.3).restart();
    d.fx = d.x; d.fy = d.y;
  })
  .on('drag', (e, d) => { d.fx = e.x; d.fy = e.y; })
  .on('end', (e, d) => {
    if (!e.active) sim.alphaTarget(0);
    d.fx = null; d.fy = null;
  });
node.call(drag);

// ── Force simulation ─────────────────────────────────────────────────────────
const sim = d3.forceSimulation(nodes)
  .force('link',      d3.forceLink(links).id(d => d.id).distance(70).strength(0.35))
  .force('charge',    d3.forceManyBody().strength(-250).distanceMax(500))
  .force('center',    d3.forceCenter(width / 2, height / 2).strength(0.06))
  .force('collide',   d3.forceCollide(d => d.size + 5).strength(0.8))
  .force('x',         d3.forceX(width  / 2).strength(0.025))
  .force('y',         d3.forceY(height / 2).strength(0.025))
  .on('tick', () => {
    link.attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
    node.attr('cx', d => d.x).attr('cy', d => d.y);
    label.attr('x', d => d.x).attr('y', d => d.y);
    if (showCommunities) renderCommRings();
  });

// ── Search ────────────────────────────────────────────────────────────────────
const searchEl = document.getElementById('search');
let searchActive = false;
searchEl.addEventListener('input', () => {
  const q = searchEl.value.toLowerCase().trim();
  searchActive = !!q;
  node.attr('opacity', d => {
    if (!q) return 1;
    return d.label.toLowerCase().includes(q) || d.domain.toLowerCase().includes(q) ? 1 : 0.06;
  });
  label.attr('opacity', d => {
    if (!q) return 0.9;
    return d.label.toLowerCase().includes(q) ? 1 : 0.03;
  });
  link.attr('stroke-opacity', d => {
    if (!q) return 0.5;
    const src = d.source.label || d.source.id || '';
    const tgt = d.target.label || d.target.id || '';
    return (src.toLowerCase().includes(q) || tgt.toLowerCase().includes(q)) ? 0.7 : 0.04;
  });
});

// ── Toggle tags ───────────────────────────────────────────────────────────────
let tagsVisible = true;
d3.select('#toggle-tags').on('click', function() {
  tagsVisible = !tagsVisible;
  this.textContent = `Tags: ${tagsVisible ? 'On' : 'Off'}`;
  this.classList.toggle('active', !tagsVisible);
  node.attr('opacity', d => {
    if (d.id.startsWith('#')) return tagsVisible ? 0.85 : 0;
    if (searchActive) {
      const q = searchEl.value.toLowerCase();
      return d.label.toLowerCase().includes(q) || d.domain.toLowerCase().includes(q) ? 1 : 0.06;
    }
    return 1;
  });
});

// ── Domain filter ─────────────────────────────────────────────────────────────
function updateVisibility() {
  node.attr('opacity', d => {
    if (d.id.startsWith('#')) return tagsVisible ? 0.85 : 0;
    if (!activeDomains.has(d.domain)) return 0.05;
    if (searchActive) {
      const q = searchEl.value.toLowerCase();
      return d.label.toLowerCase().includes(q) || d.domain.toLowerCase().includes(q) ? 1 : 0.06;
    }
    return 1;
  });
  label.attr('opacity', d => {
    if (!activeDomains.has(d.domain)) return 0;
    if (searchActive) {
      return d.label.toLowerCase().includes(searchEl.value.toLowerCase()) ? 1 : 0.03;
    }
    return 0.9;
  });
  link.attr('stroke-opacity', d => searchActive ? 0.5 : 0.5);
}

// ── Init ──────────────────────────────────────────────────────────────────────
setTimeout(() => {
  const el = document.getElementById('loading');
  el.classList.add('fade');
  setTimeout(() => el.remove(), 800);
}, 600);
</script>
</body>
</html>"""

# ── Inject data ──────────────────────────────────────────────────────────────
domain_colors_json = json.dumps(DOMAIN_PALETTE, indent=2)
html = html.replace("__GRAPH_DATA__", json.dumps(graph_data, indent=2))
html = html.replace("__DOMAIN_COLORS_JSON__", domain_colors_json)

OUT.write_text(html, encoding="utf-8")
print(f"\n✅ Saved: {OUT}")
print(f"   Open: file:///{OUT.as_posix().replace(chr(92), '/')}")
print(f"   {len(node_list)} nodes · {len(edge_list)} edges")