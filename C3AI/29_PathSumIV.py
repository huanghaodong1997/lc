class Solution:
    # This is a compelete binary tree
    def pathSum(self, nums) -> int:
        ans = 0
        values = {x // 10 : x % 10 for x in nums}
        
        def dfs(node, running_sum = 0):
            nonlocal ans
            if not node in values: return
            running_sum += values[node]
            depth, pos = node // 10, node % 10
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1
            # leaf
            if left not in values and right not in values:
                ans += running_sum
            else:
                dfs(left, running_sum)
                dfs(right, running_sum)
        dfs(nums[0] // 10)
        return ans
# You can reconstruct the tree with similar logic
                