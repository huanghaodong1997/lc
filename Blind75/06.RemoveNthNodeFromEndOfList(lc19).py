# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        first = second = dummy
        
        # Suppose you get N nodes
        # If a node walk from dummy head to the end of list, the first node would need to walk "N + 1" steps (extra step because the dummy head)
        # You want the second node to point to the n - 1 th node from the end of list ( so you can delete the nth node)
        # After the second node reach the n - 1 th from the end of list position, it has n + 1 steps to the end (null)
        # So the second node must walk N + 1 - (n + 1) = N - n step from the dummy node
        # The first node also want to walk N - n steps to the end of list(null) after the first round of walk, so you don't need to actually calculate the number of N
        # So for the first round of walk, the first node need to walk N + 1 - (N - n) = n + 1 steps
        for _ in range(n + 1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        return dummy.next