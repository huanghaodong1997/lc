#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (23.95%)
# Likes:    2167
# Dislikes: 712
# Total Accepted:    262K
# Total Submissions: 914K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        border_set = set()
        m = len(board)
        if m == 0: return
        n = len(board[0])
        for i in range(m):
            border_set.add((i, 0))
            border_set.add((i, n - 1))
        for i in range(n):
            border_set.add((0, i))
            border_set.add((m - 1, i))
        
        visited = set()

        def bfs(i, j):
            nonlocal m, n
            can_flip = True
            q = deque([(i, j)])
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            res = []
            while q:
                x, y = q.popleft()
                if ((x, y)) in border_set: can_flip = False
                for d in directions:
                    x0, y0 = x + d[0], y + d[1]
                    if (x0, y0) not in visited and x0 >= 0 and x0 < m and y0 >= 0 and y0 < n and board[x0][y0] == 'O':
                        visited.add((x0, y0))
                        q.append((x0, y0))

                res.append((x, y))
            return res, can_flip
                
        def flip(to_flip):
            for x,y in to_flip:
                board[x][y] = 'X'


        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    visited.add((i, j))
                    to_flip, can_flip = bfs(i, j)
                    if can_flip:
                        flip(to_flip)


# @lc code=end

