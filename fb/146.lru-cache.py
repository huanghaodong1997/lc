class DLinkNode:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.head = DLinkNode(-1, -1)
        self.tail = DLinkNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.key2Node = {}
    
    def moveToHead(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        node.prev = node.next = None
        self.addToHead(node)
        
    def popTail(self):
        prevNode = self.tail.prev
        prevNode.prev.next = self.tail
        self.tail.prev = prevNode.prev
        prevNode.prev = prevNode.next = None
        del self.key2Node[prevNode.key]
    
    def addToHead(self, node):
        nextNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nextNode
        nextNode.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.key2Node:
            return -1
        node = self.key2Node[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key2Node:
            node = self.key2Node[key]
            node.val = value
            self.moveToHead(node)
        else:
            if self.capacity == 0:
                self.popTail()
                self.capacity += 1
            node = DLinkNode(key, value)
            self.key2Node[key] = node
            self.addToHead(node)
            self.capacity -= 1
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)