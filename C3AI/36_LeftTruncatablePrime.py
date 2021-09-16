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
def isTruncatable(n, isPrime):
    num = str(n)
    while num:
        val = int(num)
        if val not in isPrime or (len(num) > 1 and num[1] == '0'):
            break
        num = num[1:]
    return True if not num else False
def getAllTruncatable(n):
    isPrime = set(SieveFindAllPrime(n))
    res = []
    for i in range(2, n + 1):
        if i in isPrime and isTruncatable(i, isPrime):
            res.append(i)
    return res
print(getAllTruncatable(1000))