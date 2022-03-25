class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        
        def backtracking(x, y, idx):
            if idx == len(word) - 1:
                return True
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            board[x][y] = '#'
            res = False
            for d in directions:
                x0, y0 = x + d[0], y + d[1]
                if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or board[x0][y0] != word[idx + 1]:
                    continue
                res = backtracking(x0, y0, idx + 1)
                if res: break
            board[x][y] = word[idx]
            return res
        ans = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtracking(i, j, 0):
                    return True
        return False