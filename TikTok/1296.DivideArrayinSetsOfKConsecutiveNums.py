from collections import Counter
class Solution:
    def isPossibleDivide(self, nums, k: int) -> bool:
        
        counter = Counter(nums)
        keys = sorted(counter.keys())
        
        for key in keys:
            if counter[key] > 0:
                minus = counter[key]
                for i in range(key, key + k):
                    if counter[i] < minus: return False
                    counter[i] -= minus
        
        return True