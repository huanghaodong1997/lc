class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
# Time: O(nlogk)
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        if not lists: return None
        h = []
        k = len(lists)
        identi = 0
        # use unique id to seperate node with same value
        for i in range(k):
            node = lists[i]
            if not node: continue
            heapq.heappush(h, (node.val, identi, node))
            identi += 1
        head = cursor = ListNode(0)
        while h:
            _, _, min_node = heapq.heappop(h)
            cursor.next = min_node
            if min_node.next:
                heapq.heappush(h, (min_node.next.val, identi, min_node.next))
                identi += 1
            cursor = cursor.next
            min_node.next = None
        return head.next