# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stk = []
        
        def helper(node):
            while node:
                stk.append(node)
                node = node.left
                
        helper(root)
        prev = None
        while stk:
            node = stk.pop()
            if prev and prev.val >= node.val:
                return False
            if node.right:
                helper(node.right)
            prev = node
        return True
        