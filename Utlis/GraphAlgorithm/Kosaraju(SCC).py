from collections import defaultdict
test_graph_1 = {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: []}
test_graph_2 = {0: [1, 2, 3], 1: [2], 2: [0], 3: [4], 4: [5], 5: [3]}
test_graph_3 = {1:[2], 2:[3], 3:[1,5],4:[5],5:[6],6:[4],7:[6]}
def topology_sort(graph, vertex, visited):
    #suppose no cycle
    visited.add(vertex)
    order = []
    for adj in graph[vertex]:
        if adj not in visited:
            order += topology_sort(graph, adj, visited)
    order.append(vertex)
    # This order is reversed: Larger return time in the right of array
    return order

def find_components(reversed_graph, vertex, visited):
    components = [vertex]
    visited.add(vertex)
    for adj in reversed_graph[vertex]:
        if adj not in visited:
            components += find_components(reversed_graph, adj, visited)
    return components

def scc(graph):
    vis = set()
    order = []
    for node in graph:
        if node not in vis:
            order += topology_sort(graph, node, vis)
    
    
    reversed_graph = defaultdict(list)
    vis = set()
    
    for node in graph:
        for adj in graph[node]:
            reversed_graph[adj].append(node)
    all_components = []
    while order:
        node = order.pop()
        if node not in vis:
            all_components.append(find_components(reversed_graph, node, vis))
    return all_components


print(scc(test_graph_1))
print(scc(test_graph_2))
print(scc(test_graph_3))