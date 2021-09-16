import bisect
import random
class Solution:

    def __init__(self, w):
        self.prefix_sum = [w[0]]
        for i in range(1, len(w)):
            self.prefix_sum.append(self.prefix_sum[-1] + w[i])
        self.total_sum = self.prefix_sum[-1]
    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        return bisect.bisect_right(self.prefix_sum, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()