
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

# Iterative
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        stk = [head]
        dummy = Node(-1, None, None, None)
        prev = dummy
        while stk:
            curr = stk.pop()
            prev.next = curr
            curr.prev = prev
            
            if curr.next:
                stk.append(curr.next)
            if curr.child:
                stk.append(curr.child)
            curr.child = None
            prev = curr
        dummy.next.prev = None
        return dummy.next

# recursive
# class Solution:
#     def flatten(self, head: 'Node') -> 'Node':
#         if not head: return None
#         dummy = Node(-1, None, head, None)
#         # Treat child as the left subtree. Do preorder DFS
#         def dfs(prev, curr):
#             if curr == None: return prev
#             prev.next = curr
#             curr.prev = prev
#             tmp = curr.next
#             tail = dfs(curr, curr.child)
#             curr.child = None
#             return dfs(tail, tmp)
#         dfs(dummy, head)
#         dummy.next.prev = None
#         return dummy.next
            
            