from collections import defaultdict
class Solution:
    def minimumSemesters(self, N: int, edges):
        edges = set()
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for src, dst in edges:
            edges.add((src, dst))
            graph[src].append(dst)
            indegree[dst] += 1
        q = []
        order = []
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                order.append(node)
                for adj in graph[node]:
                    indegree[adj] -= 1
                    edges.remove((node, adj))
                    if indegree[adj] == 0:
                        q.append(adj)
            level += 1
        # if edge remain, it has a cycle
        return order if not edges else []
        
            
        