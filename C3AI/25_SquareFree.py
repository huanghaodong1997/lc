def isSquareFree(n):
    if n <= 3: return True
    isPrime = SieveFindAllPrime(n)
    res = []
    for j in range(4, n + 1):
        flag = True
        i = 2
        while i * i <= n:
            # Its Prime factorization has exactly one factor, so j should not be divisible by 
            # a prime number square
            if isPrime[i] and j % (i * i) == 0:
                flag = False
                break
            i += 1
        if flag:
            res.append(j)
    return res
def SieveFindAllPrime(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    res = []
    while p * p <= n:
        # If prime [p] is not changed, it is a prime
        if prime[p] == True:
            i = p * p
            while i <= n:
                prime[i] = False
                i += p
        p += 1
    for i in range(2, n + 1):
        if prime[i]:
            res.append(i)
    return res

print(isSquareFree(100))