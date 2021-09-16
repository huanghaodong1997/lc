# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Add by digit
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return None
        cursor1, cursor2 = l1, l2
        head = ListNode(-1, None)
        cursor = head
        carry = 0
        while cursor1 or cursor2:
            num = 0
            if cursor1:
                num += cursor1.val
                cursor1 = cursor1.next
            if cursor2:
                num += cursor2.val
                cursor2 = cursor2.next
            if carry == 1:
                num += 1
            if num >= 10:
                carry = 1
                num -= 10
            else: carry = 0
            
            cursor.next = ListNode(num, None)
            cursor = cursor.next
        if carry == 1:
            cursor.next = ListNode(1, None)
        return head.next