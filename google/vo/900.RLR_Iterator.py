class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.i = 0
        self.arr = []
        self.ptrs = []
        
        for j in range(0, len(encoding), 2):
            if encoding[j] != 0:
                self.arr.append(encoding[j + 1])
                self.ptrs.append(encoding[j])
        for j in range(1, len(self.ptrs)):
            self.ptrs[j] += self.ptrs[j - 1]
        self.offset = 0
        self.size = self.ptrs[-1]
        # ptrs = [3, 5]
    
    def binary_search(self, ptrs, target, lo, hi):
        # find the left boundary of mid, where self.ptrs[mid - 1] < target, self.ptrs[mid] >= target
        while lo < hi:
            mid = (lo + hi) // 2
            if ptrs[mid] > target:
                hi = mid
            elif ptrs[mid] < target:
                lo = mid + 1
            else:
                return mid
        
        return hi
            
            
    
    def next(self, n: int) -> int:
        idx = self.offset + n
        self.offset = idx
        if self.offset > self.size:
            return -1
        
        if self.ptrs[self.i] >= self.offset:
            
            return self.arr[self.i]
        
        # binary search the correct self.i
        self.i = self.binary_search(self.ptrs, idx, self.i, len(self.ptrs))
        return self.arr[self.i]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)