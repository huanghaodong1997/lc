class Solution:
    def longestConsecutive(self, nums) -> int:
        longest = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                curr = num
                seq = 0
                while curr in num_set:
                    seq += 1
                    curr += 1
                longest = max(longest, seq)
        return longest