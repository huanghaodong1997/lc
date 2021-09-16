class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]
        
        graphs = {}
        # link row to col, and link col to row
        for i in range(m):
            for j in range(n):
                v = matrix[i][j] # graphs[v]: the connection graph of value v
                if v not in graphs:
                    graphs[v] = {}
                if i not in graphs[v]:
                    graphs[v][i] = []
                if -j-1 not in graphs[v]:
                    graphs[v][-j-1] = []
                # link i to j, and link j to i
                graphs[v][i].append(-j-1)
                graphs[v][-(j+1)].append(i)
        # put points into `value2index` dict, grouped by connection
        values_to_idx = {} # {v: [[points1], [points2], ...], ...}
        seen = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in seen: continue
                v = matrix[i][j]
                seen.add((i, j))
                q = deque([(i, j)])
                points = [(i, j)]
                while q:
                    row, col = q.popleft()
                    for c in graphs[v][row]:
                        if (row, -c-1) not in seen:
                            seen.add((row, -c-1))
                            points.append((row, -c-1))
                            q.append((row, -c-1))
                    for r in graphs[v][-col-1]:
                        if (r, col) not in seen:
                            seen.add((r, col))
                            points.append((r, col))
                            q.append((r, col))
                if v not in values_to_idx: values_to_idx[v] = []
                values_to_idx[v].append(points)
        for v in sorted(values_to_idx.keys()):
            # update by connected points with same value
            for points in values_to_idx[v]:
                rank = 1
                for i, j in points:
                    rank = max(rank, max(rows[i], cols[j]) + 1)
                for i, j in points:
                    ans[i][j] = rank
                    rows[i] = max(rows[i], rank)
                    cols[j] = max(cols[j], rank)
        return ans
                            