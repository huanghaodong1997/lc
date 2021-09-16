from collections import defaultdict
class Solution:
    def numSplits(self, s: str) -> int:
        d_l = 0
        l, r = defaultdict(int), defaultdict(int) 
        for ch in s:
            r[ch] += 1
        d_r = len(r.keys())
        
        ans = 0
        
        for ch in s:
            r[ch] -= 1
            l[ch] += 1
            
            if r[ch] == 0:
                d_r -= 1
            if l[ch] == 1:
                d_l += 1
            
            if d_l == d_r:
                ans += 1
        return ans