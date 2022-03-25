class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x0, y0 = location
        arr, extra = [], 0
        
        # turn points to radius
        
        for x, y in points:
            if x0 == x and y0 == y:
                extra += 1
                continue
            arr.append(math.atan2(y - y0, x - x0))
            
        # sort the array so we can use sliding window
        arr.sort()
        
        # double the arr because we aredoing round trip
        arr = arr + [x + 2.0 * math.pi for x in arr]
        
        # change angle to radius too
        angle = math.pi * angle / 180
        
        l = ans = r = 0
        
        while r < len(arr):
            # expand window, try to get maximum points
            while r < len(arr) and arr[r] - arr[l] <= angle:
                r += 1
            ans = max(ans, r - l)
            
            # shrink the window so keep it valid
            while r < len(arr) and l < r and arr[r] - arr[l] > angle:
                l += 1
            
        return ans + extra