
import heapq

def dijkstra(graph, start, target):
    # Initialize all distances as infinity and the start node distance as 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Store the previous node in the shortest path
    previous = {node: None for node in graph}

    # Use a priority queue to select the node with the smallest tentative distance
    unvisited = [(0, start)]

    while unvisited:
        current_distance, current_node = heapq.heappop(unvisited)

        # If the target is reached, build and return the path
        if current_node == target:
            path = []
            while current_node:
                path.insert(0, current_node)
                current_node = previous[current_node]
            return distances[target], path

        # Explore all neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance_through_current = current_distance + weight
            if distance_through_current < distances[neighbor]:
                distances[neighbor] = distance_through_current
                previous[neighbor] = current_node
                heapq.heappush(unvisited, (distance_through_current, neighbor))

    # If the target is not reachable
    return None

# The graph to be used for testing Dijkstra's algorithm
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 3},
    'D': {'B': 1, 'C': 4, 'E': 1, 'F': 2},
    'E': {'C': 3, 'D': 1, 'F': 1},
    'F': {'D': 2, 'E': 1, 'G': 3},
    'G': {'F': 3}
}

# Run test cases
print("Shortest path from A to F:", dijkstra(graph, 'A', 'F'))
print("Shortest path from B to G:", dijkstra(graph, 'B', 'G'))
