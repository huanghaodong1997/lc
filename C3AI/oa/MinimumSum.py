import math
import heapq
arr = [1, 2, 3, 4, 5, 6, 7]

def min_sum(arr, k):
    h = []

    for num in arr:
        heapq.heappush(h, -num)
    
    while k:
        num = -heapq.heappop(h)
        heapq.heappush(h, -math.ceil(num / 2))
        k -= 1
    print(h)
    return sum([-num for num in h])
print(min_sum(arr, 3))