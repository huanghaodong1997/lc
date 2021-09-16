from functools import lru_cache
class Solution:
    def canCross(self, stones) -> bool:
        
        stone2Idx = {}
        for i, stone in enumerate(stones):
            stone2Idx[stone] = i
            
        @lru_cache(None)
        def dp(i, k):
            if i == len(stones) - 1:
                return True
            ans = False
            for step in range(k - 1, k + 2):
                if step > 0 and step + stones[i] in stone2Idx:
                    ans |= dp(stone2Idx[step + stones[i]], step)
            return ans
        return dp(0, 0)

# bfs
# class Solution(object):
#     def canCross(self, stones):
#         seen = set()
#         stoneSet = set(stones)
#         end = stones[-1]
#         stack = [(0, 0)]
#         while len(stack) > 0:
#             loc, steps = stack.pop()
#             if (loc, steps) in seen:
#                 continue
#             seen.add((loc, steps))
#             if loc == end:
#                 return True
#             elif loc < end:
#                 for i in range(steps-1, steps+2):
#                     if i <= 0:
#                         continue
#                     if loc + i in stoneSet:
#                         stack.append((loc+i, i))
#         return False