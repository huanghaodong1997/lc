from collections import defaultdict
import heapq
class Solution:
    def medianSlidingWindow(self, nums, k: int):
        if k == 1: return nums
        i = 0
        n = len(nums)
        ans = []
        l_heap, r_heap = [], []
        while i < k:
            heapq.heappush(r_heap, nums[i])
            i += 1
        while len(r_heap) > len(l_heap):
            heapq.heappush(l_heap, -heapq.heappop(r_heap))
        
        
        invalid = defaultdict(int)
        
        while i <= n:
            if k % 2 == 1:
                ans.append(-l_heap[0])
            else:
                ans.append((-l_heap[0] + r_heap[0]) / 2)
            if i == n: break
            inNum, outNum = nums[i], nums[i - k]
            maxLeft = -l_heap[0]
            invalid[outNum] += 1
            
            balance = -1 if outNum <= maxLeft else 1
            
            if inNum <= maxLeft:
                heapq.heappush(l_heap, -inNum)
                balance += 1
            else:
                heapq.heappush(r_heap, inNum)
                balance -= 1
            
            # left need more
            if balance < 0:
                heapq.heappush(l_heap, -heapq.heappop(r_heap))
            # right need more
            elif balance > 0:
                heapq.heappush(r_heap, -heapq.heappop(l_heap))
            while invalid[-l_heap[0]] >= 1:
                invalid[-l_heap[0]] -= 1
                heapq.heappop(l_heap)
            while invalid[r_heap[0]] >= 1:
                invalid[r_heap[0]] -= 1
                heapq.heappop(r_heap)
            i += 1
        return ans
            
            
        