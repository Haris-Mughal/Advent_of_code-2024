from collections import defaultdict, deque

def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")

    towel_patterns = lines[0].split(", ")
    designs = lines[2:]

    return towel_patterns, designs


def can_form_design(design, towel_patterns):
    queue = deque([design])
    seen = set()

    while queue:
        current = queue.popleft()

        if current == "":
            return True

        if current in seen:
            continue
        seen.add(current)

        for pattern in towel_patterns:
            if current.startswith(pattern):
                queue.append(current[len(pattern) :])

    return False


def count_possible_designs(file_path):
    towel_patterns, designs = read_input(file_path)
    possible_count = 0

    for design in designs:
        if can_form_design(design, towel_patterns):
            possible_count += 1

    return possible_count


file_path = "day_19.in"

result = count_possible_designs(file_path)
print(result)