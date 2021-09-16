from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        directions = [[-1, 0, 1], [-1, 1, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1], [1, -1, 1],[0, -1, 1], [-1, -1, 1]]
        if grid[0][0] == 1: return -1
        n = len(grid)
        q = deque([(0, 0, 1)])
        grid[0][0] = 1
        while q:
            x, y, step = q.popleft()
            if x == n - 1 and y == n - 1:
                return step
            for d in directions:
                x0, y0, next_step = x + d[0], y + d[1], step + d[2]
                if x0 >= 0 and x0 < n and y0 >= 0 and y0 < n and grid[x0][y0] == 0:
                    q.append((x0, y0, next_step))
                    grid[x0][y0] = 1
        return -1