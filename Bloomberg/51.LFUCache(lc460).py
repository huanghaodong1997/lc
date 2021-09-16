from collections import OrderedDict
from collections import defaultdict
# Ordered dict就是python的linked hashmap
class Node:
    def __init__(self, key, value, count):
        self.key = key
        self.val = value
        self.count = count
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.least_freq = 0
        self.freq_mp = defaultdict(OrderedDict)
        self.key_mp = {}
    def get(self, key: int) -> int:
        if key not in self.key_mp: return -1
        
        node = self.key_mp[key]
        
        del self.freq_mp[node.count][key]
        if not self.freq_mp[node.count]:
            del self.freq_mp[node.count]
            
        node.count += 1
        self.freq_mp[node.count][key] = node
        if not self.freq_mp[self.least_freq]:
            self.least_freq += 1
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.key_mp:
            self.key_mp[key].val = value
            self.get(key)
            return 
        else:
            if len(self.key_mp) == self.capacity:
                key_to_del, _ = self.freq_mp[self.least_freq].popitem(last=False)
                del self.key_mp[key_to_del]
            self.least_freq = 1
            self.key_mp[key] = self.freq_mp[1][key] = Node(key, value, 1)
            
             
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)