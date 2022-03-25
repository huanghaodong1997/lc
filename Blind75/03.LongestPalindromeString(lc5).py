
class Solution:
    def expand(self, s, l, r):
        if s[l] != s[r]:
            return s[l] if l == r - 1 else s[l+1:r]
        if l - 1 < 0 or r + 1 >= len(s):
            return s[l: r + 1]
        return self.expand(s, l - 1, r + 1)
        
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(0, len(s) - 1):
            s1 = self.expand(s, i, i)
            s2 = self.expand(s, i, i + 1)
            res = max(res, s1, s2, key=len)
        return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        start = end = 0
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        for i in range(0,  len(s)):
            one = expand(i, i)
            two = expand(i, i + 1)
            max_ch = max(one, two)
            
            if max_ch >= end - start + 1:
                # new_end - new_start + 1 = max_ch
                # if max_ch % 2 != 0: new_start = i - (max_ch - 1) // 2
                # if max_ch % 2 == 0: new_start = i - (max_ch - 1) // 2
                start = i - (max_ch - 1) // 2
                end = max_ch + start - 1
        return s[start:end+1]
