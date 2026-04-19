import json

with open("World Philosophers Encyclopedia.canvas", "r") as f:
    data = json.load(f)

images = {
    "socrates": {"file": "Philosophers Canvas/images/socrates.jpg", "y_offset": -200},
    "plato": {"file": "Philosophers Canvas/images/plato.jpg", "y_offset": -200},
    "aristotle": {"file": "Philosophers Canvas/images/aristotle.jpg", "y_offset": -200},
    "confucius": {"file": "Philosophers Canvas/images/confucius.jpg", "y_offset": -200},
    "kant": {"file": "Philosophers Canvas/images/kant.jpg", "y_offset": -240},
    "nietzsche": {"file": "Philosophers Canvas/images/nietzsche.jpg", "y_offset": -200},
}

nodes_added = 0
for node in list(data["nodes"]):
    nid = node.get("id")
    if nid in images:
        img = images[nid]
        img_node = {
            "id": f"{nid}_img",
            "type": "file",
            "file": img["file"],
            "x": node.get("x", 0),
            "y": node.get("y", 0) + img["y_offset"],
            "width": 120,
            "height": 150
        }
        edge = {
            "id": f"e_{nid}_img",
            "fromNode": f"{nid}_img",
            "fromSide": "bottom",
            "toNode": nid,
            "toSide": "top"
        }
        data["nodes"].append(img_node)
        data["edges"].append(edge)
        nodes_added += 1

with open("World Philosophers Encyclopedia.canvas", "w") as f:
    json.dump(data, f)

print(f"Added {nodes_added} image nodes")
