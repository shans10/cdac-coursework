import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state  # The state represents the node (e.g., a position in a maze)
        self.parent = parent  # The parent node
        self.g = g  # Cost from start to the current node
        self.h = h  # Heuristic from current node to goal
        self.f = g + h  # Total cost (g + h)

    def __lt__(self, other):
        # Comparison operator for the priority queue (heapq)
        return self.f < other.f

def a_star_search(start, goal, get_neighbors, heuristic):
    """
    A* Search Algorithm to find the shortest path from start to goal.
    :param start: The start node (state)
    :param goal: The goal node (state)
    :param get_neighbors: Function to get neighbors of a node
    :param heuristic: Heuristic function to estimate the cost to the goal
    :return: List of states representing the path from start to goal, or None if no path found
    """
    # Initialize open and closed lists
    open_list = []
    closed_list = set()

    # Push the start node into the open list
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)

        # If goal is reached, reconstruct the path
        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path (from start to goal)

        closed_list.add(current_node.state)

        # Get the neighbors of the current node
        for neighbor, cost in get_neighbors(current_node.state):
            if neighbor in closed_list:
                continue

            g = current_node.g + cost
            h = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, current_node, g, h)

            # Add the neighbor to the open list if it is not already there
            if all(neighbor_node.f < node.f for node in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None  # Return None if no path found

# Example heuristic function (Manhattan distance for grid-based pathfinding)
def heuristic(state, goal):
    x1, y1 = state
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

# Example function to get neighbors (4-directional movement for a grid)
def get_neighbors(state):
    neighbors = []
    x, y = state
    # Move up, down, left, right (grid-based example)
    for dx, dy, cost in [(-1, 0, 1), (1, 0, 1), (0, -1, 1), (0, 1, 1)]:
        neighbor = (x + dx, y + dy)
        neighbors.append((neighbor, cost))
    return neighbors

# Example usage
start = (0, 0)  # Starting position (x, y)
goal = (4, 4)  # Goal position (x, y)

path = a_star_search(start, goal, get_neighbors, heuristic)

if path:
    print("Path found:", path)
else:
    print("No path found")
