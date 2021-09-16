class IterativeSolution:
    def numTrees(self, n: int) -> int:
        #G[n] the number of unique BST for a sequence of length n.
        # F(i,n) the number of unique BST, where the number i is served as the root of BST
        # G[n] = sum
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]

from functools import lru_cache 
class RecursiveSolution:
    def numTrees(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(i,j):
            if i >= j: return 1
            res = 0
            for k in range(i,j +1):
                res += dp(i,k - 1) * dp(k + 1, j)
            return res
        return dp(1, n)