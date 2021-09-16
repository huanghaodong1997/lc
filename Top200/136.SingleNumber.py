class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # a ^ a = 0
        # b ^ 0 = b

        # so a ^ a ^ b ^ c ^ c = b
        # The only one number remain.
        a = 0
        for i in nums:
            a ^= i
        return a