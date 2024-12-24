from collections import deque

def simulate_falling_bytes(grid_size, corrupted_coords, max_bytes):
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    for x, y in corrupted_coords[:max_bytes]:
        grid[y][x] = "#"

    return grid


def find_shortest_path(grid):
    grid_size = len(grid)
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)

    
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < grid_size
                and 0 <= ny < grid_size
                and (nx, ny) not in visited
                and grid[ny][nx] == "."
            ):
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    return -1


def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    corrupted_coords = [tuple(map(int, line.strip().split(","))) for line in lines]
    return corrupted_coords


def find_blocking_byte(grid_size, corrupted_coords):
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    for i, (x, y) in enumerate(corrupted_coords):
        grid[y][x] = "#"
        if find_shortest_path(grid) == -1:
            return x, y

    return None


# Main execution
if __name__ == "__main__":
    input_file = "day_18.in"
    corrupted_coords = read_input(input_file)

    grid_size = 71  

    blocking_byte = find_blocking_byte(grid_size, corrupted_coords)

    if blocking_byte:
        print(f"{blocking_byte[0]},{blocking_byte[1]}")
    else:
        print("No blocking byte found")