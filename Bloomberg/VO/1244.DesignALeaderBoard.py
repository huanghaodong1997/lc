import collections
import heapq
from random import randint
class Leaderboard:
    def __init__(self): self.L = collections.defaultdict(int)
        
    def addScore(self, I, s): self.L[I] += s
        
    def Naivetop(self, K): return sum(heapq.nlargest(K, self.L.values()))

    def Heaptop(self, K):
        values = self.L.values()
        h = []
        
        for val in values:
            heapq.heappush(h, val)
            
            if len(h) > K:
                heapq.heappop(h)
        return sum(h)

    def QuickSelect(self, K):
        values = list(self.L.values())
        
        def partion(i, j):
            # randomly pick a index as pivot
            k = randint(i, j)
            
            values[i], values[k] = values[k], values[i]
            oi = i
            pivot = values[i]
            i += 1
            
            
            while True:
                # U always make sure that the left part of points are less or EQUAL than u
                # Because U try to get K cloest points
                # So u should not try to keep too much equal to pivot elements in the left part
                # such as [1, 2, 3, 4, 4, 4, 4, 6] and k = 4. Your goal is to get the left most 4
                while i < j and values[i] > pivot:
                    i += 1
                
                while i <= j and values[j] <= pivot:
                    j -= 1
                if i >= j: break
                values[i], values[j] = values[j], values[i]
            # When u get out of this loop, the j will be the final pivot point
            # Just swap j with origin i 
            values[oi], values[j] = values[j], values[oi]
            return j
        l, r = 0, len(values) - 1
        
        while l <= r:
            mid = partion(l, r)
            if mid == K - 1:
                break
            elif mid < K - 1:
                l = mid + 1
            else:
                r = mid - 1
        return sum(values[:K])
    def reset(self, I): del self.L[I]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)


from sortedcontainers import SortedDict

class TreeMapLeaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:

        # The scores dictionary simply contains the mapping from the
        # playerId to their score. The sortedScores contain a BST with 
        # key as the score and value as the number of players that have
        # that score.     
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            preScore = self.scores[playerId]
            val = self.sortedScores.get(-preScore)
            if val == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = val - 1    
            
            newScore = preScore + score;
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1
        
    def top(self, K: int) -> int:
        count, total = 0, 0;

        for key, value in self.sortedScores.items():
            times = self.sortedScores.get(key)
            for _ in range(times): 
                total += -key;
                count += 1;
                
                # Found top-K scores, break.
                if count == K:
                    break;
                
            # Found top-K scores, break.
            if count == K:
                break;
        
        return total;

    def reset(self, playerId: int) -> None:
        preScore = self.scores[playerId]
        if self.sortedScores[-preScore] == 1:
            del self.sortedScores[-preScore]
        else:
            self.sortedScores[-preScore] -= 1
        del self.scores[playerId];