class Solution:
    def subsets(self, nums):
        n = len(nums)
        ans = []
        def backtracking(depth, cur_list):
            if depth == n:
                tmp = [nums[i] for i in cur_list]
                ans.append(tmp)
                return
            # not put current element
            backtracking(depth + 1, cur_list)
            cur_list.append(depth)
            # put current element
            backtracking(depth + 1, cur_list)
            cur_list.pop()
        backtracking(0, [])
        return ans