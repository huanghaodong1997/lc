class Solution:
    def largestRectangleArea(self, heights) -> int:
        stk = [-1]
        ans = 0
        for i, height in enumerate(heights):
            
            while stk[-1] != -1 and heights[stk[-1]] >= height:
                # it is confirmed that elements between stk[-1] and i are valid for heights[stk.pop()]
                ans = max(ans, heights[stk.pop()] * (i - stk[-1] - 1))
            stk.append(i)
        while stk[-1] != -1:
            #every element in stk means that this number is valid from prev to the last element
            ans = max(ans, heights[stk.pop()] * (len(heights) - stk[-1] - 1))
        return ans