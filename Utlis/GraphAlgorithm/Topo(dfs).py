from collections import defaultdict
dependencies = {
    "A" : ["B", "C", "D", "E"],
    "B" : ["C", "D", "E", "X"],
    "Y" : ["A", "X"]  
}
packages = ["A", "B", "C", "D", "E", "X", "Y"]
# topo sort to get a order
# Then 
def buildPacakges(dependencies, packages):
    graph = defaultdict(list)
    for dst in dependencies:
        for src in dependencies[dst]:
            graph[src].append(dst)


    all_dependencies = {}
    for p in packages:
        all_dependencies[p] = set()
    visited = set()
    temp = set()
    def topo_sort(graph, node):
        if node in visited:
            return []
        if node in temp:
            # cycle
            return []
        
        order = []
        temp.add(node)
        
        for adj in graph[node]:
            if adj in temp:
                # cycle
                return []
            else:
                order += topo_sort(graph, adj)
        temp.remove(node)
        visited.add(node)
        order.append(node)
        return order
    topo_order= []
    for p in packages:
        if p not in visited:
            topo_order += topo_sort(graph, p)
    print(topo_order)
    if len(topo_order) != len(packages):
        # cycle 
        print("cycle")
        return None
    while topo_order:
        src = topo_order.pop()
        for dst in graph[src]:
            all_dependencies[dst] |= all_dependencies[src]
            all_dependencies[dst].add(src)
    print(all_dependencies)
buildPacakges(dependencies, packages)

