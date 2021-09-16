# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        if root == p or root == q: return root
        def helper(root, p, q):
            if not root: return 0
            
            cur = 1 if (root == p or root == q) else 0
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)
            
            if (cur + left + right) >= 2 and self.ans == None:
                self.ans = root
            return 1 if (cur + left + right) > 0 else 0
        helper(root, p, q)
        return self.ans
            