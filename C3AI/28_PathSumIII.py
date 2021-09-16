# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        ans = 0
        def dfs(root, cur_sum):
            nonlocal ans
            if not root:
                return
            cur_sum += root.val
            ans += mp[cur_sum - sum]
            mp[cur_sum] += 1
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
            mp[cur_sum] -= 1
            cur_sum -= root.val
        dfs(root, 0)
        return ans