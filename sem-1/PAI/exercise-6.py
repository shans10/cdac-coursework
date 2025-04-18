from collections import deque

def bfs_maze(maze, start, goal):
    """
    Perform BFS to find the shortest path in a maze from start to goal.

    :param maze: 2D list representing the maze (0 = open, 1 = wall)
    :param start: Tuple (row, col) representing the start position
    :param goal: Tuple (row, col) representing the goal position
    :return: List representing the path from start to goal or None if no path exists
    """
    # Directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Queue for BFS (FIFO)
    queue = deque([(start, [start])])  # (current position, path taken to reach that position)
    visited = set()  # Set to track visited positions

    while queue:
        current_pos, path = queue.popleft()  # Dequeue the first node in the queue

        # Goal test
        if current_pos == goal:
            return path  # Return the path if the goal is found

        visited.add(current_pos)  # Mark the position as visited

        # Generate neighbors (adjacent cells)
        for direction in directions:
            new_row, new_col = current_pos[0] + direction[0], current_pos[1] + direction[1]

            # Check if the new position is within bounds and not a wall
            if (0 <= new_row < len(maze)) and (0 <= new_col < len(maze[0])) and maze[new_row][new_col] == 0:
                new_pos = (new_row, new_col)
                if new_pos not in visited:
                    visited.add(new_pos)
                    queue.append((new_pos, path + [new_pos]))  # Enqueue the new position with updated path

    return None  # Return None if no path is found


# Example usage
maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Starting position (row, col)
goal = (4, 4)  # Goal position (row, col)

path = bfs_maze(maze, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found")
