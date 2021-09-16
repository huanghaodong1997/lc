class Solution:
    def candyCrush(self, board):
        m = len(board)
        n = len(board[0])
        
        todo = False
        
        for i in range(m):
            for j in range(n - 2):
                if abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]) != 0:
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
                    todo = True
        for i in range(m - 2):
            for j in range(n):
                if abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]) != 0:
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])
                    todo = True
        
        for j in range(n):
            wr = m - 1
            for i in range(m - 1, -1, -1):
                if board[i][j] > 0:
                    board[wr][j] = board[i][j]
                    wr -= 1
            for i in range(wr, -1, -1):
                board[i][j] = 0
        
        return board if not todo else self.candyCrush(board)