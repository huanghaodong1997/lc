class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for ch in s:
            if not stk or stk[-1][0] != ch:
                stk.append((ch, 1))
            # stk[-1][0] == ch
            else:
                _, freq = stk[-1]
                # If reach the limit, remove the characters
                if freq + 1 == k:
                    stk.pop()
                # Combine the char with top of the stk by modify the top
                else:
                    stk[-1] = (ch, freq + 1)
        ans = ""
        for ch, freq in stk:
            ans += ch * freq
        return ans