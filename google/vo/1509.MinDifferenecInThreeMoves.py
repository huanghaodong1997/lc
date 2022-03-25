class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = float('inf')
        i, j = 0, n - 4
        while j >= 0 and j < n:
            res = min(res, nums[j] - nums[i])
            j += 1
            i += 1
        return int(res) if res < float('inf') else 0