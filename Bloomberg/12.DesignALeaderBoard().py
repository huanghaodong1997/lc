from collections import defaultdict
import heapq
class Leaderboard:
    def __init__(self): self.L = defaultdict(int)
    def addScore(self, I, s): self.L[I] += s
    def top(self, K): 
        heap = []
        for x in self.L.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res
    def reset(self, I): del self.L[I]