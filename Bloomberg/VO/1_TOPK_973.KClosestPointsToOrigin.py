# O(NLOGN)
class SortSolution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
# O(NlogK)
import heapq
class HeapSolution:
    def kClosest(self, points, K):
        h = []
        
        for x, y in points:
            dis = x ** 2 + y ** 2
            heapq.heappush(h, (-dis, x, y))
            
            if len(h) > K:
                heapq.heappop(h)
        return [[x, y] for _, x, y in h]

# O(N) best, O(N ^ 2) worst, average O(NlogN)
from random import randint
class QuickSelectSolution:
    def kClosest(self, points, K):
        # quick select
        def dist(i):
            return points[i][0]**2 + points[i][1]**2

        def partion(i, j):
            # randomly pick a index as pivot
            k = randint(i, j)
            
            points[i], points[k] = points[k], points[i]
            oi = i
            pivot = dist(i)
            i += 1
            
            
            while True:
                # U always make sure that the left part of points are less or EQUAL than u
                # Because U try to get K cloest points
                # So u should not try to keep too much equal to pivot elements in the left part
                # such as [1, 2, 3, 4, 4, 4, 4, 6] and k = 4. Your goal is to get the left most 4
                while i < j and dist(i) < pivot:
                    i += 1
                
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]
            # When u get out of this loop, the j will be the final pivot point
            # Just swap j with origin i 
            points[oi], points[j] = points[j], points[oi]
            return j
        l, r = 0, len(points) - 1
        
        while l <= r:
            mid = partion(l, r)
            if mid == K - 1:
                break
            elif mid < K - 1:
                l = mid + 1
            else:
                r = mid - 1
        return points[:K]