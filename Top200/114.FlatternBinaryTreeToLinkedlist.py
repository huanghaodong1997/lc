class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class O1Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        curr = root
        #However, the postponing of rewiring of connections on the 
        # current node until the left subtree is done, is basically what 
        # recursion is. Recursion 
        # is all about postponing decisions until something else is completed.

        #For a current node, we will check if it has a left child or not. 
        # If it does, we will find the last node in the rightmost branch 
        # of the subtree rooted at this left child. Once we find this
        #  "rightmost" node, 
        # we will hook it up with the right child of the current node.
        # Node 1
        while curr:
            if curr.left: # Node2
                rightmost = curr.left # Node 2
                while rightmost.right:
                    rightmost = rightmost.right
                # rightmost Node 4
                rightmost.right = curr.right 
                curr.right = curr.left
                curr.left = None    
            curr = curr.right