class Solution:
    def exist(self, board, word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        
        def backtracking(x, y, cur_word):
            #At the beginning, first we check if we reach the bottom case 
            # of the recursion, where the word to be matched is empty,
            #  i.e. we have already found the match for each prefix of the word.
            if len(cur_word) == 1:
                return True
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            board[x][y] = '#'
            res = False
            for d in directions:
                x0, y0 = x + d[0], y + d[1]
                if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or board[x0][y0] != cur_word[1]:
                    continue
                res = backtracking(x0, y0, cur_word[1:])
                if res: break
            # revert
            board[x][y] = cur_word[0]
            return res
        ans = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtracking(i, j, word):
                    return True
        return False