
# Naive O(n sqrt(n))
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
def FindAllPrime(n):
    arr = []
    for i in range(2, n + 1):
        if isPrime(i):
            arr.append(i)
    return arr
print(FindAllPrime(50))

#Sieve of Eratosthenes O(n log(log(n))) Best
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
print(SieveFindAllPrime(50))