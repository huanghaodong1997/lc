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
        
        def preorder(node, cur_sum):
            nonlocal count
            if not node:
                return
            
            cur_sum += node.val
            
            if cur_sum == sum:
                count += 1
            count += mp[cur_sum - sum]
            
            mp[cur_sum] += 1
            preorder(node.left, cur_sum)
            preorder(node.right, cur_sum)
            mp[cur_sum] -= 1
        count = 0
        preorder(root, 0)
        return count
            
            
        
            