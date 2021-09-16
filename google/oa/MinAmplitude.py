import heapq
arr1 = [-1, 3, -1, 8, 5, 4]

arr2 = [10,10,3,4,10]
def minAmplitude(arr):
    max_h, min_h = [], []
    for num in arr:
        heapq.heappush(max_h, num)
        heapq.heappush(min_h, -num)

        if len(min_h) > 4:
            heapq.heappop(min_h)
        if len(max_h) > 4:
            heapq.heappop(max_h)

    max_4, min_4 = [], []
    while max_h:
        max_4.append(heapq.heappop(max_h))
    while min_h:
        min_4.append(-heapq.heappop(min_h))
    ans = float('inf')
    for i in range(0, 4):
        ans = min(ans, max_4[i] - min_4[3 - i])
    return ans
print(minAmplitude(arr1))
print(minAmplitude(arr2))