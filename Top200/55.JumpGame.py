class Solution:
    def canJump(self, nums) -> bool:
        max_reach = len(nums) - 1
        target = len(nums) - 1
        # starting from back, 
        # if any index can reach max_reach
        # then change max_reach to current index i
        for i in range(target - 1, -1 ,-1):
            if nums[i] + i >= max_reach:
                max_reach = i
        # if max_reach == 0, it mean that we can reach the end
        return True if max_reach == 0 else False