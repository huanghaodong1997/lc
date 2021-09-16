class Solution:
    def findPeakElement(self, nums) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # mid in a increaseing sequence of left part
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l