class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        res = []
        def dfs(node, path):
            if node == n - 1:
                res.append(path[:] + [node])
                return 
            path.append(node)
            for adj in graph[node]:
                dfs(adj, path)
            path.pop()
            
        dfs(0, [])
        return res