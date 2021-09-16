class Solution:
    def canJump(self, nums) -> bool:
        max_reach = len(nums) - 1
        target = len(nums) - 1
        for i in range(target - 1, -1 ,-1):
            if nums[i] + i >= max_reach:
                max_reach = i
        return True if max_reach == 0 else False
            