# dijkstra.py

import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue to store (distance, node)
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Process each neighbor of the current node
        for neighbor in graph[current_node]:
            # Get the weight of the edge (current_node -> neighbor)
            weight = graph[current_node][neighbor].get('weight', 1)
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances
