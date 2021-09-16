
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# O(n) space: Level order traversal

# O(1) space: Utilizing the fact that we can level traverse using next pointer
# The idea is to use a helper function toa process the node as well as
# return the next level leftmost node and next level prev node(the node needed to estabilish next pointer to next node which
# need to be process)
class Solution:
    
    def process_child(self, child, prev, leftmost):
        if child:
            # we are traversing the first left child node of the next level, so set the leftmost pointer
            if not prev:
                leftmost = child
            else:
                prev.next = child
            prev = child
        return leftmost, prev
    
    def connect(self, root: 'Node') -> 'Node':
        
        leftmost = root
        
        # still have level nodes that need to be processed
        while leftmost:
            
            curr = leftmost
            
            leftmost = None
            prev = None
            
            while curr:
                leftmost, prev = self.process_child(curr.left, prev, leftmost)
                leftmost, prev = self.process_child(curr.right, prev, leftmost)
                curr = curr.next
        return root