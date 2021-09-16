import heapq
class Solution:
    def trapRainWater(self, heightMap) -> int:
        h = []
        m = len(heightMap)
        if m == 0: return 0
        n = len(heightMap[0])
        visited = set()
        res = 0
        
        for i in range(m):
            heapq.heappush(h, (heightMap[i][0], i, 0))
            heapq.heappush(h, (heightMap[i][n - 1], i, n - 1))
            visited.add((i, 0))
            visited.add((i, n - 1))
        for i in range(1, n - 1):
            heapq.heappush(h, (heightMap[0][i], 0, i))
            heapq.heappush(h, (heightMap[m - 1][i], m - 1, i))
            visited.add((0, i))
            visited.add((m - 1, i))
        res = 0
        while h:
            cur_height, x, y = heapq.heappop(h)
            
            for d in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                x0, y0 = x + d[0], y + d[1]
                if x0 >= 0 and x0 < m and y0 >= 0 and y0 < n and (x0, y0) not in visited:
                    # important, 在遍历到某一点后，这个点的高度在heap里的高度应该为 max（这个点最低围墙点高度， 这个点的高度)
                    heapq.heappush(h, (max(cur_height,heightMap[x0][y0]), x0, y0))
                    visited.add((x0, y0))
                    res += max(0, cur_height - heightMap[x0][y0])
        return res