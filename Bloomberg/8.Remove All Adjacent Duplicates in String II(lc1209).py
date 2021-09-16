class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        
        for ch in s:
            if not stk:
                stk.append((ch, 1))
            else:
                prev_ch, freq = stk[-1]
                if prev_ch != ch:
                    stk.append((ch, 1))
                else:
                    if freq + 1 >= k:
                        stk.pop()
                    else:
                        stk[-1] = (prev_ch, freq + 1)
        res = ""
        for ch, freq in stk:
            res += ch * freq
        return res