class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i + 1:]):
                    comp = -val1 - val2
                    # if comp shows up in seen, we know that val1, comp, val2 is a tuplet sums up to 0
                    # to prevent duplicate, we need to check whether comp is in seen during the current i loop or not
                    if comp in seen and seen[comp] == i:
                        res.add(tuple(sorted((val1, val2 , comp))))
                    seen[val2] = i
        return list(res)