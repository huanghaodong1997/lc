class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        m, n= len(dungeon), len(dungeon[0])
        
        # dp[i][j]: the minimum healtha u need to walk to bottom right
        # starting from i, j. Every element is at least 1
        dp = [[float('inf')] * n for _ in range(m)]
        
        def get_min_health(curr_cell, i, j):
            if i >= m or j >= n:
                return float('inf')
            # You need to have at least dp[i][j] to go to (i, j)
            # because dungeon[i][j] + dp[i][j] >= 1
            # So the health you need in curr_cell will be
            # max(1, dp[i][j] - curr_cell\)

            # if curr_cell is less than zero, you will need dp[i][j] - curr_cell
            # to go to next (i, j), because dp[i][j] + dungeonp[i][j] >= 1
            return max(1, dp[i][j] - curr_cell)
        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1,- 1):
                currCell = dungeon[row][col]
                
                right_health = get_min_health(currCell, row, col + 1)
                down_health = get_min_health(currCell, row + 1, col)
                next_health = min(right_health, down_health)
                
                if next_health != float('inf'):
                    dp[row][col] = next_health
                else:
                    dp[row][col] = 1 if currCell >= 0 else 1 - currCell
        return dp[0][0]
