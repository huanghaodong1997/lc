matrix = [
    ['1', '2', '3'],
     ['4', '5', '6'],
     ['x', '7', '8']
]

def getTargetKey(n) -> str:
    m = [str(i) for i in range(1, n * n)] +['x']
    return ",".join(m)

def getKey(matrix) -> str:
    key = ""
    for i in range(len(matrix)):
        key += ",".join(matrix[i])
        if i < len(matrix) - 1: key += ','
    return key

def findX(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'x':
                return (i, j)
# direction = 1 -> right; direction = -1 -> left
def moveHori(x, y, matrix, direction):
    tmp = matrix[x][y]
    cur_idx = (y + direction) % len(matrix) if y + direction >= 0 else (y + direction) + len(matrix)
    while cur_idx != y:
        matrix[x][cur_idx], tmp = tmp, matrix[x][cur_idx]
        cur_idx = (cur_idx + direction) % len(matrix) if cur_idx + direction >= 0 else (cur_idx + direction) + len(matrix)
    matrix[x][y] = tmp

def moveVerti(x, y, matrix, direction):
    tmp = matrix[x][y]
    cur_idx = (x + direction) % len(matrix) if x + direction >= 0 else (x + direction) + len(matrix)
    while cur_idx != x:
        matrix[cur_idx][y], tmp = tmp, matrix[cur_idx][y]
        cur_idx = (cur_idx + direction) % len(matrix) if cur_idx + direction >= 0 else (cur_idx + direction) + len(matrix)
    matrix[x][y] = tmp
#只允许四种操作: 把x这一行左右平移，或者这一列上下平移   

def moveMatrix(matrix):
    n = len(matrix)
    targetStr = getTargetKey(n)
    x, y = findX(matrix)
    ans = []
    visited = set()
    def backtracking(x, y, path):
        nonlocal ans
        key = getKey(matrix)
        if key == targetStr:
            if not ans or len(ans) > len(path):
                ans = path[:]
            return
        if key in visited: return 
        visited.add(key)
        path.append('l')
        moveHori(x, y, matrix, -1)
        next_y = n - 1 if  y - 1 < 0 else y - 1
        backtracking(x, next_y, path)
        moveHori(x, next_y, matrix, 1)
        path.pop()

        path.append('r')
        moveHori(x, y, matrix, 1)
        next_y = 0 if  y + 1 >= n else y + 1
        backtracking(x, next_y, path)
        moveHori(x, next_y, matrix, -1)
        path.pop()

        path.append('u')
        moveVerti(x, y, matrix, -1)
        next_x = n - 1 if  x - 1 < 0 else x - 1
        backtracking(next_x, y, path)
        moveVerti(next_x, y, matrix, 1)
        path.pop()

        path.append('d')
        moveHori(x, y, matrix, -1)
        next_x = 0 if  x + 1 >= n else x + 1
        backtracking(next_x, y, path)
        moveVerti(next_x, y, matrix, 1)
        path.pop()

    backtracking(x, y, [])
    return ans

print(moveMatrix(matrix))

        