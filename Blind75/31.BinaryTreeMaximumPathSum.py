# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        def helper(root):
            if not root:
                return 0
            left, right = helper(root.left), helper(root.right)
            val = root.val
            self.ans = max(self.ans, val, val + left, val + right, val + left + right)
            return max(val, val + left, val + right)
        helper(root)
        return self.ans
            
            
            