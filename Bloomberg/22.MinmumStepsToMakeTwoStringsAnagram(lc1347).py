from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        res = 0
        for ch in count_t.keys():
            if count_t[ch] > count_s[ch]:
                res += (count_t[ch] - count_s[ch])
        return res