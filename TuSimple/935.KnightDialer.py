from functools import lru_cache
class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]
        
        @lru_cache(None)
        def dp(start, remain):
            if remain == 1:
                return 1
            res = 0
            for nei in moves[start]:
                res = (res + dp(nei, remain - 1)) % mod
            return res
        return sum(dp(i, n) for i in range(0, 10)) % mod