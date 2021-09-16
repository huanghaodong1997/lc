# Cascading
#At each step one takes new integer into 
# consideration and generates new subsets from the existing ones.
class Solution1:
    def subsets(self, nums):
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
#backtracking
#For each element , add it to the list or not add it to the list
class Solution2:
    def subsets(self, nums):
        n = len(nums)
        ans = []
        def backtracking(depth, cur_list):
            if depth == n:
                tmp = [nums[i] for i in cur_list]
                ans.append(tmp)
                return
            backtracking(depth + 1, cur_list)
            cur_list.append(depth)
            backtracking(depth + 1, cur_list)
            cur_list.pop()
        backtracking(0, [])
        return ans