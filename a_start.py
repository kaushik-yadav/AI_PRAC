import heapq  # For priority queue to get the node with lowest f cost

class Node:
    def __init__(self, x, y, g, h, parent=None):
        self.x = x  # Row position
        self.y = y  # Column position
        self.g = g  # Cost from start node
        self.h = h  # Estimated cost to goal
        self.f = g + h  # Total cost
        self.parent = parent  # Previous node (for path reconstruction)

    def __lt__(self, other):
        return self.f < other.f  # Compare nodes by f value in priority queue

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance heuristic

def a_star(grid, start, goal):
    open_list = []  # List of nodes to explore
    closed_list = set()  # Set of visited nodes

    # Create the start node with g=0 and calculated h
    start_node = Node(start[0], start[1], 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)  # Add start node to open list

    while open_list:
        current_node = heapq.heappop(open_list)  # Get node with lowest f value

        if (current_node.x, current_node.y) == goal:  # If goal is reached
            path = []
            while current_node:  # Reconstruct path by going through parents
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]  # Return reversed path (start to goal)

        closed_list.add((current_node.x, current_node.y))  # Mark node as visited

        # Explore 4 neighboring cells
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_x, neighbor_y = current_node.x + dx, current_node.y + dy

            # Skip if out of grid or is a wall (1)
            if not (0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0])) or grid[neighbor_x][neighbor_y] == 1:
                continue

            if (neighbor_x, neighbor_y) in closed_list:  # Skip already visited
                continue

            g = current_node.g + 1  # Move cost from start
            h = heuristic((neighbor_x, neighbor_y), goal)  # Heuristic to goal
            neighbor_node = Node(neighbor_x, neighbor_y, g, h, current_node)  # Create new node

            # Only add to open list if it's better than any existing one
            if all(neighbor_node.f < node.f for node in open_list if node.x == neighbor_x and node.y == neighbor_y):
                heapq.heappush(open_list, neighbor_node)  # Add neighbor to open list

    return None  # Return None if no path found

# Define grid with 0 as open and 1 as wall
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)  # Start position
goal = (2, 2)   # Goal position

path = a_star(grid, start, goal)  # Call A* function
print("Path:", path)  # Print the path from start to goal
