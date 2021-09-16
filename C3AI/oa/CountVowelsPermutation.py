class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        
        dp = [[0] * (5) for _ in range(n + 1)]
        for i in range(0,5):
            
            dp[1][i] = 1
        for i in range(1, n):
            dp[i + 1][0] = (dp[i][1] + dp[i][2] + dp[i][4]) % mod
            dp[i + 1][1] = (dp[i][0] + dp[i][2]) % mod
            dp[i + 1][2] = (dp[i][1] + dp[i][3]) % mod
            dp[i + 1][3] = dp[i][2]
            dp[i + 1][4] = (dp[i][2] + dp[i][3]) % mod
        res = 0
        for i in range(0,5):
            res = (res + dp[n][i]) % mod
        return res