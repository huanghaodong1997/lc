class Solution:
# Start from bottom-left
#Then, until we find target and return true
#  (or the pointer points to a (row, col)(row,col) 
# that lies outside of the dimensions of the matrix),
#  we do the following: if the currently-pointed-to value
#  is larger than target we can move one row "up". 
# Otherwise, if the currently-pointed-to value is smaller 
# than target, we can move one column "right". It is not 
# too tricky to see why doing this will never prune the 
# correct answer; because the rows are sorted from 
# left-to-right, we know that every value to the right of 
# the current value is larger. Therefore, if the current 
# value is already larger than target, we know that every
#  value to its right will also be too large. 
# A very similar argument can be made for the columns, 
# so this manner of search will always find target 
# in the matrix (if it is present).
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        row, col = m - 1, 0
        
        while col < n and row >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
            
        return False

class DivdeAndConquerSolution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix: return False
        def searchRec(left, up, right, bottom):
            if left > right or up > bottom:
                return False
            if target < matrix[up][left] or target > matrix[bottom][right]:
                return False
            row = up
            mid = (left + right) // 2
            while row <= bottom and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            #pruning the search space upper left and bottom right matrix
            # because target is not possibile to exist in those two matrices
            return searchRec(left, row, mid - 1, bottom) or searchRec(mid + 1, up, right, row - 1)
        return searchRec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)
            