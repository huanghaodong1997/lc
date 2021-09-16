from collections import defaultdict
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
            # The current node has finished its exploration and 
            # appear in the final topo order, should return immediately
            # The parent node of this node should appear in the back of this node
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

            # once a node finished all its explore, marked it as visted
            visited.add(node)
            order.append(node)
            return order
        
        topo = []
        for node in range(N):
            if node not in visited:
                topo += helper(node)
        
        return topo if len(topo) == N else []
    
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        order = self.topo(numCourses, prerequisites)
        return True if order else False