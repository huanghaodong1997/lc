class Solution:
    def triangleNumber(self, nums) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n - 2):
            if nums[i] == 0: continue
            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += (k - j - 1)
        return res
                