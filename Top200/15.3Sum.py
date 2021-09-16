class Solution:
    def threeSum(self, nums):
        # sort the array
        # skip the duplicates element
        
        res = []
        nums.sort()
        
        def twoSum(nums, i, res):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if sum < 0:
                    lo += 1
                elif sum > 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    # important: remove dupliacates tuples
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
            
        
        for i in range(len(nums)):
            if nums[i] > 0: 
                # If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(nums, i, res)
        return res
    
    
# Set the low pointer lo to i + 1, and high pointer hi to the last index.
# While low pointer is smaller than high:
# If sum of nums[i] + nums[lo] + nums[hi] is less than zero, increment lo.
# If sum is greater than zero, decrement hi.
# Otherwise, we found a triplet:
# Add it to the result res.
# Decrement hi and increment lo.
# Increment lo while the next value is the same as before to avoid duplicates in the result.