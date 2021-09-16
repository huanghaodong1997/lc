#encode the path using string
class Solution:
    def numDistinctIslands(self, grid) -> int:
        islands = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(x, y, path):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0: return ""
            grid[x][y] = 0
            return path + dfs(x, y + 1, 'R') + 'L' + dfs(x + 1, y, 'D') + 'U' + dfs(x, y - 1, 'L') + 'R' + dfs(x - 1, y, 'U') + 'D'
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islands.add(dfs(i,j,"s"))
        return len(islands)