class Solution:
    def numDupDigitsAtMostN(self, N):
        L = [int(ch) for ch in str(N + 1)]
        print(L)
        #n is the length of digit
        res, n = 0, len(L)
        #Transform N + 1 to arrayList
        # Count the number with digits < n
        # Count the number with same prefix
        def A(m, n):
            return 1 if n == 0 else A(m, n - 1) * (m - n + 1)
        
        # calculate non-repeated numeber of pattern
        # *, **, ***, ... until length of L which is n
        # EG: n = 4
        # A(9,4)
        for i in range(1, n): res += 9 * A(9, i - 1)
        s = set()
        
        # for every digit x in L
        # let's say that L = [1, 2, 3, 4, 5]
        for i, x in enumerate(L):
            # i means how many digit u are going to use as prefix
            # 
            # the range of y should be in range[0, x)
            for y in range(0 if i else 1, x):
                if y not in s:
                    res += A(9 - i, n - i - 1)
            # let's say if we meet the same number again, 
            # then we cannot have more unique digits number from now on, so we break
            if x in s: break
            s.add(x)
        return N - res