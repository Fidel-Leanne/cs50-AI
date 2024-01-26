from queue import PriorityQueue

def gbfs(graph, start, goal, heuristic):
    visited = set()
    priority_queue = PriorityQueue()

    priority_queue.put((heuristic[start], start))  # Corrected this line

    while not priority_queue.empty():
        current_node = priority_queue.get()[1]

        if current_node == goal:
            return "Goal found!"

        if current_node not in visited:
            visited.add(current_node)

            # Expand neighbors and enqueue them based on heuristic
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    priority_queue.put((heuristic[neighbor], neighbor))  # Corrected this line

    return "Goal not reachable."

# Example usage (unchanged):
graph = {
    'A': {'B': 2, 'E': 4},
    'B': {'A': 2, 'C': 3, 'E': 1},
    'C': {'B': 3, 'D': 1},
    'D': {'C': 1},
    'E': {'A': 4, 'B': 1}
}

heuristic = {'A': 5, 'B': 3, 'C': 2, 'D': 1, 'E': 4}

start_node = 'A'
goal_node = 'D'

result_gbfs = gbfs(graph, start_node, goal_node, heuristic)
print(result_gbfs)
