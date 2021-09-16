from collections import defaultdict
s = "(B,D) (D,E) (A,B) (C,F) (E,G) (A,C)"
#s = "(A,B) (A,C) (B,G) (C,H) (E,F) (B,D) (C,E)"
def find_roots(numNodes, graph):
    indegree = defaultdict(int)
    for node in graph:
        for adj in list(graph[node]):
            indegree[adj] += 1
    q = []
    root = None
    for node in graph:
        if indegree[node] == 0:
            q.append(node)
            root = node
    if len(q) == 0:
        return (0, None)
    if len(q) > 1:
        return (len(q), None)
    
    vis = set()
    vis.add(root)
    while q:
        node = q.pop(0)
        for adj in list(graph[node]):
            if adj in vis:
                return (0, None)
            vis.add(adj)
            q.append(adj)
    return (1, root) if numNodes == len(vis) else (0, None)

def helper(root, graph):
    l = r = ""
    children = list(graph[root])
    if len(children) == 1:
        l = helper(children[0], graph)
        return "(" + root + l + ")"
    if len(children) == 2:
        l = helper(children[0], graph)
        r = helper(children[1], graph)
        if children[0] <= children[1]:
            return "(" + root + l + r + ")"
        else:
            return "(" + root + r + l + ")"
    return "(" + root + ")"


def GetSExpression(s):
    E2 = False
    graph = defaultdict(set)
    i = 0
    nodes = set()
    while i != -1:
        src, dst = s[i + 1], s[i + 3]
        if dst in graph[src]:
            E2 = True
        nodes.add(src)
        nodes.add(dst)
        graph[src].add(dst)
        i = s.find('(', i + 1)
    for node in graph:
        if len(graph[node]) > 2:
            return "E1"
    if E2: return "E2"
    numRoots, root = find_roots(len(nodes), graph)
    if numRoots == 0: return "E3"
    if numRoots > 1: return "E4"
    if root == None: return "E5"
    return helper(root, graph)
    
print(GetSExpression(s))