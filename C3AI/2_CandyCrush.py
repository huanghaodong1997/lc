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

# Simulation
#  We can flag candy that should be crushed first
# By mark it directly on the board by making the entry negative
#
# For each column we want all the candy to go to the bottom
# We can use a sliding window approach, maintaing a read 
# and write head. As the read head iterates through
# the column in reverse order, when the read head sees candy
# the write head will write it down and move one place
# if the read head doesn't meat candy, write head will not move upward
# which mean that write head will be in the bottom of read head,
# at last the gap between write head and read head must be filled with 0
