from collections import defaultdict
class SolutionKahn:
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
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                order.append(node)
                for adj in graph[node]:
                    indegree[adj] -= 1
                    edges_set.remove((node, adj))
                    if indegree[adj] == 0:
                        q.append(adj)
            level += 1
        # if edge remain, it has a cycle
        return order if not edges_set else []
    
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        order = self.topo(numCourses, prerequisites)
        return True if order else False
# Course Schedule I and II can use same approach here
class Solution:
    def topo_sort(self, N, graph):
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
        order = []
        for i in range(N):
            if i not in visited:
                order += helper(i)
        return order if len(order) == N else []
     
    def findOrder(self, numCourses: int, prerequisites):
        graph = defaultdict(list)
        
        # intialize graph
        for src, dst in prerequisites:
            graph[src].append(dst)
        return self.topo_sort(numCourses, graph)
            

        

