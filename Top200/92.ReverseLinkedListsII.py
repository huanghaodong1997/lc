class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# swap the value of nodes
class BacktrackingRecursiveSolution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers     
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next           

        recurseAndReverse(right, m, n)
        return head

# redirect the link, not swapping the value
class IterativeSolution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    
        dummy = ListNode(-1, head)
        cursor1 = cursor2 = dummy
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