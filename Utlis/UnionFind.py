class UnionFind:
    def __init__(self, n):
        self.distinct_components = n
        self.component = [i for i in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]
        
    def find_component(self, a):
        if self.component[a] != a:
            self.component[a] = self.find_component(self.component[a])
        return self.component[a]
    
    def union(self, a, b):
        root_a = self.find_component(a)
        root_b = self.find_component(b)
        if root_a == root_b: return False

        # Set the root with more componets as the new root
        if self.rank[root_a] < self.rank[root_b]:
            self.component[root_a] = root_b
        else:
            if self.rank[root_a] == self.rank[root_b]:
                self.rank[root_a] += 1
            self.component[root_b] = root_a
        self.distinct_components -= 1
        return True
    
    def connected(self, a, b):
        return self.find_component(a) == self.find_component(b)
    
    def united(self):
        return self.distinct_components == 1