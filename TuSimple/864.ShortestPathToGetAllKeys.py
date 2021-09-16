class Solution:
    def shortestPathAllKeys(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        numKeys = 0
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        x, y = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] in "abcdef":
                    numKeys += 1
                if grid[i][j] == '@':
                    x, y = i, j
        
        q = [(x, y, ".@abcdef", 0, 0)]
        
        while q:
            x, y, keys, step, collected = q.pop(0)
            if grid[x][y] in "abcdef" and grid[x][y].upper() not in keys:
                collected += 1
                keys += grid[x][y].upper()
            
            if collected == numKeys:
                return step
            
            for d in directions:
                x0, y0 = x + d[0], y + d[1]
                #grid[x0][y0] in keys means you have collected the key. For example 'B' in keys mean you have collected key 'b'
                if x0 >= 0 and x0 < m and y0 >= 0 and y0 < n and grid[x0][y0] in keys and (x0, y0, keys) not in visited:
                    visited.add((x0, y0, keys))
                    q.append((x0, y0, keys, step + 1, collected))
        return -1
            
            
            