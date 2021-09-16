class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        prime = [True for _ in range(n + 1)]
        p = 2
        res = 0
        while p * p <= n:
            # If prime [p] is not changed, it is a prime
            if prime[p] == True:
                i = p * p
                while i <= n:
                    prime[i] = False
                    i += p
            p += 1
        for i in range(2, n):
            if prime[i]:
                res += 1
        return res