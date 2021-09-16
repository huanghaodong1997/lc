pros = [[5,4], [4,3], [6,5], [3,5]]
import heapq
def func(pros, k):
    max_dis = max((p[0] for p in pros))

    h = []

    for i, p in enumerate(pros):
        pms = (max_dis - p[0]) * p[1]
        heapq.heappush(h, (pms, -i))
        if len(h) > k:
            heapq.heappop(h)
    ans = []
    while h:
        _, idx = heapq.heappop(h)
        ans.append(-idx)
    return ans[::-1]
print(func(pros, 2))