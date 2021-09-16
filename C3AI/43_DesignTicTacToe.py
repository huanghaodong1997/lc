class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        # Don't need to actully store the board
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.antidiag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.rows[row] += 1 if player == 1 else -1
        self.cols[col] += 1 if player == 1 else -1
        
        # You only have one diagonal to win in this game
        if row + col == self.n - 1:
            self.antidiag += 1 if player == 1 else -1
        if row - col == 0:
            self.diag += 1 if player == 1 else -1
        if abs(self.rows[row])==self.n or abs(self.cols[col])==self.n \
            or abs(self.diag)==self.n or abs(self.antidiag)==self.n:
            return 1 if player==1 else 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)