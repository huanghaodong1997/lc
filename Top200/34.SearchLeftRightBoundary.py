class Solution:
    def searchRange(self, nums, target: int):
        
        def search_boundary(nums, target, search_left):
            lo, hi = 0, len(nums)
            
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > target or (search_left and target == nums[mid]):
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        left_idx = search_boundary(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        
        return [left_idx, search_boundary(nums, target, False) - 1]

# First, because we are locating the 
# leftmost (or rightmost) index containing target
#  (rather than returning true iff we find target),
#  the algorithm does not terminate as soon as we find
#  a match. Instead, we continue to search until lo == hi 
# and they contain some index at which target can be found.

#The other change is the introduction of the left parameter, 
# which is a boolean indicating what to do in the event 
# that target == nums[mid]; if left is true, 
# then we "recurse" on the left subarray on ties.
#  Otherwise, we go right(go to the right boundary). 