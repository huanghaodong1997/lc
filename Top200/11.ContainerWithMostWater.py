class Solution:
    def maxArea(self, height) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

#the area formed between the lines will 
# always be limited by the height of 
# the shorter line. Further, the farther the lines, 
# the more will be the area obtained.

# So each iteration we just increase the pointer which has smaller height
# we can proof by contraction that, because the area is bounded by smaller height
# if we move the pointer that has larger value, then we could never find
# another area that is larger than the previous area