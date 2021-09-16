class Solution:
    def search(self, nums, target: int) -> int:
        if not nums: return -1
        
        def search_rotate_idx():
            l, r = 0, len(nums) - 1
            if nums[l] <= nums[r]: return 0
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[l]:
                        r = mid - 1
                    else:
                        l = mid + 1
                        
        start = search_rotate_idx()
        l, r = 0, len(nums) - 1
        if target <= nums[r] and target >= nums[start]:
            l = start
        elif target >= nums[l] and target <= nums[start - 1]:
            r = start - 1
        else:
            return -1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
                