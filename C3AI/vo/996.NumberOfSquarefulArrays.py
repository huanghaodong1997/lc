from collections import defaultdict
from collections import Counter
class Solution:
    def numSquarefulPerms(self, A) -> int:
        graph = defaultdict(list)
        count = Counter(A)
        # convert it to a graph problem
        for x in count:
            for y in count:
                if int((x + y)**0.5)**2 == (x + y):
                    graph[x].append(y)
        res = 0
        def dfs(node, remain):
            if remain == 0: return 1
            ans = 0
            count[node] -= 1
            for candi in graph[node]:
                if count[candi] > 0:
                    ans += dfs(candi, remain - 1)
            count[node] += 1
            return ans
        for node in count:
            res += dfs(node, len(A) - 1)
        return res
from functools import lru_cache
import math
class DPSolution:
    def numSquarefulPerms(self, A):
        N = len(A)

        def edge(x, y):
            r = math.sqrt(x+y)
            return int(r + 0.5) ** 2 == x+y

        graph = [[] for _ in range(len(A))]
        for i, x in enumerate(A):
            for j in range(i):
                if edge(x, A[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        # find num of hamiltonian paths in graph

        @lru_cache(None)
        def dfs(node, visited):
            if visited == (1 << N) - 1:
                return 1

            ans = 0
            for nei in graph[node]:
                if (visited >> nei) & 1 == 0:
                    ans += dfs(nei, visited | (1 << nei))
            return ans

        ans = sum(dfs(i, 1<<i) for i in range(N))
        count = Counter(A)
        for v in count.values():
            ans //= math.factorial(v)
        return ans