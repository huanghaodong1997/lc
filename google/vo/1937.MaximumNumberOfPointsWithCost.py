class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        
        dp = [num for num in points[0]]
        
        # dp[i][j] = max(dp[i-1][k] - abs(j-k) for k in range(0, n))
                
        # let's say j > k
        # dp[i][j] = max(dp[i-1][k]  - (j - k))
        # if j < k:
        # dp[i][j] = max(dp[i-1][k] - (k - j))
        for i in range(1, m):
            left_dp = [0] * n
            right_dp = [0] * n
            left_dp[0] = dp[0]
            right_dp[n - 1] = dp[n - 1] - n + 1
            for k in range(1, n):
                left_dp[k] = max(left_dp[k - 1], dp[k] + k)
            for k in range(n - 2, -1, -1):
                right_dp[k] = max(right_dp[k + 1], dp[k] - k)
                
            for j in range(0, n):
                dp[j] = max(left_dp[j] - j, right_dp[j] + j) + points[i][j]
        return max(dp)