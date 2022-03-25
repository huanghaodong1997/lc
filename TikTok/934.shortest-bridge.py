#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#
# https://leetcode.com/problems/shortest-bridge/description/
#
# algorithms
# Medium (44.66%)
# Likes:    969
# Dislikes: 70
# Total Accepted:    35.9K
# Total Submissions: 73.4K
# Testcase Example:  '[[0,1],[1,0]]'
#
# In a given 2D binary array A, there are two islands.  (An island is a
# 4-directionally connected group of 1s not connected to any other 1s.)
# 
# Now, we may change 0s to 1s so as to connect the two islands together to form
# 1 island.
# 
# Return the smallest number of 0s that must be flipped.  (It is guaranteed
# that the answer is at least 1.)
# 
# 
# Example 1:
# Input: A = [[0,1],[1,0]]
# Output: 1
# Example 2:
# Input: A = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:
# Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 2 <= A.length == A[0].length <= 100
# A[i][j] == 0 or A[i][j] == 1
# 
# 
#

# @lc code=start
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        q = deque()
        boarder = deque()
        m = len(A)
        n = len(A[0])
        visited = set()
        for i in range(m):
            flag = False
            for j in range(n):
                if A[i][j] == 1:
                    q.append((i,j))
                    visited.add((i,j))
                    flag = True
                    break
            if flag: break
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        
        while q:
            x,y = q.popleft()
            is_boarder = False
            for d in directions:
                x0, y0 = x + d[0], y + d[1]
                if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or (x0,y0) in visited: continue
                visited.add((x0,y0))
                q.append((x0, y0))
                if A[x0][y0] == 0: is_boarder = True
            if is_boarder: boarder.append((x0,y0))
        depth = 0
        found = False
        while boarder:
            size = len(boarder)
            if found: break
            for _ in range(size):
                x,y = boarder.popleft()
                if A[x][y] == 1: 
                    found = True
                    break
                for d in directions:
                    x0, y0 = x + d[0], y + d[1]
                    if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or (x0,y0) in visited: continue
                    visited.add((x0,y0))
                    boarder.append((x0, y0))
            depth += 1
        return depth


        
# @lc code=end

