from collections import Counter
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        freq = Counter(t)
        required = len(freq)
        
        # left pointer contract the window
        # right pointer expand the window
        # satisfy is used to keep track of how many unique characters in t are present in the current window in its desired frequency. e.g. AABC has 3 unique chars, so satisfy need to be 3 to let window satisfy the constraint
        l = r = satisfy = 0
        window = Counter()
        
        # tuple of the form (window length, left, right)
        ans = (float("inf"), None, None)
        
        while r < len(s):
            ch = s[r]
            
            window[ch] = window.get(ch, 0) + 1
            
            # If the added char meet the requirement, increment satisfy var
            if ch in freq and window[ch] == freq[ch]:
                satisfy += 1
            
            # try to shirnk the window as minnimum as possible while it still satisfy the constraint
            while l <= r and required == satisfy:
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                left_ch = s[l]
                window[left_ch] -= 1
                
                # One required character is poped of of the window, stop shirnking
                # Must continue expanding to right
                if left_ch in freq and freq[left_ch] > window[left_ch]:
                    satisfy -= 1
                l += 1
            
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]