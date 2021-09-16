from collections import defaultdict
class DLinkNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class FirstUnique:
    
    def remove(self, node):
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev
        del node
        
    def addToTail(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        
    def addToQueue(self, value):
        node = DLinkNode(value)
        self.addToTail(node)
        self.mp[value] = node

    def __init__(self, nums):
        self.head = DLinkNode(-1)
        self.tail = DLinkNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.freq = defaultdict(int)
        self.mp = {}
        
        for num in nums:
            self.freq[num] += 1
            if self.freq[num] == 1:
                self.addToQueue(num)
            elif self.freq[num] == 2:
                self.remove(self.mp[num])
        
        
    def showFirstUnique(self) -> int:
        return self.head.next.val

    def add(self, value: int) -> None:
        self.freq[value] += 1
        if self.freq[value] == 1:
            self.addToQueue(value)
        elif self.freq[value] == 2:
            self.remove(self.mp[value])
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)