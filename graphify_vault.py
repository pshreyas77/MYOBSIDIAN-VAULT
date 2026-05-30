#!/usr/bin/env python3
import re, networkx as nx, plotly.graph_objects as go
from pathlib import Path

VAULT = Path(".")
out = VAULT / "obsidian_graph.html"

def links(t): return re.findall(r'\[\[(.*?)\]\]', t)
def tags(t): return re.findall(r'(?<!\w)#([\w/-]+)', t)

G = nx.Graph()
for md in VAULT.glob("**/*.md"):
    name = str(md.relative_to(VAULT)).replace(".md","")
    G.add_node(name, type="note")
    try:
        text = md.read_text()
        for tag in tags(text):
            tn = f"#{tag}"
            G.add_node(tn, type="tag")
            G.add_edge(name, tn)
        for link in links(text):
            target = link.split("|")[0].split("#")[0].strip()
            if target: G.add_edge(name, target)
    except: pass

print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
pos = nx.spring_layout(G, k=0.5)

node_x, node_y, node_text, node_color, node_size = [], [], [], [], []
for n in G.nodes():
    x,y = pos[n]
    node_x.append(x); node_y.append(y); node_text.append(n)
    is_tag = G.nodes[n].get("type")=="tag"
    node_color.append("orange" if is_tag else "lightblue")
    node_size.append(5 if is_tag else 8)

node_trace = go.Scatter(x=node_x, y=node_y, mode='markers+text', text=node_text,
                        textposition="top center", marker=dict(size=node_size, color=node_color))
edge_x, edge_y = [], []
for u,v in G.edges():
    x0,y0 = pos[u]; x1,y1 = pos[v]
    edge_x.extend([x0,x1,None]); edge_y.extend([y0,y1,None])
edge_trace = go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(width=0.5, color='grey'))

fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(title="Obsidian Vault Graph", showlegend=False,
                                 xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                 yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                 width=1200, height=800))
fig.write_html(out.as_posix())
print(f"Saved: {out}")
