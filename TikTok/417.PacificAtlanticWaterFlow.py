from collections import deque
class Solution:
    def pacificAtlantic(self, matrix):
        pacific, atlantic = set(), set()
        
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        for i in range(m):
            pacific.add((i, 0))
            atlantic.add((i, n -1))
        for i in range(n):
            pacific.add((0, i))
            atlantic.add((m - 1, i))
        
        def bfs(ocean):
            used = set(ocean)
            q = deque([idx for idx in ocean])
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            while q:
                x, y = q.popleft()
                val = matrix[x][y]
                for d in directions:
                    x0, y0 = x + d[0], y + d[1]
                    if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or (x0, y0) in used or matrix[x0][y0] < val: continue
                    q.append((x0, y0))
                    ocean.add((x0, y0))
                    used.add((x0, y0))
        bfs(pacific)
        bfs(atlantic)
        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic: ans.append((i, j))
        return ans