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
cities = ['AAA', 'BBB', 'CCC']

class Solution:
    def minimumCost(self, cities, connection, path) -> int:
        graph = defaultdict(list)
        for src, dst in connection:
            graph[src].append(dst)
            graph[dst].append(src)

        def cost(city, stop):
            return sum([1 if c != s else 0 for c, s in zip(city,stop)])

        @lru_cache(None)
        def dp(city, remain_path):
            if len(remain_path) == 3:
                return cost(city, remain_path)
            prefix = remain_path[0:3]
            remain_path = remain_path[4:]
            cur_cost = cost(city, prefix)

            return cur_cost + min((dp(adj, remain_path) for adj in graph[city]))
        path_str = ",".join(path)
        ans = min(dp(city, path_str) for city in cities)
        return ans
sol = Solution()
for path in paths:
    print(sol.minimumCost(cities, connection, path))        