# Reverse input
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            # keep the next node
            tmp = head.next
            # reverse the link
            head.next = last
            # update the last node and the current node
            last = head
            head = tmp
        
        return last
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # reverse lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        head = None
        carry = 0
        while l1 or l2:
            # get the current values 
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            
            # current sum and carry
            val = (carry + x1 + x2) % 10
            carry = (carry + x1 + x2) // 10
            
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr
            
            # move to the next elements in the lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head


# Not reversing input

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1 and not l2: return None
#         if l1 and not l2: return l1
#         if l2 and not l1: return l2
#         n1 = 0
#         n2 = 0
#         cursor = l1
#         while cursor:
#             n1 += 1
#             cursor = cursor.next
#         cursor = l2
#         while cursor:
#             n2 += 1
#             cursor = cursor.next
#         if n2 > n1:
#             tmp = l1
#             l1 = l2
#             l2 = tmp
#             tmp = n1
#             n1 = n2
#             n2 = tmp
#         c1, c2 = l1, l2
#         prev = None
#         while c1 and c2:
#             num = c1.val
#             if n1 == n2:
#                 num += c2.val
#                 n2 -= 1
#                 c2 = c2.next
#             n1 -= 1
#             c1 = c1.next
#             curr = ListNode(num, prev)
#             prev = curr
#         cursor = prev
#         prev = None
#         carry = 0
#         while cursor:
#             num = cursor.val
#             if carry == 1:
#                 num += 1
#             if num >= 10:
#                 carry = 1
#                 num -= 10
#             else:
#                 carry = 0
                
#             cursor.val = num
#             tmp_next = cursor.next
#             cursor.next = prev
#             prev = cursor
#             cursor = tmp_next
#         if carry == 1:
#             return ListNode(1, prev)
#         return prev
            
            
            