class UnionFind:
    def __init__(self, n):
        self.distinct_components = 0
        self.component = [-1 for i in range(n)]
        self.rank = [0 for _ in range(n)]
        
    def isValid(self, i):
        return self.component[i] >= 0
    
    # intizatile a new root
    def setParent(self, i):
        self.component[i] = i
        self.distinct_components += 1
        
    def find_component(self, a):
        if self.component[a] != a:
            self.component[a] = self.find_component(self.component[a])
        return self.component[a]
    
    def union(self, a, b):
        root_a = self.find_component(a)
        root_b = self.find_component(b)
        if root_a == root_b: return False

        # Set the root with more componets as the new root
        if self.rank[root_a] > self.rank[root_b]:
            self.component[root_b] = root_a
        elif self.rank[root_a] < self.rank[root_b]:
            self.component[root_a] = root_b
        else:
            self.component[root_b] = root_a
            self.rank[root_a] += 1
        self.distinct_components -= 1
        return True
    
    def get_distinct_components(self):
        return self.distinct_components
    
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        ans = []
        
        uf = UnionFind(m * n)
        visited = set()
        for r, c in positions:
            overlap = []
            if (r, c) in visited:
                ans.append(ans[-1])
                continue
            
            for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0 <= nr < m and 0 <= nc < n and uf.isValid(nr*n+ nc): overlap.append(nr*n+nc)
            idx = r * n + c
            uf.setParent(idx)
            for i in overlap:
                uf.union(i, idx)
            ans.append(uf.get_distinct_components())
            visited.add((r,c))
        return ans