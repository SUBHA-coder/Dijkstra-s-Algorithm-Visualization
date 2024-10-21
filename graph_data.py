# graph_data.py

import networkx as nx

def create_sample_graph():
    G = nx.DiGraph()
    
    # Add nodes and weighted edges
    G.add_weighted_edges_from([
        (0, 1, 2), (1, 2, 4), (0, 2, 9),
        (1, 3, 1), (2, 3, 3), (2, 4, 8),
        (3, 4, 6), (4, 5, 1)
    ])
    
    return G
