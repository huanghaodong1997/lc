# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    
        dummy = ListNode(-1, head)
        cursor1 = dummy
        prev_tail = None
        new_tail = None
        prev = None
        while m > 1 or n > 0:
            if m > 1 and n > 0:
                cursor1 = cursor1.next
                m -= 1
                n -= 1
            else:
                if not prev_tail:
                    prev_tail = cursor1
                    cursor1 = cursor1.next
                    new_tail = cursor1
                    prev_tail.next = None
                next_node = cursor1.next
                cursor1.next = prev
                prev = cursor1
                cursor1 = next_node
                n -= 1
        new_tail.next = cursor1
        prev_tail.next = prev
        return dummy.next
                
                