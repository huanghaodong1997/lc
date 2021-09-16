import math
def getDivisors(n) : 
      
    # Note that this loop runs till square root 
    i = 1
    tmp = []
    res = 0
    while i <= math.sqrt(n): 
          
        if (n % i == 0) : 
              
            # If divisors are equal, print only one 
            if (n // i == i) : 
                res += i
                tmp.append(i)
            else : 
                # Otherwise print both 
                res += (i + n // i)
                tmp.append(i)
                tmp.append(n // i)
        i = i + 1
    return res - n
def find(n):
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if getDivisors(i) == j and getDivisors(j) == i:
                print((i, j))
find(1000)