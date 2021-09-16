G = {
    "A": [["B", 2], ["C", 5]],
    "B": [["A", 2], ["D", 3], ["E", 1], ["F", 1]],
    "C": [["A", 5], ["F", 3]],
    "D": [["B", 3]],
    "E": [["B", 4], ["F", 3]],
    "F": [["C", 3], ["E", 3]],
}
def floyd_warshall(graph):
    n = len(graph)
    dis = [[float('inf')] * n for _ in range(n)]
    path = [['*'] * n for _ in range(n)]
    cur_id = 0
    v2Id = {}
    for node in graph:
        v2Id[node] = cur_id
        cur_id += 1
    for node in graph:
        node_id = v2Id[node]
        dis[node_id][node_id] = 0
        path[node_id][node_id] = node_id
        for adj, cost in graph[node]:
            adj_id = v2Id[adj]
            dis[node_id][adj_id] = cost
            path[node_id][adj_id] = adj_id

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dis[i][k] != float('inf') and dis[k][j] != float('inf') and dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
                    path[i][j] = path[i][k]
    return dis, path
def get_path(start, end, path):
    p = ""
    while start != end:
        p += (str(start) + ',')
        start = path[start][end]
    return p + str(end)
distances, path = floyd_warshall(G)
print(get_path(0,3, path))
print(get_path(1,2, path))