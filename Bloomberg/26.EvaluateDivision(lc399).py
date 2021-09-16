from collections import defaultdict
from collections import deque
class Solution:
    def calcEquation(self, equations, values, queries) :
        graph = defaultdict(list)
        for vertices, value in zip(equations, values):
            v1, v2 = vertices
            graph[v1].append((v2, value))
            graph[v2].append((v1, 1 / value))
        def find_path(src, dst):
            if src not in graph or dst not in graph: return -1
            q = deque([(src, 1.0)])
            visited = set()
            visited.add(src)
            while q:
                head, cur_res = q.popleft()
                if head == dst: return cur_res
                for adj, value in graph[head]:
                    if adj in visited: continue
                    q.append((adj, cur_res * value))
                    visited.add(adj)
            return -1.0
        result = []
        for src, dst in queries:
            result.append(find_path(src, dst))
        return result