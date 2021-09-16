from collections import deque
class DequeSolution:
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

class DPSolution:
    # dp approach
    # dividing window into len(nums) // k parts
    # left[i]: maximum value from start of current block to i
    # right[i]: maximum value from start of current block to i
    #      i ->   <-j 
    # [1,3,4,2], [2,5,6,7]  k = 4
    # for any window (i,j): max the max(right[i], left[j])
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        
        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(nums[i], left[i - 1])
        for i in range(n - 2, -1, -1):
            if (i + 1) % k == 0:
                right[i] = nums[i]
            else:
                right[i] = max(nums[i], right[i + 1])
        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))
        return output