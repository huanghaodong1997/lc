# bucket
class Solution:
    def firstMissingPositive(self, nums) -> int:
        if 1 not in nums:
            return 1
        n = len(nums)
        if n == 1: return 2
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
                
        for i in range(n):
            num = abs(nums[i])
            
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
            
        for i in range(1, n):
            if nums[i] > 0:
                return i + 1
        return n + 1