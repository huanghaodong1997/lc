class Solution(object):
    def hitBricks(self, grid, hits):
        m, n = len(grid), len(grid[0])
        
        # Connect unconnected bricks, update value
        # Every time you hit dfs(i, j) on a valid cell
        # It means this cell is affected by some hit in hits
        def dfs(i, j):
            if not (0<=i<m and 0<=j<n) or grid[i][j] !=1:
                return 0
            
            ret = 1
            # Set to 2 to represent connected
            grid[i][j] = 2
            ret += sum(dfs(i+dx,j+dy) for dx,dy in((-1,0),(0,1),(1,0),(0,-1)) )
            return ret
        
        # Check (i,j) is connected to Not falling bricks
        # (1) Brick on top row
        def is_connected(i, j):
            return i==0 or any([0<=x<m and 0<=y<n and grid[x][y]==2 for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]])
        
        # Mark whether there is a brick at the each hit
        for i, j in hits:
            grid[i][j] -= 1
                
        # Get grid after all hits
        for i in range(n):
            dfs(0, i)
        
        # Reversely add the block of each hits and get count of newly add bricks
        ret = [0]*len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j]==1 and is_connected(i, j):
                ret[k] = dfs(i, j)-1
            
        return ret