class Solution:
    def findMin(self, nums) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        left, right = 0, n - 1
        if nums[right] > nums[0]: return nums[0]
        
        while left <= right:
            mid = left + (right - left) // 2
            # if the mid element is greater than its next element then mid+1 element is the smallest. Because mid will always less than the right boundary,
            # imageine nums = [3,4,5,1], will return 1 when mid = 5, so don't worry about
            # crossing the boundary
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1
        
