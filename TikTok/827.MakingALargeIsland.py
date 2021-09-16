class Solution:
    def largestIsland(self, grid) -> int:
        n = len(grid)
        
        def moves(x, y):
            next_moves = []
            for d in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                next_x, next_y = x + d[0], y + d[1]
                if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
                    next_moves.append((next_x, next_y))
            return next_moves
        
        areas = {0:0}
        index = 2
        def dfs(x, y, index):
            res = 0
            grid[x][y] = index
            for next_x, next_y in moves(x, y):
                if grid[next_x][next_y] == 1:
                    res += dfs(next_x, next_y, index)
            return res + 1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[index] = dfs(i, j, index)
                    index += 1
        
        res = max(areas.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    connected = set([grid[x][y] for x, y in moves(i, j)])
                    res = max(res, sum(areas[idx] for idx in connected) + 1)
        return res