import json
import re

# Read the backup file  
with open("World Philosophers Encyclopedia.backup.canvas", "r") as f:
    content = f.read()

# Extract all valid nodes using regex
# Pattern matches complete node objects
node_pattern = r'\{\s*"id"\s*:\s*"[^"]+"\s*,\s*"type"\s*:\s*"text"[^}]*"[^}]+"\s*,\s*"x"\s*:\s*[-\d]+\s*,\s*"y"\s*:\s*[-\d]+\s*,\s*"width"\s*:\s*\d+\s*,\s*"height"\s*:\s*\d+[^}]*\}'
nodes_matches = re.findall(node_pattern, content, re.DOTALL)

nodes = []
for nm in nodes_matches:
    try:
        n = json.loads(nm)
        if n.get('id') not in ['socrates_img']:
            nodes.append(n)
    except:
        pass

# Also need to find the socrates node separately (it was split)
# Find socrates entry
socrates_match = re.search(r'"id":"socrates"[^}]*"text":"## Socrates[^"]*"[^,]*', content)
if socrates_match:
    # Find the full socrates node
    soc_start = content.find('"id":"socrates"')
    if soc_start != -1:
        # Find from "id":"socrates" to the next complete node
        soc_section = content[soc_start:soc_start+800]
        # Try to construct it
        try:
            # Manual extraction based on pattern
            soc_id = "socrates"
            soc_text_match = re.search(r'"id":"socrates"[^,]*,"type":"text","text":"([^"]*)"', content)
            if soc_text_match:
                soc_text = soc_text_match.group(1).replace('\\"', '"')
            soc_coords = re.search(r'"id":"socrates"[^}]*"x":(-?\d+),"y":(-?\d+),"width":(\d+),"height":(\d+)', content)
            if soc_coords:
                sx, sy, sw, sh = soc_coords.groups()
                socrates_node = {
                    "id": "socrates",
                    "type": "text", 
                    "text": "## Socrates\n**470-399 BCE** | Classical\n\nSocratic method (elenchus). \"Know thyself\" - virtue is knowledge. Executed 399 BCE by hemlock. Shifted philosophy to ethics",
                    "x": int(sx),
                    "y": int(sy),
                    "width": int(sw),
                    "height": int(sh),
                    "color": "5"
                }
                nodes.append(socrates_node)
        except Exception as e:
            print(f"Error extracting socrates: {e}")

# Remove duplicates
seen_ids = set()
unique_nodes = []
for n in nodes:
    if n['id'] not in seen_ids:
        seen_ids.add(n['id'])
        unique_nodes.append(n)

print(f"Total unique nodes: {len(unique_nodes)}")

# Extract edges
edge_pattern = r'\{\s*"id"\s*:\s*"e[^"]*"[^}]*"fromNode"[^}]*"toNode"[^}]*\}'
edges_matches = re.findall(edge_pattern, content, re.DOTALL)
edges = []
for em in edges_matches:
    try:
        e = json.loads(em)
        edges.append(e)
    except:
        pass

print(f"Total edges: {len(edges)}")

# Build clean canvas
canvas = {
    "nodes": unique_nodes,
    "edges": edges,
    "metadata": {
        "version": "1.0-1.0",
        "frontmatter": {}
    }
}

# Save
def custom_json_dump(obj, indent=0):
    if isinstance(obj, dict):
        if len(obj) == 0:
            return "{}"
        items = []
        for k, v in obj.items():
            key = json.dumps(k)
            val = custom_json_dump(v, indent + 1)
            items.append(f'{key}:{val}')
        return "{" + ",".join(items) + "}"
    elif isinstance(obj, list):
        if len(obj) == 0:
            return "[]"
        items = [custom_json_dump(item, indent + 1) for item in obj]
        return "[" + ",".join(items) + "]"
    else:
        return json.dumps(obj)

# Use standard json dump with custom formatting
with open("World Philosophers Encyclopedia.canvas", "w") as f:
    f.write('{ "nodes":[')
    for i, node in enumerate(unique_nodes):
        if i > 0:
            f.write(',')
        f.write(json.dumps(node))
    f.write('], "edges":[')
    for i, edge in enumerate(edges):
        if i > 0:
            f.write(',')
        f.write(json.dumps(edge))
    f.write('], "metadata": {"version":"1.0-1.0","frontmatter":{}} }')

print("Saved!")

# Verify
with open("World Philosophers Encyclopedia.canvas", "r") as f:
    test = json.load(f)
print(f"Verification: {len(test['nodes'])} nodes, {len(test['edges'])} edges")
