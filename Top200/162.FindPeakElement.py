class Solution:
    def findPeakElement(self, nums) -> int:
        #We can view any given sequence in numsnums array as alternating ascending and descending sequences. By making use of this, and the fact that we can return any peak as the result, we can make use of Binary Search to find the required peak element.
        l, r = 0, len(nums) - 1
        
        
        #We start off by finding the middle element, midmid from the given numsnums array. If this element happens to be lying in a descending sequence of numbers. or a local falling slope(found by comparing nums[i]nums[i] to its right neighbour), it means that the peak will always lie towards the left of this element. Thus, we reduce the search space to the left of midmid(including itself) and perform the same process on left subarray.
        while l < r:
            mid = (l + r) // 2
            
            # mid in a increaseing sequence of left part
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l