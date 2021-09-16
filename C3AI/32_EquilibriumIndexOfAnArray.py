# O(n) Time, O(n) Space
class Solution1:
    def pivotIndex(self, nums) -> int:
        n = len(nums)
        prefix = [0] * (n + 2)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        for i in range(1, n + 1):
            left = prefix[i - 1]
            right = prefix[n] - prefix[i]
            if left == right:
                return i - 1
        return -1

class SpaceSolution:
    def pivotIndex(self, nums) -> int:
        n = len(nums)
        all_sum = sum(nums)
        left_sum = 0
        for i in range(1, n + 1):
            left = left_sum
            right = all_sum - left_sum - nums[i - 1]
            if left == right:
                return i - 1
            left_sum += nums[i - 1]
        return -1
        