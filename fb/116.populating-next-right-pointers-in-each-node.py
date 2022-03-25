"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# O(n) space: Level order traversal

# The fact that we are doing a perfect binary tree
# So you can easily keep the leftmost node of next level

# O(1) space: Utilizing the fact that we can level traverse using next pointer
# The idea is to use a helper function toa process the node as well as
# return the next level leftmost node and next level prev node(the node needed to estabilish next pointer to next node which
# need to be process)
class Solution:
    
    
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        leftmost = root
        
        # still have level nodes that need to be processed
        while leftmost.left:
            
            curr = leftmost
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            
            leftmost = leftmost.left
        return root