class Connection:
    def __init__(self, city1, city2, cost):
        self.city1 = city1
        self.city2 = city2
        self.cost = cost

class UnionFind:
    def __init__(self, parents):
        self.parents = parents
    # get parent
    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    def union(self, city1, city2):
        p1, p2 = self.find(city1), self.find(city2)
        if p1 != p2:
            self.parents[p1] = p2
            return True
        return False
connections = [Connection("B","C",2), Connection("B","A",3), Connection("A", "C", 1)]
def Kruskal(connections):
    parents = {}
    for c in connections:
        parents[c.city1] = c.city1
        parents[c.city2] = c.city2
    uf = UnionFind(parents)
    connections.sort(key=lambda x: (x.cost, x.city1, x.city2))
    mst = []
    for c in connections:
        city1, city2 = c.city1, c.city2
        p1 = uf.find(city1)
        p2 = uf.find(city2)
        if p1 != p2:
            mst.append((c.city1, c.city2, c.cost))
            uf.union(c.city1, c.city2)
    return mst
print(Kruskal(connections))

