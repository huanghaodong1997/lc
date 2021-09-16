# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Use stack to perform inorder traversal
# You are traversomg the elements in an inorder order.
class IterativeSolution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        stk = []
        prev = None
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            # the current element must be strictly larger than previous one
            if prev and prev.val >= root.val: return False
            prev = root
            root = root.right
        return True
        
class RecursiveSolution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        
        # Set the boundary of the node when performing dfs
        # The validation of current node is postponed to the child nodes
        # by setting the boundary
        # let's say if the current node will pass an illeagal boundary
        # to child nodes, then it is the child node which 
        def helper(node, lower, upper):
            if not node: return True
            if lower and lower.val >= node.val: return False
            if upper and upper.val <= node.val: return False
            return helper(node.left, lower, node) and helper(node.right, node, upper)
        return helper(root, TreeNode(float('-inf')), TreeNode(float('inf')))