#!/usr/bin/env python3
import streamlit as st
import re
import json
from pathlib import Path
from rag import build_chain

st.set_page_config(page_title="Obsidian RAG", page_icon="🧠", layout="wide")

st.markdown(
    """
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600&family=JetBrains+Mono:wght@300;400&display=swap" rel="stylesheet">
<style>
* { font-family: 'Space Grotesk', sans-serif; }
body, .stApp { background: #0a0a0f !important; color: #e8e6ff; }
#MainMenu, footer, header, [data-testid="stSidebar"] { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; margin: 0 !important; }
.stChatInput > div > div { background: rgba(20,16,40,0.95) !important; border: 1px solid rgba(120,80,255,0.3) !important; border-radius: 12px !important; }
.stChatInput input { color: #e8e6ff !important; background: transparent !important; }
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-thumb { background: rgba(120,80,255,0.3); border-radius: 2px; }
</style>
""",
    unsafe_allow_html=True,
)

VAULT_DIR = "./vault"


def get_graph():
    nodes, edges, links, folders = [], [], {}, {}
    for f in Path(VAULT_DIR).rglob("*.md"):
        try:
            with open(f, "r", encoding="utf-8") as fp:
                content = fp.read()
            title, folder = f.stem, f.parent.name
            if folder not in folders:
                folders[folder] = len(folders)
            nodes.append({"name": title[:15], "fid": folders[folder]})
            for link in re.findall(r"\[\[([^\]]+)\]\]", content):
                if link not in links:
                    links[link] = []
                links[link].append(title)
        except:
            pass
    seen = set()
    for tgt, srcs in links.items():
        for src in srcs:
            eid = f"{src}->{tgt}"
            if eid not in seen:
                edges.append({"source": src, "target": tgt})
                seen.add(eid)
    return {"nodes": nodes[:40], "edges": edges[:50], "folders": folders}


if "msgs" not in st.session_state:
    st.session_state.msgs = []
if "gdata" not in st.session_state:
    st.session_state.gdata = get_graph()

cols = ["#7c3aed", "#a855f7", "#22d3ee", "#f59e0b", "#ec4899", "#3b82f6"]
g = st.session_state.gdata

canvas_html = (
    """
<canvas id="graphCanvas" style="position:fixed;top:0;left:0;width:100%;height:100%;background:#0a0a0f;z-index:0;"></canvas>
<script>
var cols = """
    + json.dumps(cols)
    + """;
var data = """
    + json.dumps(g)
    + """;
var canvas = document.getElementById('graphCanvas');
var ctx = canvas.getContext('2d');
var nodes = [], links = [];
var mx = 0, my = 0;

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

data.nodes.forEach(function(n, i) {
    var hub = i < 5;
    nodes.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: 0, vy: 0,
        name: n.name,
        color: cols[n.fid %% cols.length],
        size: hub ? 8 + Math.random() * 4 : 2 + Math.random() * 2,
        isHub: hub,
        phase: Math.random() * 6.28
    });
});

data.edges.slice(0, 40).forEach(function(e) {
    var s = nodes.find(function(x) { return x.name === e.source; });
    var t = nodes.find(function(x) { return x.name === e.target; });
    if(s && t) links.push({s: s, t: t});
});

canvas.addEventListener('mousemove', function(e) { mx = e.clientX; my = e.clientY; });

function draw() {
    var t = Date.now() * 0.001;
    var w = canvas.width, h = canvas.height, cx = w/2, cy = h/2;
    
    ctx.fillStyle = '#0a0a0f';
    ctx.fillRect(0, 0, w, h);
    
    nodes.forEach(function(n) {
        n.vx += (cx - n.x) * 0.0001;
        n.vy += (cy - n.y) * 0.0001;
        var dx = mx - n.x, dy = my - n.y, d = Math.sqrt(dx*dx + dy*dy);
        if(d < 80) { n.vx -= dx/d * 0.3; n.vy -= dy/d * 0.3; }
        n.vx *= 0.95; n.vy *= 0.95;
        n.x += n.vx; n.y += n.vy;
        n.x = Math.max(10, Math.min(w-10, n.x));
        n.y = Math.max(10, Math.min(h-10, n.y));
    });
    
    links.forEach(function(l) {
        var dx = l.t.x - l.s.x, dy = l.t.y - l.s.y, d = Math.sqrt(dx*dx + dy*dy);
        if(d < 150) {
            ctx.beginPath();
            ctx.strokeStyle = 'rgba(120,80,255,0.15)';
            ctx.lineWidth = 0.5;
            ctx.moveTo(l.s.x, l.s.y);
            ctx.lineTo(l.t.x, l.t.y);
            ctx.stroke();
        }
    });
    
    nodes.forEach(function(n) {
        var sc = n.isHub ? 1 + Math.sin(t*1.5 + n.phase)*0.15 : 1;
        var sz = n.size * sc;
        
        if(n.isHub) {
            var g = ctx.createRadialGradient(n.x, n.y, 0, n.x, n.y, sz*2);
            g.addColorStop(0, n.color + '55');
            g.addColorStop(1, 'transparent');
            ctx.fillStyle = g;
            ctx.beginPath(); ctx.arc(n.x, n.y, sz*2, 0, 6.28); ctx.fill();
        }
        
        ctx.fillStyle = n.color + (n.isHub ? 'dd' : '88');
        ctx.beginPath(); ctx.arc(n.x, n.y, sz, 0, 6.28); ctx.fill();
        
        if(n.isHub) {
            ctx.fillStyle = 'rgba(255,255,255,0.5)';
            ctx.font = '6px Space Grotesk';
            ctx.textAlign = 'center';
            ctx.fillText(n.name.substring(0,8), n.x, n.y + sz + 6);
        }
    });
    requestAnimationFrame(draw);
}
draw();
</script>
"""
)
st.markdown(canvas_html, unsafe_allow_html=True)

