import heapq

def parse_input(file_path):
    """Parse the input file to get the list of corrupted coordinates."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    corrupted_positions = [tuple(map(int, line.strip().split(','))) for line in lines]
    return corrupted_positions

def simulate_corruption(grid_size, corrupted_positions, num_bytes):
    """Simulate the corruption of the memory space for the first num_bytes bytes."""
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for i in range(min(num_bytes, len(corrupted_positions))):
        x, y = corrupted_positions[i]
        grid[y][x] = 1  # Mark the position as corrupted
    return grid

def is_valid(x, y, grid):
    """Check if a position is within bounds and not corrupted."""
    return 0 <= x < len(grid) and 0 <= y < len(grid) and grid[y][x] == 0

def find_shortest_path(grid):
    """Find the shortest path from top-left to bottom-right using A* algorithm."""
    start = (0, 0)
    goal = (len(grid) - 1, len(grid) - 1)

    # Priority queue for A* search
    pq = []
    heapq.heappush(pq, (0, start))  # (cost, position)

    # Distance dictionary
    distances = {start: 0}

    # Directions for moving in the grid
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        current_cost, current_pos = heapq.heappop(pq)
        if current_pos == goal:
            return current_cost

        x, y = current_pos
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid):
                new_cost = distances[current_pos] + 1
                if (nx, ny) not in distances or new_cost < distances[(nx, ny)]:
                    distances[(nx, ny)] = new_cost
                    priority = new_cost + abs(nx - goal[0]) + abs(ny - goal[1])  # Heuristic
                    heapq.heappush(pq, (priority, (nx, ny)))

    return -1  # No path found

def main():
    file_path = 'day_18.in'
    grid_size = 71  # Memory space grid size (0-70 inclusive)
    num_bytes = 1024  # First kilobyte

    corrupted_positions = parse_input(file_path)
    grid = simulate_corruption(grid_size, corrupted_positions, num_bytes)
    shortest_path_steps = find_shortest_path(grid)

    print(f"The minimum number of steps needed to reach the exit is: {shortest_path_steps}")

if __name__ == "__main__":
    main()