# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 0
        
        cursor = root
        
        while cursor.left:
            cursor = cursor.left
            level += 1
        
        before_leaves = 2 ** level - 1
        
        
        
        # Check if the idx node exixts in leaves
        
        # enumerate potential nodes in the last level from 0 to 2^d - 12 
#d
 #−1. How to check if the node number idx exists? Let's use binary search again to reconstruct the sequence of moves from root to idx node. 
        def exists(idx, d, node):
        
            left, right = 0, 2 ** d - 1
            # at each level, think of leaves are divide into two parts
            # if idx <= pivot, mean the potentail leaf in left part, so go to left
            # else, the leaf may be in exist in right part go to right to check exixstence
            for _ in range(d):
                pivot = (right - left) // 2 + left
                if idx <= pivot:
                    node = node.left
                    # note that pivot will always fall on the left side of leaves
                    right = pivot
                else:
                    node = node.right
                    left = pivot + 1
            return node is not None
        
        left, right = 1, 2 ** level - 1
#         1.. It's a complete tree, and hence all nodes in the last level are as far left as possible. That means that instead of checking the existence of all 2^d2 
# d
#   possible leafs, one could use binary search and check \log(2^d) = dlog(2 
# d
#  )=d leafs only.
        while left <= right:
            pivot = left + (right - left) // 2
            if exists(pivot, level, root):
                left = pivot + 1
            else:
                right = pivot - 1
        
        return before_leaves + left
        
        