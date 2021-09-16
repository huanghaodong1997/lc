#  Binary search answer between lower bound and upper bound
class Solution:
    def splitArray(self, nums, m: int) -> int:
        # lower bound must be the maximum of nums
        l = max(nums)
        # upper bound is total sum of nums
        r = sum(nums)
        
        ans = r
        
        while l <= r:
            mid = (l + r) // 2
            cur_sum = 0
            
            cuts, curr_sum  = 0, 0
            for x in nums:
                curr_sum += x
                if curr_sum > mid:
                    cuts, curr_sum = cuts+1, x
            cnt = cuts + 1
                    
            if cnt <= m:
                ans = mid
                
                # mid too big, so few groups
                r = mid - 1
            else:
                l = mid + 1
        return ans

# Correct But TLE, can use binary search
# from functools import lru_cache
# class Solution:
#     def splitArray(self, nums, m: int) -> int:
#         n = len(nums)
#         prefix_sum = [0] * n
#         prefix_sum[0] = nums[0]
#         for i in range(1, n):
#             prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
#         @lru_cache(None)
#         def dp(idx, m):
#             if m == 1:
#                 return prefix_sum[n - 1] - prefix_sum[idx - 1] if idx > 0 else prefix_sum[n - 1]
            
#             res = float('inf')
#             for j in range(idx, n - m + 1):
#                 prev_sum = prefix_sum[idx - 1] if idx > 0 else 0
#                 curr_sum = prefix_sum[j] - prev_sum
#                 res = min(res, max(curr_sum, dp(j + 1, m - 1)))
#             return res
#         return dp(0, m)