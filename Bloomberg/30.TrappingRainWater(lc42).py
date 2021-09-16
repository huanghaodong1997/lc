class Solution:
    def trap(self, height) -> int:
        n = len(height)
        l, r = 0, n - 1
        while l < n and height[l] <= 0:
            l += 1
        while r >= 0 and height[r] <= 0:
            r -= 1
        if l == n or r < 0: return 0
        
        max_left = height[l]
        max_right = height[r]
        res = 0
        while l <= r:
            if max_left <= max_right:
                max_left = max(max_left, height[l])
                #若当前 height[l]为max_left, 不会更新答案(max_left - heihgt[l] = 0)， 因此不用再用一个if 来判断
                res += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right, height[r])
                res += max_right - height[r]
                r -= 1
        return res
        
                
        