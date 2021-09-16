# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iterative inorder travesel
class BSTIterator:
    
    
    def __init__(self, root: TreeNode):
        self.stk = []
        self.leftmost_inorder(root)
    
    def leftmost_inorder(self, root):
        while root:
            self.stk.append(root)
            root = root.left
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        top_node = self.stk.pop()
        if top_node.right:
            self.leftmost_inorder(top_node.right)
        return top_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stk) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()