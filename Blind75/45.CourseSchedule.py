# BFS topo
class Solution:
    def topo(self, N: int, edges):
        edges_set = set()
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for src, dst in edges:
            edges_set.add((src, dst))
            graph[src].append(dst)
            indegree[dst] += 1
        q = []
        order = []
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.pop(0)
            order.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                edges_set.remove((node, nei))
                if indegree[nei] == 0:
                    q.append(nei)
                    
        return order if not edges_set else []
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        order = self.topo(numCourses, prerequisites)
        return True if order else False
# DFS TOPO
class Solution:
    def topo(self, N: int, edges):
        graph = defaultdict(list)
        
        # intialize graph
        for src, dst in edges:
            graph[src].append(dst)
        visited = set()
        temp = set()
        
        # dfs topo
        def helper(node):
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
                    order += helper(adj)
            temp.remove(node)
            visited.add(node)
            order.append(node)
            return order
        
        topo = []
        for node in range(N):
            if node not in visited:
                topo += helper(node)
        
        return topo if len(topo) == N else []
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        order = self.topo(numCourses, prerequisites)
        return True if order else False