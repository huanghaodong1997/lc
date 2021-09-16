class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] *(n + 1) for _ in range(m + 1)]
        #dp[i][j] be the answer to the problem for the strings s1[i:], s2[j:]
        for i in range(m - 1, -1, -1):
            dp[i][n] = dp[i + 1][n] + ord(s1[i])
        for i in range(n - 1, -1, -1):
            dp[m][i] = dp[m][i + 1] + ord(s2[i])
        
        for i in range(m - 1, -1 , -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j] + ord(s1[i]), dp[i][j + 1] + ord(s2[j]))
        return dp[0][0]
#When s1[i] == s2[j], 
# we have dp[i][j] = dp[i+1][j+1] 
# as we can ignore these two characters.

#When s1[i] != s2[j],
#  we will have to delete at least one of them. 
# We'll have dp[i][j] as the minimum of the answers after both deletion options.