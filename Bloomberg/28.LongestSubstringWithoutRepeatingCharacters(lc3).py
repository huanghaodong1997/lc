class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        ch_set = set()
        ans = 0
        while j < len(s):
            while s[j] in ch_set:
                ch_set.remove(s[i])
                i += 1
            ch_set.add(s[j])
            j += 1
            ans = max(ans, len(ch_set))
        return ans