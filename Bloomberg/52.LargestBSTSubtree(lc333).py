# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        
        self.max_node = 0
        
        def helper(root): # return 1. is BST? 2.node num 3. max_val in BST 4. min_val in BST
            if not root:
                return True, 0, float('-inf'), float('inf')
            l, ln, lmax, lmin = helper(root.left)
            r, rn, rmax, rmin = helper(root.right)
            
            if l and r and root.val > lmax and root.val < rmin:
                if ln + rn + 1 > self.max_node:
                    self.max_node = ln + rn + 1
                return True, ln + rn + 1, max(root.val, lmax, rmax), min(root.val, lmin, rmin)
            return False, 0, None, None
        helper(root)
        return self.max_node
            