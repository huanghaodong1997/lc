from collections import defaultdict
test_graph_1 = {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: []}
test_graph_2 = {0: [1, 2, 3], 1: [2], 2: [0], 3: [4], 4: [5], 5: [3]}
test_graph_3 = {1:[2], 2:[3], 3:[1,5],4:[5],5:[6],6:[4],7:[6]}

def tarjan(graph) -> list:
    node2Id = {}
    lowlink = {}
    cur_id = 0
    stk = []
    stk_set = set()
    visited = set()
    ans = []
    def dfs(node):
        nonlocal cur_id
        visited.add(node)
        node2Id[node] = cur_id
        lowlink[node] = cur_id
        cur_id += 1
        stk.append(node)
        stk_set.add(node)
        for adj in graph[node]:
            if adj not in visited:
                dfs(adj)
            if adj in stk_set:
                lowlink[node] = min(lowlink[node], lowlink[adj])
        # current node is root of component
        if node2Id[node] == lowlink[node]:
            component = []
            while stk and lowlink[stk[-1]] == lowlink[node]:
                del_node = stk.pop()
                stk_set.remove(del_node)
                component.append(del_node)
            ans.append(component)
    for node in graph:
        if node not in visited:
            dfs(node)
    return ans

print(tarjan(test_graph_1))
print(tarjan(test_graph_2))
print(tarjan(test_graph_3))