from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        i = j = 0
        max_freq = 0
        counter = Counter()
        ans = 0
        for j in range(n):
            counter[s[j]] += 1
            # we don't care which character has most freq, we just care the size
            
            max_freq = max(max_freq, counter[s[j]])
            
            # Move i pointer when we cannot satisfy the k operations
            if j - i + 1 - max_freq > k:
                counter[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans