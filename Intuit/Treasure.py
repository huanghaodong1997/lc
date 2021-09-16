grid = [
[1,1,1,1,1,1],
[0,0,1,0,1,1],
[0,0,0,0,0,0],
[1,1,1,0,1,0],
[1,0,0,0,1,1]]
def find_legal_moves1(grid, x, y):
    m = len(grid)
    n = len(grid[0])
    zeros = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                zeros += 1
    

    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 1:
            return 0
        grid[x][y] = 1
        res = 1

        for d in ((0,1),(1,0),(0,-1),(-1,0)):
            res += dfs(x + d[0], y + d[1])
        return res
    res = dfs(x,y)
    if res != zeros:
        return False
    else:
        return True

#print(find_legal_moves1(grid, 1, 0))

grid = [
    [  1,  0,  0, 0, 0 ],
    [  0, -1, -1, 0, 0 ],
    [  0, -1,  0, 1, 0 ],
    [ -1,  0,  0, 0, 0 ],
    [  0,  1, -1, 0, 0 ],
    [  0,  0,  0, 0, 0 ],
]

def find_shortest_route(grid, x, y, x1, y1):
    m = len(grid)
    n = len(grid[0])
    diamonds = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                diamonds += 1
    ans = None
    def dfs(x, y, path, remain):
        nonlocal ans
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1:
            return 
        if x == x1 and y == y1 and (remain == 0 or remain == 1 and grid[x][y] == 1):
            if not ans:
                ans = path[:] + [(x1,y1)]
            else:
                if len(path) < len(ans):
                    ans = path[:] + [(x1,y1)]
            return 
        tmp = grid[x][y]
        grid[x][y] = -1
        path.append((x, y))
        if tmp == 1:
            remain -= 1
        for d in ((0,1),(1,0),(0,-1),(-1,0)):
            dfs(x + d[0], y + d[1], path, remain)
        path.pop()
        grid[x][y] = tmp
        return 
    dfs(x, y, [], diamonds)
    print(ans)
find_shortest_route(grid, 0, 0, 4, 1)