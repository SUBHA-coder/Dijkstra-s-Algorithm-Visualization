# visualize_3d.py

import plotly.graph_objects as go
import random
import networkx as nx
from dijkstra import dijkstra

def visualize_dijkstra_3d(G, start_node):
    distances = dijkstra(G, start_node)

    # Create edge coordinates
    edge_x = []
    edge_y = []
    edge_z = []
    for edge in G.edges():
        x0, y0, z0 = G.nodes[edge[0]]['pos']
        x1, y1, z1 = G.nodes[edge[1]]['pos']
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]
        edge_z += [z0, z1, None]

    edge_trace = go.Scatter3d(
        x=edge_x, y=edge_y, z=edge_z,
        line=dict(width=2, color='blue'),
        mode='lines')

    node_x = []
    node_y = []
    node_z = []
    node_text = []
    for node in G.nodes():
        x, y, z = G.nodes[node]['pos']
        node_x.append(x)
        node_y.append(y)
        node_z.append(z)
        node_text.append(f"Node {node}, Distance: {distances[node]}")

    node_trace = go.Scatter3d(
        x=node_x, y=node_y, z=node_z,
        mode='markers',
        marker=dict(size=10, color='red'),
        text=node_text)

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(title="Dijkstra's Algorithm in 3D"))
    
    fig.show()

if __name__ == "__main__":
    G = nx.DiGraph()

    # Add more complex edges with weights
    G.add_weighted_edges_from([
        (0, 1, 7), (0, 2, 9), (0, 5, 14),
        (1, 2, 10), (1, 3, 15),
        (2, 3, 11), (2, 5, 2),
        (3, 4, 6),
        (4, 5, 9)
    ])
    
    # Add random 3D positions to each node
    for node in G.nodes():
        G.nodes[node]['pos'] = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))

    visualize_dijkstra_3d(G, start_node=0)
