from collections import Counter
class Solution:
    def permuteUnique(self, nums):
        ans = []
        c = Counter(nums)
        def backtracking(cur_list = [], step = 0):
            if step == len(nums):
                ans.append(cur_list[:])
                return
            for num in c:
                if c[num] > 0:
                    c[num] -= 1
                    cur_list.append(num)
                    backtracking(cur_list, step + 1)
                    cur_list.pop()
                    c[num] += 1
        backtracking()
        return ans