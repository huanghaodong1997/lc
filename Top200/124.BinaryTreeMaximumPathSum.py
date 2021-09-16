# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0
        
        def helper(root):
            # at each step, to continue the current path or to start a new path 
            # with the current node as a highest node in this new path.
            if not root: return float('-inf'), 0
            ans = float('-inf')
            l_ans, left = helper(root.left)
            r_ans, right = helper(root.right)
            cur_val = root.val
            take_left = left + cur_val
            take_right = right + cur_val
            
            cur_ans = max(cur_val, take_left, take_right, cur_val + left + right)
            # update ans if it's better to start a new path
            ans = max(l_ans, r_ans, cur_ans)

            # for recursion :
            # return the max gain if continue the same path
            return ans, max(cur_val, take_left, take_right)
        ans, _ = helper(root)
        return ans
            
            
            