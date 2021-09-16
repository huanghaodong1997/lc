# Remove K digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        
        for digit in num:
            while k > 0 and stk and stk[-1] > digit:
                stk.pop()
                k -= 1
            stk.append(digit)
        final = stk if k == 0 else stk[:-k]
        res = "".join(final).lstrip('0')
        return res if res else '0'