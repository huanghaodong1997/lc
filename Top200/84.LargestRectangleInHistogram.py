class Solution:
    def largestRectangleArea(self, heights) -> int:
        stk = [-1]
        ans = 0
        for i, h in enumerate(heights):
            while stk[-1] != -1 and heights[stk[-1]] >= h:
                ans = max(ans, heights[stk.pop()] * (i - stk[-1] - 1))
            stk.append(i)
        while stk[-1] != -1:
            ans = max(ans, heights[stk.pop()] * (len(heights) - stk[-1] - 1) )
        return ans