class Solution:
    def isValidSudoku(self, board) -> bool:
        n = len(board)
        rowUsed = [[False] * (n + 1) for _ in range(n)]
        colUsed = [[False] * (n + 1) for _ in range(n)]
        boxUsed = [[False] * (n + 1) for _ in range(n)]
        def couldPlace(num, x, y):
            boxRow = x // 3
            boxCol = y // 3
            if rowUsed[x][num] or colUsed[y][num] or boxUsed[boxRow * 3 + boxCol][num]:
                return False
            return True
        def place(num, x, y):
            boxRow = x // 3
            boxCol = y // 3
            rowUsed[x][num] = True
            colUsed[y][num] = True
            boxUsed[boxRow * 3 + boxCol][num] = True
            
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                if not couldPlace(num, i, j):
                    return False
                place(num, i, j)
        return True
            