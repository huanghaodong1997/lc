# Course Schedule I and II can use same approach here
from collections import defaultdict
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
            

        

