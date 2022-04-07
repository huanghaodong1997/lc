class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for i, num in enumerate(nums):
            if num - 1 not in num_set:
                cum, tmp = 0, num
                while tmp in num_set:
                    cum += 1
                    tmp += 1
                res = max(res, cum)
        return res