from functools import lru_cache
class RecursiveSolution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def dp(i):
            if i == 0:
                return 1
            elif i < 0:
                return 0
            
            return dp(i - 1) + dp(i - 2)
        return dp(n)

class DPO1Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second