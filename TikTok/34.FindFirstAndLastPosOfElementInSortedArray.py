# binary search boundary
class Solution:
    def searchRange(self, nums, target: int):
        
        def search_boundary(nums, target, search_left):
            lo, hi = 0, len(nums)
            
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > target or (search_left and target == nums[mid]):
                    # imporant!!! not mid + 1
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        left_idx = search_boundary(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        
        return [left_idx, search_boundary(nums, target, False) - 1]