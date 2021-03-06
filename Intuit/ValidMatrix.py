grid = [[1,3,1],
[2,1,3],
[3,2,1]]
def validMatrix(grid):
    n = len(grid)

    for i in range(n):

        rowSet = set()
        colSet = set()

        for j in range(n):
            if grid[i][j] < 1 or grid[i][j] > n:
                return False
            if grid[j][i] < 1 or grid[j][i] > n:
                return False
            
            if grid[i][j] in rowSet:
                return False

            if grid[j][i] in colSet:
                return False

            rowSet.add(grid[i][j])
            colSet.add(grid[j][i])
    return True
#print(validMatrix(grid))

"""
A nonogram is a logic puzzle, similar to a crossword, in which the player is given a blank grid and has to color it according to some instructions.
 Specifically, each cell can be either black or white, which we will represent as 0 for black and 1 for white.

+------------+
| 1  1  1  1 |
| 0  1  1  1 |
| 0  1  0  0 |
| 1  1  0  1 |
| 0  0  1  1 |
+------------+

For each row and column, the instructions give the lengths of contiguous runs of black (0) cells. For example, the instructions for one row of [ 2, 1 ] 
indicate that there must be a run of two black cells, followed later by another run of one black cell, and the rest of the row filled with white cells.

These are valid solutions: [ 1, 0, 0, 1, 0 ] and [ 0, 0, 1, 1, 0 ] and also [ 0, 0, 1, 0, 1 ]
This is not valid: [ 1, 0, 1, 0, 0 ] since the runs are not in the correct order.
This is not valid: [ 1, 0, 0, 0, 1 ] since the two runs of 0s are not separated by 1s.

Your job is to write a function to validate a possible solution against a set of instructions. Given a 2D matrix representing a player's solution; and instructions 
for each row along with additional instructions for each column; return True or False according to whether both sets of instructions match.

Example instructions #1

matrix1 = [[1,1,1,1],
           [0,1,1,1],
           [0,1,0,0],
           [1,1,0,1],
           [0,0,1,1]]
rows1_1    =  [], [1], [1,2], [1], [2]
columns1_1 =  [2,1], [1], [2], [1]
validateNonogram(matrix1, rows1_1, columns1_1) => True

Example solution matrix:
matrix1 ->
                                   row
                +------------+     instructions
                | 1  1  1  1 | <-- []
                | 0  1  1  1 | <-- [1]
                | 0  1  0  0 | <-- [1,2]
                | 1  1  0  1 | <-- [1]
                | 0  0  1  1 | <-- [2]
                +------------+
                  ^  ^  ^  ^
                  |  |  |  |
  column       [2,1] | [2] |
  instructions      [1]   [1]


Example instructions #2

(same matrix as above)
rows1_2    =  [], [], [1], [1], [1,1]
columns1_2 =  [2], [1], [2], [1]
validateNonogram(matrix1, rows1_2, columns1_2) => False

The second and third rows and the first column do not match their respective instructions.

Example instructions #3

matrix2 = [
[ 1, 1 ],
[ 0, 0 ],
[ 0, 0 ],
[ 1, 0 ]
]
rows2_1    = [], [2], [2], [1]
columns2_1 = [1, 1], [3]
validateNonogram(matrix2, rows2_1, columns2_1) => False

The black cells in the first column are not separated by white cells.

n: number of rows in the matrix
m: number of columns in the matrix
"""

matrix1 = [
    [1,1,1,1], # []
    [0,1,1,1], # [1] -> a single run of _1_ zero (i.e.: "0")
    [0,1,0,0], # [1, 2] -> first a run of _1_ zero, then a run of _2_ zeroes
    [1,1,0,1], # [1]
    [0,0,1,1], # [2]
]

# True
rows1_1 = [[],[1],[1,2],[1],[2]]
columns1_1 = [[2,1],[1],[2],[1]]
# False
rows1_2 = [[],[],[1],[1],[1,1]]
columns1_2 = [[2],[1],[2],[1]]

matrix2 = [
    [1,1],
    [0,0],
    [0,0],
    [1,0]
]
# False
rows2_1 = [[],[2],[2],[1]]
columns2_1 = [[1,1],[3]]
def nonogram(matrix, rows, columns):
    m = len(matrix)
    n = len(matrix[0])

    def checkRows():
        for i in range(m):
            stk = []
            zeros = 0
            for j in range(n):
                if matrix[i][j] == 1:
                    if zeros != 0:
                        stk.append(zeros)
                        zeros = 0
                else:
                    zeros += 1
            if zeros != 0:
                stk.append(zeros)
            if tuple(stk) != tuple(rows[i]):
                return False
        return True
    def checkCols():
        for i in range(n):
            stk = []
            zeros = 0
            for j in range(m):
                if matrix[j][i] == 1:
                    if zeros != 0:
                        stk.append(zeros)
                        zeros = 0
                else:
                    zeros += 1
            if zeros != 0:
                stk.append(zeros)
            if tuple(stk) != tuple(columns[i]):
                return False
        return True
    return checkRows() and checkCols()
print(nonogram(matrix1, rows1_1, columns1_1))
print(nonogram(matrix1, rows1_2, columns1_2))
print(nonogram(matrix2, rows2_1, columns2_1))