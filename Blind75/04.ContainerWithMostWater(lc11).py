class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        max_left, max_right = height[0], height[-1]
        l,r = 0, len(height) - 1
        while l < r:
            # 当前左边 和 右边遇到过的最高木板
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])

            # 水的面积是 两边中短板的长度 X　x轴的长
            res = max(res, min(height[l], height[r]) * (r - l))

            if max_left >= max_right:
                r -= 1
            else:
                l += 1
        return res

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            #根据短板效应，如果移动长板的话最终面积一定会小于等于 移动短板
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area