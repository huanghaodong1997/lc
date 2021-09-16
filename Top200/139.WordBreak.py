from functools import lru_cache
class DFSMemoSolution:
    def wordBreak(self, s: str, wordDict) -> bool:
        
        @lru_cache(None)
        def dp(i):
            if i == len(s):
                return True
            res = False
            
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict:
                    res |= dp(j)
            return res
        return dp(0)
#The intuition behind this approach is that the given problem (ss) 
# can be divided into subproblems s1s1 and s2s2. If these subproblems 
# individually satisfy the required conditions,
#  the complete problem, ss also satisfies the same.

# dp[i] s[i:] can word break or not

# We can check the subproblem s1 by checking s1 is in wordDict or not
# Then we check subproblem s2 by calling the recursive funciton
class DPSolution:
    def wordBreak(self, s: str, wordDict) -> bool:
        
        n = len(s)
        dp = [False] * (n + 1)
        
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if s[i:j] in wordDict:
                    dp[i] |= dp[j]
        return dp[0]