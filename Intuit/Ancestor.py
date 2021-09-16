parents = [[1,4], [1,5], [2,5], [3,6], [6,7],[8,1],[8,2], [9,2],[9,3],[10,9]]
from collections import defaultdict
#只有0个parents和只有1个parent的节点
def num_of_nodes(parents):
    graph = defaultdict(list)
    #indegree = defaultdict(int)
    nodes = set()
    for src, dst in parents:
        nodes.add(src)
        nodes.add(dst)
        graph[dst].append(src)
    res = []
    for node in nodes:
        if node not in graph or len(graph[node]) == 1:
            res.append(node)
    return res
#print(num_of_nodes(parents))
from collections import deque
def has_common_ancestor(parents, x, y):
    graph = defaultdict(list)
    #indegree = defaultdict(int)
    nodes = set()
    for src, dst in parents:
        nodes.add(src)
        nodes.add(dst)
        graph[dst].append(src)
    def bfs(node):
        res = set()
        q = deque([node])
        while q:
            node = q.popleft()
            res.add(node)
            for parent in graph[node]:
                q.append(parent)
        return res
    s1 = bfs(x)
    s2 = bfs(y)
    print(s1 & s2)
    if len(s1 & s2) != 0:
        return True
    return False
#print(has_common_ancestor(parents, 4, 5))

def furthest_common_ancestor(parents, x):
    graph = defaultdict(list)
    #indegree = defaultdict(int)
    nodes = set()
    for src, dst in parents:
        nodes.add(src)
        nodes.add(dst)
        graph[dst].append(src)
    def bfs(node):
        res = node
        q = deque([node])
        while q:
            node = q.popleft()
            res = node
            for parent in graph[node]:
                q.append(parent)
        return res
    ancestor = bfs(x)
    return ancestor
print(furthest_common_ancestor(parents, 5))

