
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class O1Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        # This O(1) method's intuitive is that we always want to know
        # Where is the random node's location, after
        # we interleave the copied node with original node
        # we know that the copied node is just one after the original node
        
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head
    
        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old
class RecursiveSolution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node2Copy = {}
        
        def helper(node):
            if not node: return None
            if node in node2Copy: return node2Copy[node]
            
            root = Node(node.val)
            node2Copy[node] = root
            root.next = helper(node.next)
            root.random = helper(node.random)
            
            return root
        return helper(head)

class IterativeSolution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        mp = {}
        
        cursor = head
        prev = None
        res = None
        while cursor:
            copied = Node(cursor.val) if cursor not in mp else mp[cursor]
            mp[cursor] = copied
            if not res: res = copied
            if cursor.random in mp:
                copied.random = mp[cursor.random]
            else:
                random_node = None if not cursor.random else Node(cursor.random.val)
                mp[cursor.random] = random_node
                copied.random = random_node
            
            if prev: prev.next = copied
            cursor = cursor.next
            prev = copied
        return res