# First of all let's get rid of negative numbers 
# and zeros since there is no need of them.
#  One could get rid of all numbers larger than n as well, 
# since the first missing positive is for sure smaller 
# or equal to n + 1. 
# The case when the first missing positive 
# is equal to n + 1 will be treated separately.

class Solution:
    #index as hash key
    def firstMissingPositive(self, nums) -> int:
        # edge case 1: because we are going to use 1 to indicate out of bound values later
        if 1 not in nums:
            return 1
        n = len(nums)
        
        # edge case2: nums = [1]
        if n == 1: return 2
        
        # Get rid of number that is less than 0 or larger than n
        # Because no use
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # Set the index which equal current number to be negative
        for i in range(n):
            num = abs(nums[i])
            
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
        
        # The first index i that nums[i] > 0 mean that number i + 1 is missing
        for i in range(0, n):
            if nums[i] > 0:
                return i + 1
        # if i = 0 - n - 1 exist, mean number 1 - n exist, return n + 1
        return n + 1