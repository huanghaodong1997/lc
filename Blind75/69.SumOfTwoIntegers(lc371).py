class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure x >= y
        if x < y:
            return self.getSum(b, a)  
        
        # a decide the sign
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            while y:
                # instinct of add
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of two positive integers
            while y:
                x, y = x ^ y, ((-x) & y) << 1
        
        return x * sign