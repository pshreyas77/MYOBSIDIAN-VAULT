import json

with open("World Philosophers Encyclopedia.canvas", "r") as f:
    data = json.load(f)

# Available images and their corresponding philosopher nodes
image_map = {
    "socrates": "Philosophers Canvas/images/socrates.jpg",
    "plato": "Philosophers Canvas/images/plato.jpg",
    "aristotle": "Philosophers Canvas/images/aristotle.jpg",
    "confucius": "Philosophers Canvas/images/confucius.jpg",
    "kant": "Philosophers Canvas/images/kant.jpg",
    "nietzsche": "Philosophers Canvas/images/nietzsche.jpg",
    "marx": "Philosophers Canvas/images/marx.jpg",
    "descartes": "Philosophers Canvas/images/descartes.webp",
}

# Find philosopher nodes and add images
nodes_added = 0
for node in list(data["nodes"]):
    nid = node.get("id")
    if nid in image_map:
        img_path = image_map[nid]
        # Calculate position above the node
        x = node.get("x", 0)
        y = node.get("y", 0) - 180
        width = 120
        height = 150
        
        # Check if image already exists for this node
        existing_img = [n for n in data["nodes"] if n.get("id") == f"{nid}_img"]
        if existing_img:
            print(f"Skipping {nid} - image already exists")
            continue
            
        img_node = {
            "id": f"{nid}_img",
            "type": "file",
            "file": img_path,
            "x": x,
            "y": y,
            "width": width,
            "height": height
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
        print(f"Added image for {nid}")

with open("World Philosophers Encyclopedia.canvas", "w") as f:
    json.dump(data, f)

print(f"\nTotal images added: {nodes_added}")
