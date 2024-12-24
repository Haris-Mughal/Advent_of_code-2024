def parse_input(file_path):
    with open(file_path, 'r') as file:
        grid = []
        commands = None
        
        for line in file:
            line = line.strip()
            if line.startswith('<') or line.startswith('^') or line.startswith('>') or line.startswith('v'):
                commands = line
            else:
                grid.append(list(line))
                
    return grid, commands

def move_in_grid(grid, commands, start_pos):
    direction_map = {
        '<': (0, -1),
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0) 
    }
    
    x, y = start_pos
    boxes = set() 
    
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'O':
                boxes.add((i, j))
    
    for command in commands:
        dx, dy = direction_map.get(command, (0, 0))
        new_x, new_y = x + dx, y + dy
        
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != '#':
            
            if (new_x, new_y) in boxes:
                
                box_x, box_y = new_x + dx, new_y + dy
                if 0 <= box_x < len(grid) and 0 <= box_y < len(grid[0]) and grid[box_x][box_y] != '#':
                    
                    boxes.remove((new_x, new_y))
                    boxes.add((box_x, box_y))
                    
                    x, y = new_x, new_y
            else:
                x, y = new_x, new_y
    
    return boxes

def find_start_position(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '@':
                return i, j
    return None

def calculate_gps_sum(boxes):
    return sum(x + y for x, y in boxes)

def main():
    file_path = 'day_15.in'
    grid, commands = parse_input(file_path)
    
    start_pos = find_start_position(grid)
    
    if start_pos:
        final_boxes = move_in_grid(grid, commands, start_pos)
        gps_sum = calculate_gps_sum(final_boxes)
        print(gps_sum)
    else:
        print("Starting position not found!")

if __name__ == "__main__":
    main()
