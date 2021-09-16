grid = [
[1,1,1,1,1,1],
[0,0,1,0,1,1],
[0,0,1,0,1,0],
[1,1,1,0,1,0],
[1,0,0,1,1,1]]


def find_all_rectangles(grid):
    res = []
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                width = height = 1
                rec = [[i,j]]
                while j + width < n and grid[i][j+width] == 0:
                    width += 1
                while i + height < m and grid[i + height][j] == 0:
                    height += 1
                
                for h in range(height):
                    for w in range(width):
                        grid[i + h][j + w] = 1
                rec.append([i + height - 1, j + width - 1])
                res.append(rec)
    return res
#print(find_all_rectangles(grid))

def find_all_shapes(grid):
    result = []
    m = len(grid)
    n = len(grid[0])    
    def dfs(x, y, shape):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 1:
            return
        grid[x][y] = 1
        shape.append((x, y))

        for d in ((0,1),(1,0),(0,-1),(-1,0)):
            dfs(x + d[0], y + d[1], shape)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                shape = []
                dfs(i, j, shape)
                result.append(shape)
    return result
print(find_all_shapes(grid))
