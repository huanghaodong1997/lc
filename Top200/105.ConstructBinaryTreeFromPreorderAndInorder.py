class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# the preorder traversal follows Root -> Left -> Right order,
#  that makes it very convenient to construct the tree from its root.

#he first element in the preorder list is a root. 
# This root splits inorder list into left and right subtrees. 
# Now one have to pop up the root from preorder list since 
# it's already used as a tree node and then repeat the step above 
# for the left and right subtrees.
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder: return None
        self.id = 0

        # value to id map
        inorderIdx = {}
        for i, val in enumerate(inorder):
            inorderIdx[val] = i
        def helper(lo,hi):
            if lo > hi: return None
            root_val = preorder[self.id]
            self.id += 1


            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            root_idx = inorderIdx[root_val]
            root.left = helper(lo, root_idx - 1)
            root.right = helper(root_idx + 1, hi)
            return root
        return helper(0, len(preorder) - 1)