# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         Maintain two pointers pApA and pBpB initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.
# When pApA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pBpB reaches the end of a list, redirect it the head of A.
# If at any point pApA meets pBpB, then pApA/pBpB is the intersection node

    # The main idea is to let pA and pB begin at a postion that has same remaning node
    # in both list
    
        lenA = lenB = 0
        pA = headA
        pB = headB
        
        while pA:
            lenA += 1
            pA = pA.next
        
        while pB:
            lenB += 1
            pB = pB.next
        
        pA, pB = headA, headB
        
        while pA != pB and (lenA > 0 and lenB > 0):
            if lenA > lenB:
                pA = pA.next
                lenA -= 1
            elif lenB > lenA:
                pB = pB.next
                lenB -= 1
            else:
                pA = pA.next
                pB = pB.next
                lenA -= 1
                lenB -= 1
        return pA if pA == pB else None