
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
class IterativeSolution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        
        # Use stk to simulate DFS
        
        stk = [head]
        dummy = Node(-1, None, head, None)
        prev = dummy
        while stk:
            curr = stk.pop()
            prev.next = curr
            curr.prev = prev
            
            if curr.next:
                stk.append(curr.next)
            # Make sure that child is in the top of stk, so you can process child first
            if curr.child:
                stk.append(curr.child)
            curr.child = None
            prev = curr
        #clear the link between dummy node and head
        dummy.next.prev = None
        return head
class RecursiveSolution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        dummy = Node(-1, None, head, None)
        # return the tail of current level 
        def dfs(prev, curr):
            # return tail
            if not curr: return prev
            
            prev.next = curr
            curr.prev = prev
            
            tmp = curr.next
            # if curr.child == None, tail = curr
            tail = dfs(curr, curr.child)
            
            # empty the child
            curr.child = None
            return dfs(tail, tmp)
        dfs(dummy, head)
        dummy.next.prev = None
        return head
            