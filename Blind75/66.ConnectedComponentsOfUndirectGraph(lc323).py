from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges) -> int:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
            
        visited = set()
        def dfs(node):
            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    dfs(adj)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
            