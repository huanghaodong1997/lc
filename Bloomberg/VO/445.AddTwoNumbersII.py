# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class ReverseInputSolution:
    def reverseLinkedList(self, root):
        if not root or not root.next:
            return root
        prev, curr = None, root
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        r1, r2 = self.reverseLinkedList(l1), self.reverseLinkedList(l2)
        
        
        prev = None
        carry = 0
        while r1 or r2:
            num = carry
            if r1:
                num += r1.val
                r1 = r1.next
            if r2:
                num += r2.val
                r2 = r2.next
            carry = 0 if num < 10 else 1
            num = num % 10
            curr = ListNode(num)
            curr.next = prev
            prev = curr
        if carry == 1:
            head = ListNode(1, prev)
            return head
        return prev
# follow up
class NoReverseInputSolution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return None
        if l1 and not l2: return l1
        if l2 and not l1: return l2
        n1 = 0
        n2 = 0
        cursor = l1
        while cursor:
            n1 += 1
            cursor = cursor.next
        cursor = l2
        while cursor:
            n2 += 1
            cursor = cursor.next
        if n2 > n1:
            tmp = l1
            l1 = l2
            l2 = tmp
            tmp = n1
            n1 = n2
            n2 = tmp
        c1, c2 = l1, l2
        prev = None
        while c1 and c2:
            num = c1.val
            if n1 == n2:
                num += c2.val
                n2 -= 1
                c2 = c2.next
            n1 -= 1
            c1 = c1.next
            curr = ListNode(num, prev)
            prev = curr
        cursor = prev
        prev = None
        carry = 0
        while cursor:
            num = cursor.val
            if carry == 1:
                num += 1
            if num >= 10:
                carry = 1
                num -= 10
            else:
                carry = 0
                
            cursor.val = num
            tmp_next = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = tmp_next
        if carry == 1:
            return ListNode(1, prev)
        return prev
            
            
class RecursiveSolution:
    
    def getLength(self, l):
        n = 0
        while l:
            l = l.next
            n += 1
        return n
    
    def helper(self, l1, l2, s1, s2):
        if not l1:
            return None
        result = ListNode(l1.val + l2.val) if s1 - s2 == 0 else ListNode(l1.val)
        next_node = self.helper(l1.next, l2.next, s1 - 1, s2 - 1) if s1 - s2 == 0 else self.helper(l1.next, l2, s1 - 1, s2)
        
        if next_node and next_node.val > 9:
            result.val += 1
            next_node.val = next_node.val % 10
        result.next = next_node
        return result
        
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif not l1 and not l2:
            return None
        
        s1, s2 = self.getLength(l1), self.getLength(l2)
        
        # in case the next node is larger than 9
        head = ListNode(1)
        
        if s1 >= s2:
            head.next = self.helper(l1, l2, s1, s2)
        else:
            head.next = self.helper(l2, l1, s2, s1)
            
        if head.next.val > 9:
            head.next.val = head.next.val % 10
            return head
        
        return head.next