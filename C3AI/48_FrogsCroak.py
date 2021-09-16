class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ch2Idx = {c : i for i, c in enumerate("croak")}
        cnt = [0] * 5
        frogs = max_frogs = 0
        
        for ch in croakOfFrogs:
            idx = ch2Idx[ch]
            cnt[idx] += 1
            if idx == 0:
                frogs += 1
                max_frogs = max(max_frogs, frogs)
            elif cnt[idx - 1] <= 0:
                return -1
            elif idx == 4:
                frogs -= 1
            cnt[idx - 1] -= 1
        return max_frogs if frogs == 0 else -1
                
                
            