# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class RecursiveSolution:
    def pathSum(self, root: TreeNode, sum: int):
        ans = []
        def helper(root, sum, cur_list):
            if not root:
                return 
            if not root.left and not root.right and sum - root.val == 0:
                ans.append(cur_list[:] + [root.val])
                return
            cur_list.append(root.val)
            helper(root.left, sum - root.val, cur_list)
            helper(root.right, sum - root.val, cur_list)
            cur_list.pop()
        helper(root, sum, [])
        return ans
class IterativeSolution:
    def pathSum(self, root: TreeNode, sum: int):
        if not root: return []
        stk = []
        num_stk = []
        ans = []
        cur_sum = 0
        curr = root
        prev = None
        while curr != None or stk:
            while curr != None:
                stk.append(curr)
                num_stk.append(curr.val)
                cur_sum += curr.val
                
                curr = curr.left
            curr = stk[-1]

            # This is important because u haven't explore right subtree yet, so go to right directly
            # if curr.right == prev: mean you have explore the right child
            if curr.right and curr.right != prev:
                curr = curr.right
                continue
            if not curr.left and not curr.right and cur_sum == sum:
                ans.append(num_stk[:])
            prev = curr
            stk.pop()
            num_stk.pop()
            cur_sum -= curr.val
            curr = None
            
        return ans