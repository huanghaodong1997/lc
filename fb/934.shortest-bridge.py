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
                if A[x0][y0] == 0: 
                    is_boarder = True
                    continue
                visited.add((x0,y0))
                q.append((x0, y0))
                
            if is_boarder: boarder.append((x,y))
        depth = 0
        res = 1
        found = False
        while boarder:
            size = len(boarder)
            if found: break
            for _ in range(size):
                x,y = boarder.popleft()
                # if A[x][y] == 1: 
                #     found = True
                #     break
                for d in directions:
                    x0, y0 = x + d[0], y + d[1]
                    if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or (x0,y0) in visited: continue
                    if not found and A[x0][y0] == 1:
                        found = True
                        res = depth
                    visited.add((x0,y0))
                    boarder.append((x0, y0))
            depth += 1
        return res
