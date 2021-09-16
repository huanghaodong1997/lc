import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.balance = 0
        #min heap
        self.r_heap = []
        
        #max heap
        self.l_heap = []

    # log(n)
    def addNum(self, num: int) -> None:
        if not self.l_heap or num < -self.l_heap[0]:
            heapq.heappush(self.l_heap, -num)
            self.balance -= 1
        else:
            heapq.heappush(self.r_heap, num)
            self.balance += 1
        
        # move right to left
        if self.balance > 1:
            heapq.heappush(self.l_heap, -heapq.heappop(self.r_heap))
            self.balance = 0
        elif self.balance < -1:
            heapq.heappush(self.r_heap, -heapq.heappop(self.l_heap))
            self.balance = 0
            
    
    # O(1)
    def findMedian(self) -> float:
        if self.balance == -1:
            return -self.l_heap[0]
        elif self.balance == 0:
            return (-self.l_heap[0] + self.r_heap[0]) / 2
        elif self.balance == 1:
            return self.r_heap[0]
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()