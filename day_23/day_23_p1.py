from itertools import combinations

def parse_input(file_path):
    connections = []
    with open(file_path, 'r') as f:
        for line in f:
            connections.append(line.strip().split('-'))
    return connections

def build_graph(connections):
    graph = {}
    for a, b in connections:
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_triangles(graph):
    triangles = set()
    for node in graph:
        neighbors = list(graph[node])
        for a, b in combinations(neighbors, 2):
            if a in graph[b]:
                triangles.add(tuple(sorted([node, a, b])))
    return triangles

def filter_triangles(triangles):
    filtered = [triangle for triangle in triangles if any(computer.startswith('t') for computer in triangle)]
    return filtered

def main():
    connections = parse_input('day_23.in')
    graph = build_graph(connections)
    triangles = find_triangles(graph)
    filtered_triangles = filter_triangles(triangles)
    result = len(filtered_triangles)
    print(result)

if __name__ == "__main__":
    main()