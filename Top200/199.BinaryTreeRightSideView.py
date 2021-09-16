# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
# level order traversel, always pick the end of the queue
class Solution:
    def rightSideView(self, root: TreeNode):
        if root is None:
            return []
        queue = deque([root])
        res = []
        while queue:
            res.append(queue[-1].val)
            k = len(queue)
            for i in range(k):
                head = queue.popleft()
                if head.left is not None:
                    queue.append(head.left)
                if head.right is not None:
                    queue.append(head.right)
        return res
        