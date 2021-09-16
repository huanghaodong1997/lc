
class OptimalSolution:
    #Collect Coordinates in Sorted Order
    def minTotalDistance(self, grid) -> int:
        rows = []
        cols = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    cols.append(j)
        row = rows[len(rows) // 2]
        col = cols[len(cols) // 2]
        
        def helper(points, origin):
            dis = 0
            for p in points:
                dis += abs(p - origin)
            return dis
        
        return helper(rows, row) + helper(cols, col)

# Sort Solution, O(m * n * log(mn))
# However u can can collect both the row and column coordinates in sorted order.
# And the time complexity will boil down to O(m * n)

class Solution:
    def minTotalDistance(self, grid) -> int:
        rows = []
        cols = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        cols.sort()
        
        row = rows[len(rows) // 2]
        col = cols[len(cols) // 2]
        
        def helper(points, origin):
            dis = 0
            for p in points:
                dis += abs(p - origin)
            return dis
        
        return helper(rows, row) + helper(cols, col)