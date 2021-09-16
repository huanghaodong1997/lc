class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# iteration
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        stk = []
        prev = None
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if prev and prev.val >= root.val: return False
            prev = root
            root = root.right
        return True

# recursion

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         if not root: return True
        
#         def helper(node, lower, upper):
#             if not node: return True
#             if lower and lower.val >= node.val: return False
#             if upper and upper.val <= node.val: return False
#             return helper(node.left, lower, node) and helper(node.right, node, upper)
#         return helper(root, TreeNode(float('-inf')), TreeNode(float('inf')))