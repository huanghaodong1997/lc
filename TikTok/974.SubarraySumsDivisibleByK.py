#Running Sum[i]%K == Running Sum[j]%k that means we have sum(i,j) which is divisible by K.
from collections import Counter
class Solution:
    def subarraysDivByK(self, A, K: int) -> int:
        counter = Counter()
        cur_sum = 0
        res = 0
        counter[0] = 1
        for num in A:
            cur_sum += num
            key = cur_sum % K
            res += counter[key]
            counter[key] += 1
        return res
            