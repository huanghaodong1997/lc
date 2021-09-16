class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        graph = [set(g) for g in graph]
        res = []
        def dfs(node, path):
            if node == n - 1:
                res.append(path[:])
                return
            for n_node in graph[node]:
                path.append(n_node)
                dfs(n_node, path)
                path.pop()
        dfs(0,[0])
        return res
                