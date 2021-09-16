# distinct value
class DistinctValueSolution:
    def search(self, nums, target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            # mid on left part
            #Pivot element is larger than the first element in the array
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
                
            # mid on right part
            #Pivot element is smaller than the first element of the array
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

class NotDistinceValueSolution:
    def search(self, nums, target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target or nums[left] == target or nums[right] == target: return True
            
            # difference logic with above
            if nums[mid] == nums[right]: #unable to confirm which side is sorted
                right -= 1

            # same logic as above
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