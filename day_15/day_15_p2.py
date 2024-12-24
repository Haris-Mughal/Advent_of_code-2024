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
    # Define movement directions for robot
    direction_map = {
        '<': (0, -1),  # Move left
        '^': (-1, 0),  # Move up
        '>': (0, 1),   # Move right
        'v': (1, 0)    # Move down
    }
    
    x, y = start_pos
    boxes = set()  # Track all box positions
    
    # Initialize box positions
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'O':
                boxes.add((i, j))  # Add box positions
    
    # Iterate through each movement command
    for command in commands:
        dx, dy = direction_map.get(command, (0, 0))
        new_x, new_y = x + dx, y + dy
        
        # Check if the robot can move (not hitting a wall)
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != '#':
            # Check if there is a box to push
            if (new_x, new_y) in boxes:
                # Try to move the box in the same direction
                box_x, box_y = new_x + dx, new_y + dy
                if 0 <= box_x < len(grid) and 0 <= box_y < len(grid[0]) and grid[box_x][box_y] != '#':
                    # Move the box
                    boxes.remove((new_x, new_y))  # Remove the box from its original position
                    boxes.add((box_x, box_y))    # Add the box to the new position
                    
                    # Move robot to the new position
                    x, y = new_x, new_y
            else:
                # Robot just moves to the new position without pushing a box
                x, y = new_x, new_y
    
    return boxes

def find_start_position(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '@':
                return i, j
    return None

def calculate_gps_sum(boxes):
    # Sum of x + y for each box
    return sum(x + y for x, y in boxes)

def main():
    file_path = 'day_15.in'
    grid, commands = parse_input(file_path)
    
    start_pos = find_start_position(grid)
    
    if start_pos:
        final_boxes = move_in_grid(grid, commands, start_pos)
        gps_sum = calculate_gps_sum(final_boxes)
        print(f"Sum of GPS coordinates of all boxes: {gps_sum}")
    else:
        print("Starting position not found!")

if __name__ == "__main__":
    main()
