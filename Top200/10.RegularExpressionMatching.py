class DPSolution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[m][n] = True
        # iterate from back
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = i < m and (p[j] == s[i] or p[j] == '.')
                if j + 1 < n and p[j + 1] == '*':
                    # don't match or match
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    # match or not
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]

from functools import lru_cache
class DFSSolution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        
        @lru_cache(None)
        def dp(i, j):
            if i == m and j == n:
                return True
            if j == n:
                return False
            
            repeatable = False
            if j + 1 < n and p[j + 1] == '*':
                repeatable = True
            # if i is end, then if j is * then it must match null char
            if i == m:
                if repeatable:
                    return dp(i, j + 2)
                else:
                    return False
            
            
            res = False
            
            if s[i] == p[j] or p[j] == '.':
                if repeatable:
                    # match current character
                    res |= dp(i + 1, j)
                    # don't match
                    res |= dp(i, j + 2)
                else:
                    res |= dp(i + 1, j + 1)
            else:
                if repeatable:
                    # don't match
                    res |= dp(i, j + 2)
            return res
        return dp(0, 0)