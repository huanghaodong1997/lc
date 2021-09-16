class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # how many combination of char in s can form t ? 
        n, m = len(s), len(t)
        
        # dp(i, j) mean the number of subseq s[i:] contain of t[j:]
        #Two actions:(1) If s[i] == t[j], we can match the chars
        # (2) we don't match the chars no matter what
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][m] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
                dp[i][j] += dp[i + 1][j]
        return dp[0][0]
        
#         @lru_cache(None)
#         def dp(i, j):
#             if j == m:
#                 return 1
#             elif i == n:
#                 return 0
            
#             res = 0
#             # if match, we can match the s[i] and t[j]
#             if s[i] == t[j]:
#                 res += dp(i + 1, j + 1)
                
#             # we don't match the current s[i] and t[j]
#             res += dp(i + 1, j)
#             return res
#         ans = dp(0, 0)
        # return ans