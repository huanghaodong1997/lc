# 题目有点绕，用一个triple代表city，比如“AAA”，“BBB”都可以代表city
# 然后这些城市有一个连通的无向图
# 比如
#      “AAA”
#       /  \
# "BBB" "CCC"
# 暂时可以先假设只有三个city，
# 然后给一条path，比如["BBD"->"AAD"->"CCA"],求最少转换数
# 此case应该返回3，所以就是["BBB"->"AAA"->"CCC"]和path 字符串diff一下

from collections import defaultdict
from functools import lru_cache
connection = [['AAA', 'BBB'], ['AAA', 'CCC'], ['BBB', 'DDD'], ['DDD', 'EEE'], ['CCC', 'EEE']]
#path = ['BBD', 'AAD', 'CCA']
#path = ['BBB', 'CCB']
paths = [
    ['AAA', 'BBB', 'CCC'],
    ['ABC', 'CCC'],
    ['AAA', 'CCC', 'BDB']
]
# res: 3 2 3
# N   M    O(N + N ^2 * m )  O(M)
cities = ['AAA', 'BBB', 'CCC']

class Solution:
    def minimumCost(self, cities, connection, path) -> int:
        graph = defaultdict(list)
        ans = float('inf')
        for src, dst in connection:
            graph[src].append(dst)
            graph[dst].append(src)

        def cost(city, target):
            return sum([1 if c != t else 0 for c,t in zip(city, target)])

        memo = {}
        # remain_path = "AAA,BBB,CCC"
        def dfs(city, remain_path):
            key = (city, remain_path)
            if len(remain_path) == 3:
                return cost(city, remain_path)
            if key in memo: return memo[key]
            target = remain_path[0:3]
            remain_path = remain_path[4:]
            res = cost(city, target) + min((dfs(neighbour, remain_path) for neighbour in graph[city]))
            memo[key] = res
            return res        
        path_str = ",".join(path)
        for city in cities:
            ans = min(ans, dfs(city, path_str))
        return ans

sol = Solution()
for path in paths:
    print(sol.minimumCost(cities, connection, path))        