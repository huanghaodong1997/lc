class Solution:
    def trap(self, height) -> int:
        max_left = max_right = 0
        left, right = 0, len(height) - 1
        ans = 0
        
        #the water trapped depends upon the left_max, and similar is the case when \text{left\_max}[i]>\text{right\_max}[i]left_max[i]>right_max[i] (from element 8 to 11). So, we can say that if there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction (from left to right). As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left). We must maintain \text{left\_max}left_max and \text{right\_max}right_max during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.


        
        while left < right:
            if height[left] < height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    ans += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    ans += max_right - height[right]
                right -= 1
        return ans
class StackSolution:
    def trap(self, height) -> int:
        stk = []
        ans = 0
        
        i = 0
        
        while i < len(height):
            while stk and height[stk[-1]] < height[i]:
                top = stk.pop()
                
                if not stk:
                    break
                
                distance = i - stk[-1] - 1
                bounded_h = min(height[i], height[stk[-1]]) - height[top]
                ans += distance * bounded_h
                
            stk.append(i)
            i += 1
        return ans
            
# follow up: have zero inside, 0 会导致漏水

class FolloUpSolution:
    def trap(self, height) -> int:
        stk = []
        ans = 0
        
        i = 0
        
        while i < len(height):
            if height[i] == 0:
                stk = []
                i += 1
                continue
            while stk and height[stk[-1]] < height[i]:
                top = stk.pop()
                
                if not stk:
                    break
                
                distance = i - stk[-1] - 1
                bounded_h = min(height[i], height[stk[-1]]) - height[top]
                ans += distance * bounded_h
                
            stk.append(i)
            i += 1
        return ans
            