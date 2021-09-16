# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        
        def helper(root):
            if not root: return 0
            
            cur_sum = root.val
            left_sum = max(helper(root.left), 0)
            right_sum = max(helper(root.right), 0)
            self.ans = max(self.ans, cur_sum + left_sum + right_sum)
            return cur_sum + max(left_sum, right_sum)
        helper(root)
        return self.ans
            
        
        
        