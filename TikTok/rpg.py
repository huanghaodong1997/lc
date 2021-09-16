from functools import lru_cache
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)
# attack dmg; N: hp; K times
def rpg(M, N, K):

    @lru_cache(None)
    def dp(hp, times):
        if hp <= 0:
            return (M + 1) ** times
        if times <= 0:
            return 0
        res = 0
        for dmg in range(M + 1):
            res += dp(hp - dmg, times - 1)
        return res
    win = dp(N, K)
    total = ((M + 1) ** (K))
    ans = win / total
    return float("{:.5f}".format(ans))

# print(rpg(1, 2, 3))
# print(rpg(3, 1, 6))
print(rpg(5, 100, 2))
print(rpg(1000, 1000, 1000))