
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

#global variable 
class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.ans = 0
        def helper(root):
            if not root: return 0
            
            child_depth = []
            
            for child in root.children:
                child_depth.append(helper(child))
            
            
            
            if not child_depth:
                return 0
            child_depth.sort()
            max_child_depth = child_depth[-1] + 1
            if max_child_depth > self.ans:
                self.ans = max_child_depth
            if len(child_depth) >= 2:
                self.ans = max(self.ans, max_child_depth + child_depth[-2] + 1)
            return max_child_depth
        helper(root)
        return self.ans

#no global variable 