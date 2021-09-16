# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder: return None
        self.id = 0
        inorderIdx = {}
        for i, val in enumerate(inorder):
            inorderIdx[val] = i
        def helper(lo,hi):
            if lo > hi: return None
            root_val = preorder[self.id]
            self.id += 1
            root = TreeNode(root_val)
            root_idx = inorderIdx[root_val]
            root.left = helper(lo, root_idx - 1)
            root.right = helper(root_idx + 1, hi)
            return root
        return helper(0, len(preorder) - 1)
        
        