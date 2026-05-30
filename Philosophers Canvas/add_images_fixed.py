#!/usr/bin/env python3
import json

with open("World Philosophers Encyclopedia.canvas", "r") as f:
    data = json.load(f)

images = {
    "socrates": {"file": "Philosophers Canvas/images/socrates.jpg", "y_offset": -180},
    "plato": {"file": "Philosophers Canvas/images/plato.jpg", "y_offset": -180},
    "aristotle": {"file": "Philosophers Canvas/images/aristotle.jpg", "y_offset": -180},
    "confucius": {"file": "Philosophers Canvas/images/confucius.jpg", "y_offset": -180},
    "kant": {"file": "Philosophers Canvas/images/kant.jpg", "y_offset": -220},
    "nietzsche": {"file": "Philosophers Canvas/images/nietzsche.jpg", "y_offset": -180},
}

for node in data["nodes"]:
    if node["id"] in images:
        img_info = images[node["id"]]
        img_node = {
            "id": f"{node['id']}_img",
            "type": "file",
            "file": img_info["file"],
            "x": node["x"],
            "y": node["y"] + img_info["y_offset"],
            "width": 120,
            "height": 150
        }
        edge = {
            "id": f"e_{node['id']}_img",
            "fromNode": f"{node['id']}_img",
            "fromSide": "bottom",
            "toNode": node["id"],
            "toSide": "top"
        }
        data["nodes"].append(img_node)
        data["edges"].append(edge)

with open("World Philosophers Encyclopedia.canvas", "w") as f:
    json.dump(data, f, indent=2)

print(f"Added {len(images)} images")
