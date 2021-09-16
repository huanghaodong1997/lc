from random import randint
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.val2Idx = {}
        
    # Append in list is O(1) operation
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val2Idx:
            return False
        else:
            self.arr.append(val)
            self.val2Idx[val] = len(self.arr) - 1
            return True

    # only pop element from tail
    # You can swap the element that is going to be deleted with the tail element
    # than pop tail
    # So the time complexity is O(1)
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val2Idx:
            return False
        else:
            idx = self.val2Idx[val]
            
            tail = self.arr[-1]
            
            tail_idx = self.val2Idx[tail]
            
            self.arr[idx] = self.arr[tail_idx]
            self.arr.pop()
            self.val2Idx[tail] = idx
            del self.val2Idx[val]
            return True
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = randint(0, len(self.arr) - 1)
        return self.arr[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()