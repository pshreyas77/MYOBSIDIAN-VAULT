#!/usr/bin/env python3
"""
Professional Obsidian Knowledge Graph
======================================
Builds a colorful, community-detected, hover-rich knowledge graph
from your Obsidian vault's wikilinks and tags.

Usage: python graphify_vault.py
Output: obsidian_graph.html (open in any browser)
"""
import re, json
from pathlib import Path
import networkx as nx
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from collections import Counter

VAULT = Path("E:/_Knowledge/ObsidianVault")
OUT = VAULT / "obsidian_graph.html"

# ── Domain color palette ──────────────────────────────────────────────────────
DOMAIN_PALETTE = {
    "Indian Political History": "#e74c3c",
    "Dravidian Politics / Tamil Nadu": "#c0392b",
    "Aryan Migration / IVC / DNA": "#9b59b6",
    "RSS / Hindutva / Sangh Parivar": "#e74c3c",
    "Philosophy & Religion": "#8e44ad",
    "Buddhism / Shramana": "#d35400",
    "Anti-Caste / Ambedkar / Phule": "#2c3e50",
    "AI & Technology / PKM": "#3498db",
    "Health & Fitness": "#27ae60",
    "Agentic Systems": "#e67e22",
    "Second Brain / LLM Wiki": "#00b4d8",
    "Projects / PARA": "#ff9ff3",
    "Daily Notes / Logs": "#54a0ff",
    "Maps / MOCs": "#5f27cd",
    "System / Infrastructure": "#1dd1a1",
    "Sources / Literature": "#feca57",
    "Output / Analyses": "#00d2d3",
    "tag": "#ffffff",
    "default": "#636e72",
}

def classify_node(name):
    """Assign domain + color to a node based on its path."""
    n = name.lower()
    if any(k in n for k in ["indian political history moc", "justice party", "periyar", "karunanidhi", "anna", "m.gr", "kamaraj", "neethi", "bjp south", "election"]):
        return "Indian Political History"
    if any(k in n for k in ["dravidian", "dmk", "aiadmk", "tamil nadu", "tamil politics", "dmk aiadmk"]):
        return "Dravidian Politics / Tamil Nadu"
    if any(k in n for k in ["aryan", "indus valley", "ivc", "steppe", "rakhigarhi", "harappan", "pre-aryan", "migration", "ancient dna"]):
        return "Aryan Migration / IVC / DNA"
    if any(k in n for k in ["rss", "hindutva", "sangh", "bhutada", "sewa international", "sewa international", "hindu"]):
        return "RSS / Hindutva / Sangh Parivar"
    if any(k in n for k in ["philosophy", "religion", "vedanta", "kant", "shankara", " Advaita"]):
        return "Philosophy & Religion"
    if any(k in n for k in ["buddhism", "buddha", "buddhist", "dhamma", "sangha", "mahayana", "theravada"]):
        return "Buddhism / Shramana"
    if any(k in n for k in ["anti-caste", "ambedkar", "dalit", "phule", "jyotirao", "maharashtra"]):
        return "Anti-Caste / Ambedkar / Phule"
    if any(k in n for k in ["agentic", "autonomous agent", "genericagent", "night shift"]):
        return "Agentic Systems"
    if any(k in n for k in ["health", "fitness", "supplement", "workout", "tier", "ppl", "gym"]):
        return "Health & Fitness"
    if any(k in n for k in ["moc", "map of content", "maps", "index"]):
        return "Maps / MOCs"
    if any(k in n for k in ["04 - daily", "daily note", "night-shift-log"]):
        return "Daily Notes / Logs"
    if any(k in n for k in ["01 - literature", "literature", "articles", "research"]):
        return "Sources / Literature"
    if any(k in n for k in ["06 - outputs", "outputs", "analysis", "synthesis"]):
        return "Output / Analyses"
    if any(k in n for k in ["03 - projects", "project", "cross-domain"]):
        return "Projects / PARA"
    if any(k in n for k in ["07 - system", "system", "vault-health", "ai-first"]):
        return "System / Infrastructure"
    if any(k in n for k in ["ai", "llm", "claude", "obsidian", "second brain", "zettel", "pkm", "wiki", "knowledge graph", "note-taking"]):
        return "AI & Technology / PKM"
    if name.startswith("#"):
        return "tag"
    return "default"


# ── Parse vault ───────────────────────────────────────────────────────────────
def get_links(text):
    return re.findall(r'\[\[(.*?)\]\]', text)

def get_tags(text):
    return re.findall(r'(?<!\w)#([\w/-]+)', text)

G = nx.Graph()
nodes_meta = {}

EXCLUDE = {'.obsidian', '.smart-env', '.git', 'node_modules', '_trash',
          '.graphify', 'trash', '.trash'}

for md in VAULT.glob("**/*.md"):
    name = str(md.relative_to(VAULT)).replace(".md", "")
    if any(e in name for e in EXCLUDE):
        continue
    try:
        text = md.read_text(encoding="utf-8", errors="ignore")
        domain = classify_node(name)
        nodes_meta[name] = {"domain": domain, "color": DOMAIN_PALETTE.get(domain, DOMAIN_PALETTE["default"]),
                            "degree": 0, "links": [], "tags": []}
        G.add_node(name, domain=domain)

        for tag in get_tags(text):
            tn = f"#{tag}"
            if tn not in nodes_meta:
                G.add_node(tn, domain="tag")
                nodes_meta[tn] = {"domain": "tag", "color": "#ffffff", "degree": 0, "links": [], "tags": []}
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

