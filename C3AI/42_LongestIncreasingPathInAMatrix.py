class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        
        memo = {}
        ans = 0
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            res = 1
            for d in [(-1,0), (0,1), (1,0), (0,-1)]:
                x, y = i + d[0], j + d[1]
                # We go into recursion only if the value is larger
                # So we will not end in endless recursion
                if x >= 0 and x < m and y >= 0 and y < n and matrix[x][y] > matrix[i][j]:
                    res = max(res, dp(x, y) + 1)
            memo[(i,j)] = res
            return res
        for i in range(m):
            for j in range(n):
                ans = max(ans, dp(i,j))
        return ans