class OnSolution:
    def longestConsecutive(self, nums) -> int:
        s = set(nums)
        res = 0
        for num in s:
            if num - 1 not in s:
                count = 0
                while num in s:
                    num += 1
                    count += 1
                res = max(count, res)
        return res

class ONlogNSolution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)