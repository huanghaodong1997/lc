matrix = [
    [0,0,0,0,1,1],
    [0,0,0,0,1,1],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
]

rectangles = [
    [2,1],
    [2,1],
    [4,3]
]


class Solution:
    def canPutRectangle(self, matrix, upp_left, bot_right) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        x, y = upp_left
        x1, y1 = bot_right
        for i in range(x, x1 + 1):
            for j in range(y, y1 + 1):
                if i < 0 or i >= m or j < 0 or j >= n: return False
                if matrix[i][j] == 1: return False
        for i in range(x, x1 + 1):
            for j in range(y, y1 + 1):
                matrix[i][j] = 1
        return True

    def restoreMatrix(self, matrix, upp_left, bot_right):
        x, y = upp_left
        x1, y1 = bot_right
        for i in range(x, x1 + 1):
            for j in range(y, y1 + 1):
                matrix[i][j] = 0
    
    def canPutRectanglesInMatrix(self, matrix, rectangles) -> bool:
        rectangles.sort()
        m = len(matrix)
        n = len(matrix[0])
        
        def dfs(depth):
            if depth == len(rectangles): return True

            res = False
            width, height = rectangles[depth]
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == 0:
                        if self.canPutRectangle(matrix, (i, j), (i + height - 1, j + width - 1)):
                            res |= dfs(depth + 1)
                            self.restoreMatrix(matrix, (i, j), (i + height - 1, j + width - 1))

                        if self.canPutRectangle(matrix, (i, j), (i + width - 1, j + height - 1)):
                            res |= dfs(depth + 1)
                            self.restoreMatrix(matrix, (i, j), (i + width - 1, j + height - 1))
            return res
                        

        ans = dfs(0)
        return ans




sol = Solution()
print(sol.canPutRectanglesInMatrix(matrix, rectangles))