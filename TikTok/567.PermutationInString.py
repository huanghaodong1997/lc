from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        target = Counter(s1)
        src = Counter()
        
        l, r = 0, 0
        numChars = len(target)
        satisfy = 0
        while r <= len(s2):
            if satisfy != numChars:
                if r == len(s2): return False
                l_ch, r_ch = s2[l], s2[r]
                src[r_ch] += 1
                if target[r_ch] == src[r_ch]:
                    satisfy += 1
                r += 1
            else:
                while satisfy == numChars:
                    src[s2[l]] -= 1
                    if src[s2[l]] < target[s2[l]]:
                        satisfy -= 1
                    l += 1
                if r - l + 1 == len(s1):
                    return True

        return False
        
        
        
        