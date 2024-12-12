from collections import deque, defaultdict

def parse_input(input_map):
    return [list(line) for line in input_map.strip().split("\n")]

def find_regions_and_calculate_costs(map_2d):

    rows, cols = len(map_2d), len(map_2d[0])
    visited = [[False] * cols for _ in range(rows)]
    total_price = 0

    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited[start_r][start_c] = True
        region_char = map_2d[start_r][start_c]
        area = 0
        perimeter = 0

        while queue:
            r, c = queue.popleft()
            area += 1
            # Check all four neighbors (up, down, left, right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if map_2d[nr][nc] == region_char and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                    elif map_2d[nr][nc] != region_char:
                        perimeter += 1
                else:
                    perimeter += 1

        return area, perimeter

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                area, perimeter = bfs(r, c)
                total_price += area * perimeter

    return total_price

garden_map = "day_12.in"

map_2d = parse_input(garden_map)
total_price = find_regions_and_calculate_costs(map_2d)
print(f"The total price of fencing all regions is: {total_price}")
