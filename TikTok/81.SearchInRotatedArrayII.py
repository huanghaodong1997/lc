class Solution:
    def search(self, nums, target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target or nums[left] == target or nums[right] == target: return True
            
            if nums[mid] == nums[right]: #unable to confirm which side is sorted
                right -= 1
            elif nums[mid] > nums[right]: # left side sorted
                if target < nums[mid] and target > nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right side sorted
                if target > nums[mid] and target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False