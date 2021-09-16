matrix = [
    [0,0,0,0,1,1],
    [0,0,0,0,1,1],
    [0,0,0,0,1,1],
    [0,0,0,0,0,1],
]

rectangles = [
    [4,2],
    [3,2],
    [3,1]
    
]


class Solution:
    def putRectangleInMatrix(self, matrix, upp_left, bot_right):
        m = len(matrix)
        n = len(matrix[0])
        x, y = upp_left
        x0, y0 = bot_right
        for i in range(x, x0 + 1):
            for j in range(y, y0 + 1):
                if i >= m or j >= n or matrix[i][j] == 1: return False
        for i in range(x, x0 + 1):
            for j in range(y, y0 + 1):
                matrix[i][j] = 1
        return True

    def restoreMatrix(self, matrix, upp_left, bot_right):
        x, y = upp_left
        x0, y0 = bot_right
        for i in range(x, x0 + 1):
            for j in range(y, y0 + 1):
                matrix[i][j] == 0

    def canPutRectanglesInMatrix(self, matrix, rectangles):
        m = len(matrix)
        n = len(matrix[0])
        def dfs(depth):
            if depth == len(rectangles):
                return True
            width, height = rectangles[depth]
            res = False
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == 0:
                        if self.putRectangleInMatrix(matrix, (i, j), (i + width - 1, j + height - 1)):
                            res |= dfs(depth + 1)
                            self.restoreMatrix(matrix, (i, j), (i + width - 1, j + height - 1))
                        elif self.putRectangleInMatrix(matrix, (i, j), (i + height - 1, j + width - 1)):
                            res |= dfs(depth + 1)
                            self.restoreMatrix(matrix, (i, j), (i + height - 1, j + width - 1))
            return res
        return dfs(0)

sol = Solution()
print(sol.canPutRectanglesInMatrix(matrix, rectangles))