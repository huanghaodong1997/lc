
def kruskal(graph):
    nodes = graph.keys()
    parent = {}
    def find_parent(node):
        if node != parent[node]:
            parent[node] = find_parent(parent[node])
        return parent[node]
    
    edges = []
    for node in nodes:
        parent[node] = node
        for adj, cost in graph[node]:
            edges.append((cost, node, adj))
    edges.sort(key=lambda x:x[0])
    mst = []
    mst_cost = 0
    for edge in edges:
        cost, src, dst = edge
        p1 = find_parent(src)
        p2 = find_parent(dst)
        if p1 != p2:
            mst_cost += cost
            mst.append(edge)
            parent[p1] = p2
    return mst, mst_cost


G = {
    "A": [["B", 2], ["C", 5]],
    "B": [["A", 2], ["D", 3], ["E", 1], ["F", 1]],
    "C": [["A", 5], ["F", 3]],
    "D": [["B", 3]],
    "E": [["B", 4], ["F", 3]],
    "F": [["C", 3], ["E", 3]],
}

mst, mst_cost = kruskal(G)
print(mst)
print(mst_cost)