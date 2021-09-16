class Solution:
    def countDigitOne(self, n: int) -> int:
        # count 1's at every digit
        
        # One's place
        # up to 10: 1 one
        # up to 20: 2 one's
        # up to 160: 16 one's
        # up to 161: 17 one's
        # upto 16x(x > 1): 17 one's
        
        # Ten's place:
        # up to 100: 1 * 10 one
        # up to 1600: 16 * 10 one
        # up to 161x: 161 + x one's
        # up to 1699: 160 + 10 one's 
        
        # so the formula, i from 1 - 10
        # divider = i * 10
        #                               up to 161x situation      up to 1699 situation
        # (n / divider) * i + min(max(n % divider - i + 1, 0),    10)
        res = 0 
        i = 1
        while i <= n:
            divider = i * 10
            res += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10
        return res