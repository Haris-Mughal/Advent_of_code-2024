from collections import defaultdict, deque

def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")

    
    towel_patterns = lines[0].split(", ")
    designs = lines[2:] 

    return towel_patterns, designs


def count_ways_to_form_design(design, towel_patterns):
    memo = {}

    def dfs(remaining):
        if remaining == "":
            return 1

        if remaining in memo:
            return memo[remaining]

        ways = 0
        for pattern in towel_patterns:
            if remaining.startswith(pattern):
                ways += dfs(remaining[len(pattern) :])

        memo[remaining] = ways
        return ways

    return dfs(design)


def total_ways_to_form_designs(file_path):
    towel_patterns, designs = read_input(file_path)
    total_ways = 0

    for design in designs:
        total_ways += count_ways_to_form_design(design, towel_patterns)

    return total_ways


file_path = "day_19.in"

result = total_ways_to_form_designs(file_path)
print(result)