# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    
    def constructFromPrePost(self, pre, post) -> TreeNode:
        N = len(pre)
        if N == 0: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root
        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root

            