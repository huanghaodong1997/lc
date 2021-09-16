# extend from a small window
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        freq = Counter(t)
        required = len(freq)
        
        # clear out the characters that are not present in t
        filtered_s = []
        for i, char in enumerate(s):
            if char in freq:
                filtered_s.append((i, char))
        l = r = satisfy = 0
        window = Counter()
        ans = [float("inf"), None, None]
        
        while r < len(filtered_s):
            ch = filtered_s[r][1]
            window[ch] += 1
            if window[ch] == freq[ch]:
                satisfy += 1
                
            while l <= r and satisfy == required:
                ch = filtered_s[l][1]
                
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                
                if end - start + 1 < ans[0]:
                    ans = [end - start + 1, start, end]
                
                window[ch] -= 1
                if window[ch] < freq[ch]:
                    satisfy -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]