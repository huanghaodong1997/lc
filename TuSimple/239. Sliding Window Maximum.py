from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        
        q = deque([])
        
        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
        res = []
        res.append(nums[q[0]])
        
        for i in range(k, len(nums)):
            while q and i - q[0] >= k:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res