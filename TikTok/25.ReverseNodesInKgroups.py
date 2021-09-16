# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def reverseLinkedList(self, start, end): #return new tail after reverse it
        if not end:
            return start, None
        
        prev, curr = None, start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        curr.next = prev
        return end, start
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or not head: return head
        
        remain = k
        start = curr = head
        
        while curr and remain > 1:
            curr = curr.next
            remain -= 1
        next_node = curr.next if curr else None
        
        new_head, new_tail = self.reverseLinkedList(start, curr)
        if next_node:
            new_tail.next = self.reverseKGroup(next_node, k)
        
        return new_head
        