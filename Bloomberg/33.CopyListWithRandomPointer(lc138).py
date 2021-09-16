class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
#Recursion
class Solution:

    def __init__(self):
        self.created = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        if head in self.created: return self.created[head]

        new_head = Node(head.val)
        self.created[head] = new_head
        new_head.next = self.copyRandomList(head.next)
        new_head.random = self.copyRandomList(head.random)
        return new_head

# #Iterative
# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         mp = {}
        
#         cursor = head
#         prev = None
#         res = None
#         while cursor:
#             copied = Node(cursor.val) if cursor not in mp else mp[cursor]
#             mp[cursor] = copied
#             if not res: res = copied
#             if cursor.random in mp:
#                 copied.random = mp[cursor.random]
#             else:
#                 random_node = None if not cursor.random else Node(cursor.random.val)
#                 mp[cursor.random] = random_node
#                 copied.random = random_node
            
#             if prev: prev.next = copied
#             cursor = cursor.next
#             prev = copied
#         return res
        