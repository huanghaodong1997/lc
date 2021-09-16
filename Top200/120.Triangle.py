class Solution:
    def minimumTotal(self, triangle) -> int:
        dp = [0] * (len(triangle) + 1)
        # dp: Minimum  effort to get to the current node i
        # because whenever you used a row, it is abandoned, so
        # we can just use a 1d array to the dp
        
        # bottom up dp
        for row in triangle[::-1]:
            for i in range(len(row)):
                dp[i] = row[i] + min(dp[i], dp[i + 1])
        return dp[0]