#We can take two pointers before and after to keep track of the 
# two linked lists as described above. These two pointers could be used two 
# create two separate lists 
# and then these lists could be combined to form the desired reformed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: return None
        small, large = ListNode(-1), ListNode(-1)
        sCursor, lCursor = small, large
        
        cursor = head
        while cursor:
            nextNode = cursor.next
            if cursor.val < x:
                sCursor.next = cursor
                sCursor = sCursor.next
            else:
                lCursor.next = cursor
                lCursor = lCursor.next
            cursor.next = None
            cursor = nextNode
        sCursor.next = large.next
        return small.next