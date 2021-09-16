# O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = n
        if N < 0:
            x = 1 / x
            N = -N
        
        def fastPow(x, n):
            if n == 0: return 1.0
            half = fastPow(x, n // 2)

            # if n is even, we can calculate fastPow(x, n // 2) and multiply itself
            if n % 2 == 0:
                return half * half
            else:
            # else, we can multiply one more x to get the result
                return half * half *x
        
        return fastPow(x, N)