st.markdown(
    """
<div style="position:fixed;top:0;left:0;width:60px;height:100%;background:rgba(15,12,30,0.95);border-right:1px solid rgba(120,80,255,0.2);z-index:10;display:flex;flex-direction:column;align-items:center;padding-top:20px;">
<div style="font-size:24px;margin-bottom:30px;">🧠</div>
<div style="width:36px;height:36px;background:linear-gradient(135deg,#7c3aed,#a855f7);border-radius:8px;margin-bottom:20px;"></div>
</div>
<div style="position:fixed;top:16px;left:80px;z-index:10;display:flex;align-items:center;gap:20px;">
<div style="display:flex;align-items:center;gap:8px;font-weight:500;">
<span style="width:8px;height:8px;background:#a855f7;border-radius:50%;animation:p 2s infinite;box-shadow:0 0 8px #a855f7;"></span>
My Vault
</div>
<div style="display:flex;gap:8px;">
<span style="background:rgba(120,80,255,0.15);border:1px solid rgba(120,80,255,0.3);border-radius:12px;padding:4px 12px;font-size:10px;font-family:JetBrains Mono;">"""
    + str(len(g["nodes"]))
    + """ nodes</span>
<span style="background:rgba(120,80,255,0.15);border:1px solid rgba(120,80,255,0.3);border-radius:12px;padding:4px 12px;font-size:10px;font-family:JetBrains Mono;">"""
    + str(len(g["edges"]))
    + """ links</span>
</div>
</div>
<style>@keyframes p {0%,100%{opacity:1}50%{opacity:0.3}}</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div style="position:fixed;bottom:20px;left:50%;transform:translateX(-50%);width:60%;max-width:500px;z-index:20;">
""",
    unsafe_allow_html=True,
)

prompt = st.text_input(
    "",
    placeholder="Ask anything from your vault...",
    key="chat_input",
    label_visibility="collapsed",
)

if prompt:
    with st.spinner("Thinking..."):
        try:
            chain = build_chain()
            result = chain.query_with_sources(prompt)
            st.session_state.msgs.append({"role": "user", "content": prompt})
            st.session_state.msgs.append(
                {"role": "assistant", "content": result["answer"]}
            )
        except Exception as e:
            st.session_state.msgs.append({"role": "user", "content": prompt})
            st.session_state.msgs.append(
                {"role": "assistant", "content": "Error: " + str(e)}
            )
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

for msg in st.session_state.msgs:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
