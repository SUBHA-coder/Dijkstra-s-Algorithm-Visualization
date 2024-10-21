# visualize_2d.py

import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import dijkstra

def visualize_dijkstra_2d(G, start_node):
    # Get positions for each node for layout
    pos = nx.spring_layout(G)
    
    # Compute shortest path using Dijkstra's algorithm
    distances = dijkstra(G, start_node)

    # Plot the graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Highlight the explored nodes with colors
    explored_nodes = sorted(distances.keys(), key=lambda node: distances[node])
    for i, node in enumerate(explored_nodes):
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='r', node_size=700)
        plt.pause(0.5)  # Add delay to show step-by-step visualization

    plt.show()

if __name__ == "__main__":
    G = nx.DiGraph()

    # Add a more complex set of edges with weights
    G.add_weighted_edges_from([
        (0, 1, 7), (0, 2, 9), (0, 5, 14),
        (1, 2, 10), (1, 3, 15),
        (2, 3, 11), (2, 5, 2),
        (3, 4, 6),
        (4, 5, 9)
    ])
    
    visualize_dijkstra_2d(G, start_node=0)
