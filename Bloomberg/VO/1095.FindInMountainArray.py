# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int:
       return 0
   def length(self) -> int:
       return 0

class Solution:
    
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        
        # Get the peak element
        # try to minimize the time for calling get
        l, r = 0, n - 1
        while l < r:
            mid = (r - l) // 2 + l
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                # If u find the actual peak, u won't go into this if statement again
                l = peak = mid + 1
            else:
                # because mid is always on the left side of r
                # so u don't need to shrink it to mid - 1
                r = mid
                
        def binary_search(lo, hi, target, increasing):
            l, r = lo, hi
            while l <= r:
                mid = (r - l) // 2 + l
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                elif mid_val < target:
                    if increasing:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if increasing:
                        r = mid - 1
                    else:
                        l = mid + 1
            return -1
        left = binary_search(0, peak, target, True)
        if left != -1: return left
        
        return binary_search(peak, n - 1, target, False)
            