from functools import lru_cache
class RecursiveSolution:
    def minimumTotal(self, triangle) -> int:
        m = len(triangle)
        @lru_cache(None)
        def dp(i, j):
            if i == m - 1:
                return triangle[i][j]
            if j < 0 or j >= len(triangle[i]):
                return float('inf')
            
            return min(triangle[i][j] + dp(i + 1, j), triangle[i][j] + dp(i + 1, j + 1))
        return dp(0,0)
class DPSolution:
    def minimumTotal(self, triangle) -> int:
        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                dp[i] = row[i] + min(dp[i], dp[i + 1])
        return dp[0]
