class DLinkNode:
    def __init__(self, key, val, prev, next_node):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next_node
    
class LRUCache:

    def __init__(self, capacity: int):
        self.head = DLinkNode(-1, -1, None, None)
        self.tail = DLinkNode(-1, -1, self.head, None)
        self.head.next = self.tail
        self.mp = {}
        self.capacity = capacity
        self.size = 0
    def add_to_head(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
    
    def move_to_head(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.add_to_head(node)
    
    def pop_from_tail(self):
        to_del = self.tail.prev
        to_del.prev.next = self.tail
        self.tail.prev = to_del.prev
        to_del.prev, to_del.next = None, None
        del self.mp[to_del.key]

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        node = self.mp[key]
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self.move_to_head(node)
        else:
            node = DLinkNode(key, value, None, None)
            self.mp[key] = node
            if self.size < self.capacity:
                self.add_to_head(node)
                self.size += 1
            else:
                self.pop_from_tail()
                self.add_to_head(node)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)