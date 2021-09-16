import math
import random


def get_n(start, sum_num):
    n = int(math.sqrt(2*sum_num))-start
    while True:
        # print(n)
        if get_sum(start, n) > sum_num:
            break
        n += 1
    return n-1


def get_sum(start, n):
    return (start+start+2*n-2)*n/2


def get_whos_first(a, b):
    swap = False
    if a < b:
        a, b = b, a
        swap = True
    total = 0
    diff1 = a-b
    n = int(math.sqrt(2*diff1))
    total += n
    first_sum = (1+n)*n//2
    a -= first_sum
    if a == b: swap = False
    more_steps1 = get_n(n+1, a)
    total += more_steps1
    a_sum = (n+1+n+1+2*more_steps1-2)*more_steps1/2
    a_left = int(a-a_sum)

    b_sum = (n+2+n+2+2*more_steps1-2)*more_steps1/2
    b_left = int(b-b_sum)
    res = n+more_steps1+more_steps1+1
    if b_left < 0:
        b_sum = (n+2+n+2+2*(more_steps1-1)-2)*(more_steps1-1)/2
        b_left = int(b-b_sum)
        res -= 1
    if a_left >= res:
        a_left -= res
        res += 1
    if b_left >= res:
        b_left -= res
        res += 1
    return (res, a_left, b_left) if not swap else (res, b_left, a_left)

print(get_whos_first(8, 11))
print(get_whos_first(11, 8))
print(get_whos_first(2, 2))
print(get_whos_first(9,4))
