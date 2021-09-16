from collections import Counter
from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counter = Counter(s)
        maxUnique = len(counter)
        ans = 0
        
        for uniques in range(1, maxUnique + 1):
            l = r = 0
            win = defaultdict(int)
            satisfy = 0
            found = 0
            while r < len(s):
                if found <= uniques:
                    win[s[r]] += 1
                    if win[s[r]] == 1:
                        found += 1
                    if win[s[r]] == k:
                        satisfy += 1
                    r += 1
                else:
                    if win[s[l]] == k:
                        satisfy -= 1
                    if win[s[l]] == 1:
                        found -= 1
                    win[s[l]] -= 1
                    l += 1
                if found == uniques and satisfy == uniques:
                    ans = max(ans, r - l)
                    
                    
        
        return ans
                
            
                