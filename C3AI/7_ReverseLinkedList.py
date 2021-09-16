# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 
class RecursiveSolution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # new_head will return along the way from the tail
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

class IterativeSolution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev