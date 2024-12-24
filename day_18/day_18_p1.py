import heapq

def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    corrupted_positions = [tuple(map(int, line.strip().split(','))) for line in lines]
    return corrupted_positions

def simulate_corruption(grid_size, corrupted_positions, num_bytes):
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for i in range(min(num_bytes, len(corrupted_positions))):
        x, y = corrupted_positions[i]
        grid[y][x] = 1
    return grid

def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid) and grid[y][x] == 0

def find_shortest_path(grid):
    
    start = (0, 0)
    goal = (len(grid) - 1, len(grid) - 1)

    
    pq = []
    heapq.heappush(pq, (0, start)) 

    distances = {start: 0}

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
                    priority = new_cost + abs(nx - goal[0]) + abs(ny - goal[1])
                    heapq.heappush(pq, (priority, (nx, ny)))

    return -1

def main():
    file_path = 'day_18.in'
    grid_size = 71
    num_bytes = 1024 

    corrupted_positions = parse_input(file_path)
    grid = simulate_corruption(grid_size, corrupted_positions, num_bytes)
    shortest_path_steps = find_shortest_path(grid)

    print(shortest_path_steps)

if __name__ == "__main__":
    main()