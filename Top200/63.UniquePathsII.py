class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        dp = [[0] * n for _ in range(m)] # m * n array
        
        dp[0][0] = 1    # intialize
        
        for i in range(0, m):
            for j in range(0, n):
                # Fucking edge cases
                if i == 0 and j == 0: continue
                left = dp[i - 1][j] if i - 1 >= 0 else 0
                up = dp[i][j - 1] if j - 1 >= 0 else 0
                dp[i][j] = left + up if obstacleGrid[i][j] == 0 else 0
        return dp[m - 1][n - 1]