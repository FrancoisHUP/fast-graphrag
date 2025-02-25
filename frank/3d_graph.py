import igraph as ig
import pickle
import gzip
import json
import random
import os

def load_graph(graph_file_path):
    """Load the compressed igraph from a pickle file."""
    with gzip.open(graph_file_path, "rb") as f:
        graph = pickle.load(f)
    return graph

def compute_3d_layout(graph):
    """
    Compute a 2D layout using Fruchterman-Reingold and extend it to 3D by assigning a random z-value.
    You could also implement or use a dedicated 3D layout if desired.
    """
    layout_2d = graph.layout("fruchterman_reingold")
    positions = []
    for point in layout_2d:
        # point is (x, y); we add a random z coordinate.
        x, y = point
        z = random.uniform(-50, 50)  # tweak range as needed
        positions.append((x, y, z))
    return positions

def export_graph_to_json(graph, positions, output_file):
    """
    Create a JSON structure with nodes (projects) and connections.
    Each node includes an id, title, position, and link.
    Each edge includes the source and target node ids.
    """
    nodes = []
    for i, vertex in enumerate(graph.vs):
        # Use an attribute "name" if available; otherwise, default to "Node X".
        node = {
            "id": i + 1,  # converting to 1-indexed id
            "title": vertex["name"] if "name" in vertex.attributes() else f"Node {i+1}",
            "position": positions[i],
            "link": vertex["link"] if "link" in vertex.attributes() else ""
        }
        nodes.append(node)
    
    edges = []
    for edge in graph.es:
        edges.append({
            "from": edge.source + 1,  # matching the 1-indexing above
            "to": edge.target + 1
        })
    
    graph_data = {
        "projects": nodes,
        "connections": edges
    }
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(graph_data, f, indent=2)
    print(f"Graph data exported to {output_file}")

def main():
    # Adjust the path to your graph file as needed.
    graph_file = "./frank/github/graph_igraph_data.pklz"
    output_file = "./frank/graph_3d.json"
    
    if not os.path.exists(graph_file):
        print(f"Graph file {graph_file} does not exist.")
        return

    graph = load_graph(graph_file)
    positions = compute_3d_layout(graph)
    export_graph_to_json(graph, positions, output_file)

if __name__ == "__main__":
    main()
