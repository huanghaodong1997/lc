# reuse the Largest Rectangle problem! brilliant!
# Variation of larget rectangle problem lc 84
# Time: O(MN)
class StackSolution:
    def maximalRectangle(self, matrix) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        maxArea = 0
        
        def largetRectangle(heights):
            n = len(heights)
            res = 0
            stk = [-1]
            for i, height in enumerate(heights):
                while stk[-1] != -1 and heights[stk[-1]] >= height:
                    res = max(res, heights[stk.pop()] * (i - stk[-1] - 1))
                stk.append(i)
            while stk[-1] != -1:
                res = max(res, heights[stk.pop()] * (n - stk[-1] - 1))
            return res
        
        heights = [0] * n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1': heights[j] += 1
                else: heights[j] = 0
            maxArea = max(maxArea, largetRectangle(heights))
        return maxArea
                    
            




#Given a maximal rectangle with height h, 
# left bound l, and right bound r, there must be a
#  point on the interval [l, r] on the rectangle's base where the number 
# of consecutive ones
#  (height) above the point is <=h. If 
# this point exists, then the rectangle defined by the point in the above 
# manner will be the maximal rectangle, as it will reach height h iterating upward
#  and then expand to the bounds of [l, r] as all heights within those bounds must
#  accommodate h for the rectangle to exist.
# If this point does not exist, then the rectangle cannot be maximum, as you would be able to create a bigger rectangle by simply increasing the height of original rectangle, since all heights on the interval [l, r] would be greater than h.
class Solution:
    def maximalRectangle(self, matrix) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        maxArea = 0
        
        # height[i]  number of consecutive 1 in the current column i
        height = [0] * n
        
        # initialize left as the leftmost boundary possible
        # new_left[j] = max(old_left[j], cur_left)
        left = [0] * n
        
        # initialize right as the rightmost boundary possible
        # new_right[j] = min(old_right[j], cur_right)
        right = [n] * n
        #main idea: shirnk the left, right border if element is 0
        for i in range(m):
            cur_left, cur_right = 0, n
            #For the sake of simplicity, we don't decrement cur_right by one , so we can calculate the area
            
            for j in range(n):
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
                    
            
            for j in range(n):
                if matrix[i][j] == '1':
                    # if the old_left[j] == 0: it means that the previous row's element is 0
                    left[j] = max(cur_left, left[j])
                else:
                    
                    left[j] = 0
                    # the left boundary is shrink, the following element could not have smaller boundary than j + 1
                    cur_left = j + 1
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                maxArea = max(maxArea, height[j] * (right[j] - left[j]))

                    
        return maxArea