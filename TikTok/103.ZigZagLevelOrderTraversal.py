from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root: return []
        res = []
        level_list = deque()
        q = deque([root])
        is_left = True
        
        while q:
            size = len(q)
            
            for _ in range(size):
                node = q.popleft()
                if is_left:
                    level_list.append(node.val)
                else:
                    level_list.appendleft(node.val)
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                    
            res.append(level_list)
            level_list = deque()
            is_left = not is_left
        return res
            
        
        