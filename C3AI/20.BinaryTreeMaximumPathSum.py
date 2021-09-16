class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class GlobalVarSolution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0
        ans = float('-inf')
        def helper(root):
            if not root: return 0
            nonlocal ans
            left = helper(root.left)
            right = helper(root.right)
            cur_val = root.val
            take_left = left + cur_val
            take_right = right + cur_val
            
            ans = max(ans, cur_val, take_left, take_right, cur_val + left + right)
            return max(cur_val, take_left, take_right)
        helper(root)
        return ans
class NoGlobalVarSolution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0
        
        def helper(root):
            if not root: return float('-inf'), 0
            ans = float('-inf')
            l_ans, left = helper(root.left)
            r_ans, right = helper(root.right)
            cur_val = root.val
            take_left = left + cur_val
            take_right = right + cur_val
            
            cur_ans = max(cur_val, take_left, take_right, cur_val + left + right)
            ans = max(l_ans, r_ans, cur_ans)
            return ans, max(cur_val, take_left, take_right)
        ans, _ = helper(root)
        return ans