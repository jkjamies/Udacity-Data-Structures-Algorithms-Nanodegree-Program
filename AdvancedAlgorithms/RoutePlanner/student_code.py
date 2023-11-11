import math

def shortest_path(M, start, goal):
    open_set = set()
    closed_set = set()
    parent = {}

    g_score = {intersection: float('inf') for intersection in M.intersections}
    g_score[start] = 0

    # Calculate heuristic
    def heuristic(node):
        return math.sqrt((M.intersections[node][0] - M.intersections[goal][0]) ** 2 +
                         (M.intersections[node][1] - M.intersections[goal][1]) ** 2)

    open_set.add(start)

    while open_set:
        # Find the intersection
        current = min(open_set, key=lambda node: g_score[node] + heuristic(node))

        # If current intersection is goal, return reconstructed path
        if current == goal:
            path = []
            while current in parent:
                path.insert(0, current)
                current = parent[current]
            path.insert(0, start)
            return path

        # Remove current intersection from set
        open_set.remove(current)
        closed_set.add(current)

        # Explore neighbors
        for neighbor in M.roads[current]:
            if neighbor in closed_set:
                continue  # Skip if visited

            # Calculate tentative g-score
            tentative_g_score = g_score[current] + distance(M.intersections[current], M.intersections[neighbor])

            if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
                # This neighbor is better than previous one
                parent[neighbor] = current
                g_score[neighbor] = tentative_g_score

                if neighbor not in open_set:
                    open_set.add(neighbor)

    # If no path found, return empty list
    return []

def distance(coord1, coord2):
    # Calculate  distance between two coordinates
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)
