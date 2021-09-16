# Definition for a binary tree node.
from collections import defaultdict
# The key insight is that we only need to know the range of the column index 
# (i.e. [min_column, max_column]). Then we can simply iterate through this range to 
# generate the outputs without the need for sorting.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode):
        if not root: return []
        min_level = max_level = 0
        level_list = defaultdict(list)
        
        q = [(root, 0)]
        
        while q:
            node, level = q.pop(0)
            level_list[level].append(node.val)
            min_level = min(level, min_level)
            max_level = max(level, max_level)
            if node.left:
                q.append((node.left, level - 1))
            if node.right:
                q.append((node.right, level + 1))
        
        res = []
        for l in range(min_level, max_level + 1):
            res.append(level_list[l][:])
        return res