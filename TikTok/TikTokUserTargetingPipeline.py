from collections import defaultdict
activity = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
engagement = [3,2,5,4,6,1,7,0]

def solution(activity, engagement):
    graph = defaultdict(list)
    for dst, src in activity:
        graph[src].append(dst)
    # no cycle
    # Get the min engagement result of every adjcent node
    visited = set()
    n_user = len(engagement)
    ans = [-1] * n_user
    def helper(node):
        visited.add(node)
        min_engage = engagement[node]
        res = node
        for adj in graph[node]:
            
            user = helper(adj) if ans[adj] == -1 else ans[adj]
    
            if engagement[user] < min_engage:
                res = user
                min_engage = engagement[user]
        ans[node] = res
        return res
    for node in range(n_user - 1, -1, -1):
        if node not in visited:
            helper(node)
    return ans

print(solution(activity, engagement))