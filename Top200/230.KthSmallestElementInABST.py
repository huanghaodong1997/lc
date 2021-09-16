# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        stk = []
        
        while True:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        # Follow up
        #What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
        
        # We could keep a double linked list which is sorted in the
        # bottom of BST
        # Always keep the smallest node in double linked list
        
        # So the kth smallest time is O(k)
        # Insert, delete Time is O(H)