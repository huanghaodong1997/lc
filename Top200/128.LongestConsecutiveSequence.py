class Solution:
    #Because a sequence could start at any number in nums,
    #  we can exhaust the entire search space by building as long a 
    # sequence as possible from every numbers

    #we only attempt to build sequences from numbers that 
    # are not already part of a longer sequence. This is accomplished 
    # by first ensuring that the number that would immediately precede 
    # the current number in a sequence is not present, as that numberß
    #  would necessarily be part of a longer sequence.

    #We traverse each number at most 2 times
    def longestConsecutive(self, nums) -> int:
        num_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in num_set:
                cur_len = 0
                while num in num_set:
                    cur_len += 1
                    num += 1
                res = max(res, cur_len)
        return res