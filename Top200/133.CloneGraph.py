class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
# map + BFS
class IterativeSolution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        visited = {}
        q = deque()
        q.append(node)
        new_head = None
        while q:
            cur_node = q.popleft()
            clone_node = visited.get(cur_node.val, Node(cur_node.val, None))
            if clone_node.val not in visited: visited[cur_node.val] = clone_node
            for nei in cur_node.neighbors:
                if nei.val not in visited:
                    new_node = Node(nei.val, None)
                    clone_node.neighbors.append(new_node)
                    visited[nei.val] = new_node
                    q.append(nei)
                else:
                    clone_node.neighbors.append(visited[nei.val])
            if new_head == None: new_head = clone_node
        return new_head