# ── Filter isolated nodes ──────────────────────────────────────────────────────
deg = dict(G.degree())
# Keep top nodes by degree — cap at 500 to keep layout fast
all_nodes = sorted(G.nodes(), key=lambda n: deg.get(n, 0), reverse=True)
if len(all_nodes) > 500:
    keep = set(all_nodes[:500])
    for n in list(G.nodes()):
        if n not in keep:
            G.remove_node(n)
print(f"Graph built: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

for n in G.nodes():
    nodes_meta.setdefault(n, {"domain": classify_node(n),
                              "color": DOMAIN_PALETTE.get(classify_node(n), "#636e72"),
                              "degree": 0, "links": [], "tags": []})
    nodes_meta[n]["degree"] = deg.get(n, 0)

# ── Community detection ───────────────────────────────────────────────────────
try:
    import community as community_louvain
    communities = community_louvain.best_partition(G.to_undirected())
    modularity = community_louvain.modularity(communities, G.to_undirected())
    print(f"Communities (Louvain): {len(set(communities.values()))}, modularity={modularity:.3f}")
except Exception:
    # Fallback: label propagation
    from networkx.algorithms import community as nx_comm
    communities = {n: i % 12 for i, n in enumerate(G.nodes())}
    print("Communities (label prop fallback):", len(set(communities.values())))

COMMUNITY_PALETTE = [
    "#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6",
    "#1abc9c", "#e67e22", "#ff6b6b", "#00cec9", "#a29bfe",
    "#fd79a8", "#00b894",
]

for n, cid in communities.items():
    nodes_meta.setdefault(n, {"domain": "default", "color": "#636e72",
                               "degree": 0, "links": [], "tags": []})
    # Override: color by community for non-tags, keep tag color
    if not n.startswith("#") and nodes_meta[n]["domain"] != "tag":
        nodes_meta[n]["community"] = cid
        nodes_meta[n]["color"] = COMMUNITY_PALETTE[cid % len(COMMUNITY_PALETTE)]

# ── Layout ─────────────────────────────────────────────────────────────────────
pos = nx.spring_layout(G.to_undirected(), k=0.8, iterations=30, seed=42)

# ── Build Plotly traces ────────────────────────────────────────────────────────
# Edges
edge_x, edge_y = [], []
for u, v in G.edges():
    if u in pos and v in pos:
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    mode="lines",
    line=dict(width=0.8, color="rgba(150,150,150,0.35)"),
    hoverinfo="none",
    zorder=1,
)

# Nodes
node_x, node_y, node_text, node_color, node_size, node_hover_text = [], [], [], [], [], []
for n in G.nodes():
    if n not in pos:
        continue
    x, y = pos[n]
    node_x.append(x)
    node_y.append(y)
    d = nodes_meta.get(n, {})
    label = n.split("/")[-1][:60]
    node_text.append(label)

    deg_val = d.get("degree", 1)
    size = 6 if n.startswith("#") else max(6, min(28, 4 + deg_val * 1.2))
    node_size.append(size)
    node_color.append(d.get("color", "#636e72"))

    # Build hover text
    links_s = d.get("links", [])[:8]
    tags_s = d.get("tags", [])[:6]
    community = d.get("community", "?")
    domain = d.get("domain", "unknown")
    hover = (
        f"<b>{label}</b><br>"
        f"<i>{domain}</i><br>"
        f"Degree: {deg_val}<br>"
        f"Community: {community}<br>"
        f"Links: {', '.join(l[:30] for l in links_s[:5])}{'...' if len(links_s) > 5 else ''}<br>"
        f"Tags: {', '.join('#'+t for t in tags_s[:4])}{'...' if len(tags_s) > 4 else ''}"
    )
    node_hover_text.append(hover)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode="markers+text",
    text=node_text,
    textposition="top center",
    textfont=dict(size=7, color="#2c3e50"),
    marker=dict(
        size=node_size,
        color=node_color,
        line=dict(width=1, color="white"),
        opacity=0.92,
    ),
    hovertext=node_hover_text,
    hoverinfo="text",
    zorder=2,
)

# ── Figure ────────────────────────────────────────────────────────────────────
fig = go.Figure(data=[edge_trace, node_trace])

# Stats banner
total = G.number_of_nodes()
edges_n = G.number_of_edges()
communities_n = len(set(communities.values()))
title = (
    f"<b>Shreyas's Second Brain — Knowledge Graph</b>  |  "
    f"{total} nodes  ·  {edges_n} links  ·  {communities_n} communities"
)

fig.update_layout(
    title=dict(text=title, x=0.5, font=dict(size=16, color="#2c3e50", family="Arial Black")),
    showlegend=False,
    hovermode="closest",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, fixedrange=True),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, fixedrange=True),
    width=1600, height=1000,
    plot_bgcolor="#f8f9fa",
    paper_bgcolor="#ffffff",
    margin=dict(l=30, r=30, t=80, b=30),
    annotations=[
        dict(
            text="🧠 Nodes colored by community · Sized by degree · Hover for details",
            showarrow=False,
            x=0.5, y=-0.04,
            xref="paper", yref="paper",
            font=dict(size=11, color="#7f8c8d"),
        )
    ],
)

fig.write_html(OUT.as_posix(), include_plotlyjs="cdn", full_html=True)
print(f"\n✅ Saved: {OUT}")
print(f"   Open in browser: file:///{OUT.as_posix().replace(chr(92), '/')}")