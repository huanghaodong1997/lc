class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        id2City = {}
        for i in range(n):
            id2City[i] = names[i]
        g = defaultdict(list)
        
        for src, dst in roads:
            g[src].append(dst)
            g[dst].append(src)
        
        m = len(targetPath)
        dp = [[m] * n for _ in range(m)]
        # Suppose prev[i][v] is u. Then (u, v) is the ending edge of the optimal path at dp[i][v].
        prev = [[0] * n for _ in range(m)]
        
        # dp[i][v] means the minimum edit distance for targetPath[:i+1] ending with city v
        # dp[i][v] = min(dp[i-1][u] + edit_cost(v)) for all edges (u, v)
        # edit_cost(v) = 1 if names[v] != targetPath[i]
        # bottom up dp
        for v in range(n):
            dp[0][v] = (names[v] != targetPath[0])
            
        for i in range(1, m):
            for v in range(n):
                for adj in g[v]:
                    if dp[i - 1][adj] < dp[i][v]:
                        dp[i][v] = dp[i - 1][adj]
                        # record the path
                        prev[i][v] = adj
                dp[i][v] += (names[v] != targetPath[i])
                
        path, min_dist = [0], m
        
        # select the point with minimal edit dist as start
        for v in range(n):
            if dp[-1][v] < min_dist:
                min_dist = dp[-1][v]
                path[0] = v
                
        for i in range(m - 1, 0, -1):
            u = prev[i][path[-1]]
            path.append(u)
        return path[::-1]