from collections import deque
class Solution:
    def orangesRotting(self, grid) -> int:
        q = deque([])
        m = len(grid)
        n = len(grid[0])
        visited = set()
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        res = -1
        
        if fresh == 0: return 0
        
        while q:
            size = len(q)
            
            for _ in range(size):
                x, y = q.popleft()
                for d in directions:
                    x0, y0 = x + d[0], y + d[1]
                    if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or grid[x0][y0] == 0 or (x0, y0) in visited:
                        continue
                    visited.add((x0, y0))
                    q.append((x0, y0))
                    fresh -= 1
                
            res += 1
        return res if fresh == 0 else -1