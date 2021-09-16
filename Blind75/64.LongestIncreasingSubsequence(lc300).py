import bisect
class Solution:
# dp solution
    # dp[i] longest increasing seq ending with nums[i]
    # dp[i] -> max(dp[j]) + 1 for some j: j < i and nums[j] < nums[i]
    # time: O(n^2)
    # space: O(n)
    
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [1] * n
        
#         res = 1
        
#         for i in range(1, n):
#             for j in range(0, i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1) 
#             res = max(res, dp[i])
        
#         return res

# dp + binary_search
# 
# time: O(nlogn)
# space: O(n)
    def lengthOfLIS(self, nums) -> int:
        sub = [nums[0]]
        
        for i in range(1, len(nums)):
            idx = bisect.bisect_left(sub, nums[i])
            if idx == len(sub):
                sub.append(nums[i])
            else:
                sub[idx] = nums[i]
        return len(sub)
        
