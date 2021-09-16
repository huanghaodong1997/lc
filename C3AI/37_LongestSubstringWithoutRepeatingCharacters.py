class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        i = j = 0
        res = 0
        while j < len(s):
            while i < j and s[j] in window:
                window.remove(s[i])
                i += 1
            res = max(res, j - i + 1)
            window.add(s[j])
            j += 1
        return res