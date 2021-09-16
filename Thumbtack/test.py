nums = [2,4,8,2]
maxOperations = 4
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        cur_max = max(nums)
        counter = Counter(nums)
        
        while maxOperations > 0:
            if cur_max not in counter:
                while cur_max > 0 and cur_max not in counter:
                    cur_max -= 1
            half1 = cur_max // 2
            half2 = cur_max - half1
            counter[half1] += 1
            counter[half2] += 1
            counter[cur_max] -= 1
            if counter[cur_max] == 0:
                del counter[cur_max]
        return max(counter.keys())