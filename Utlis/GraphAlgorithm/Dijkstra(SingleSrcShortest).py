import heapq
# 有向图或无向图中， 所有边为正权重, 可以计算一个点到其他所有点的最小距离
def Dijkstra(graph, start, end):
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[start] = 0
    h = [(0, start)]
    visited = set()
    while h:
        cost, node = heapq.heappop(h)
        if node in visited: continue
        visited.add(node)
        for adj, c in graph[node]:
            if adj in visited:
                continue
            next_cost = cost + c
            distances[adj] = min(distances[adj], next_cost)
            heapq.heappush(h, (next_cost, adj))
    return -1 if distances[end] == float('inf') else distances[end]
G = {
    "A": [["B", 2], ["C", 5]],
    "B": [["A", 2], ["D", 3], ["E", 1], ["F", 1]],
    "C": [["A", 5], ["F", 3]],
    "D": [["B", 3]],
    "E": [["B", 4], ["F", 3]],
    "F": [["C", 3], ["E", 3]],
}

shortDistance = Dijkstra(G, "E", "C")
print(shortDistance)  # E -- 3 --> F -- 3 --> C == 6