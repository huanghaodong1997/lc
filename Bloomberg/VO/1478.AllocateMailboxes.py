from functools import lru_cache
class Solution:
    def minDistance(self, houses, k: int) -> int:
        # the minimum must be in the middle of the host
        n = len(houses)
        houses = sorted(houses)
        costs = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                median = houses[(i + j) // 2]
                for t in range(i, j + 1):
                    costs[i][j] += abs(median - houses[t])
        
        # min sum of distances of putting k mail boxes among houses[i:]
        @lru_cache(None)
        def dp(i, k):
            if k == 0 and i == n:
                return 0
            if k == 0 or i == n:
                return float('inf')
            
            res = float('inf')
            
            for j in range(i, n):
                res = min(res, costs[i][j] + dp(j + 1, k - 1))
            return res
        return dp(0, k)
            