from collections import deque
class Solution:

    def maxSlidingWindow(self, nums, k: int):
        window = deque([])
        
        def clear_window(window, idx, k):
            while window and idx - window[0] >= k:
                window.popleft()
            while window and nums[window[-1]] <= nums[idx]:
                window.pop()
        
        res = []
        for i in range(0, len(nums)):
            clear_window(window, i, k)
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res