# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or head.next == None: return head
        n = 1
        oldTail = head
        while oldTail.next:
            n += 1
            oldTail = oldTail.next
        
        k = k % n
        if k == 0: return head
        
        #To close the linked list into the ring. Important
        # after you make this linkedlist a cycle, you only need to decidae where to break the cycle and return new_head
        oldTail.next = head
        to_move = n - k - 1
        new_tail = head
        
        while to_move > 0:
            new_tail = new_tail.next
            to_move -= 1
        new_head = new_tail.next
        new_tail.next = None
        return new_head