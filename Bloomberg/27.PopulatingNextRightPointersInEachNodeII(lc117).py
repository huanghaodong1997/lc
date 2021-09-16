
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    
    def process_child(self, node, prev, leftmost):
        if not node: return prev, leftmost
        if prev == None:
            return node, node
        else:
            prev.next = node
            return node, leftmost
                
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                prev, leftmost = self.process_child(curr.left, prev, leftmost)
                prev, leftmost = self.process_child(curr.right, prev, leftmost)
                curr = curr.next
        return root
            
            
            