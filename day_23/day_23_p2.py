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

def is_clique(graph, nodes):
    for a, b in itertools.combinations(nodes, 2):
        if b not in graph[a]:
            return False
    return True

def find_cliques(graph, current_clique, potential_nodes, max_clique):
    if not potential_nodes:
        if len(current_clique) > len(max_clique[0]):
            max_clique[0] = current_clique[:]
        return

    for node in potential_nodes[:]:
        new_clique = current_clique + [node]
        new_potential_nodes = [n for n in potential_nodes if n in graph[node]]
        find_cliques(graph, new_clique, new_potential_nodes, max_clique)
        potential_nodes.remove(node)

def find_largest_clique(graph):
    max_clique = [[]]
    find_cliques(graph, [], list(graph.keys()), max_clique)
    return sorted(max_clique[0])

def main():
    connections = parse_input('day_23.in')
    graph = build_graph(connections)
    largest_clique = find_largest_clique(graph)
    password = ','.join(largest_clique)
    print(f'The password to the LAN party is: {password}')

if __name__ == "__main__":
    main()