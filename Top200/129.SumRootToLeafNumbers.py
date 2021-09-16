# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MorrisSolution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        res = curr_number = 0
        
        while root:
            if root.left:
                predecessor = root.left
                step = 1
                while predecessor.right and predecessor.right != root:
                    step += 1
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = root
                    curr_number = curr_number * 10 + root.val
                    root = root.left
                    
                else:
                    predecessor.right = None
                    
                    if not predecessor.left:
                        res += curr_number
                        
                    for _ in range(step):
                        curr_number //= 10
                    root = root.right
                
            else:
                curr_number = curr_number * 10 + root.val
                if not root.right:
                    res += curr_number
                root = root.right
        return res


class RecursiveSolution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def helper(root, curr_sum):
            if not root:
                return 0
            if not root.left and not root.right:
                return curr_sum * 10 + root.val
            
            left_sum = helper(root.left, curr_sum * 10 + root.val)
            right_sum = helper(root.right, curr_sum * 10 + root.val)
            
            return left_sum + right_sum
        return helper(root, 0)

class IterativeSolution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        res = 0
        stk = [(root, 0)]
        
        while stk:
            node, curr_sum = stk.pop()
            if node:
                curr_sum = curr_sum * 10 + node.val
                if not node.left and not node.right:
                    res += curr_sum
                else:
                    stk.append((node.right, curr_sum))
                    stk.append((node.left, curr_sum))
        return res

