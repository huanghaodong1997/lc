# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int: return 0
   def length(self) -> int: return 0

# Find Peak, then binary search each part
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        left, right = 0, n - 1
        peak = -1
        while left <= right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            mid_left = mountain_arr.get(mid - 1) if mid - 1 >= 0 else float('-inf')
            mid_right = mountain_arr.get(mid + 1) if mid + 1 < n else float('inf')
            if mid_val > mid_left and mid_val > mid_right:
                peak = mid
                break
            elif mid_val > mid_left and mid_val < mid_right:
                left = mid + 1
            else:
                right = mid - 1
        def binary_search(l_bound, r_bound, reverse):
            l, r = l_bound, r_bound
            while l <= r:
                mid = (l + r) // 2
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                elif mid_val < target:
                    if not reverse:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if not reverse:
                        r = mid - 1
                    else:
                        l = mid + 1
            return -1
        left_part, right_part = binary_search(0, peak, False), binary_search(peak, n - 1, True)
        if left_part == -1: return right_part
        return left_part
                