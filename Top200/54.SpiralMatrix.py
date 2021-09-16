class Solution:
    
    def spiralOrder(self, matrix):
        
        m = len(matrix)
        n = len(matrix[0])
        # directions arrangement, right -> down -> left -> up
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        res = []
        # remember the visited index
        visited = set()
        cur_d = 1
        x = y = 0
        count = 0
        
        while count < m * n:
            res.append(matrix[x][y])
            visited.add((x, y))
            next_x, next_y = x + directions[cur_d][0], y + directions[cur_d][1]
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or (next_x, next_y) in visited:
                cur_d = (cur_d + 1) % len(directions)
                next_x, next_y = x + directions[cur_d][0], y + directions[cur_d][1]
            x, y = next_x, next_y
            count += 1
        return res