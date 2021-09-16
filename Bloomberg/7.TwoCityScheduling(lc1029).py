# Greedy, 优先安排 去城市a 和去城市b 的cost间差值大的候选人，因为若不先安排他们，就会造成更大的损失
class Solution:
    def twoCitySchedCost(self, costs) -> int:
        diff = sorted([(-abs(cost[0] - cost[1]), cost[0], cost[1], i) for i,cost in enumerate(costs)])
        cnt_a = cnt_b = 0
        n = len(costs)
        res = 0
        for _, cost_a, cost_b, idx in diff:
            if cnt_a == n // 2:
                cnt_b += 1
                res += cost_b
            elif cnt_b == n // 2:
                cnt_a += 1
                res += cost_a
            elif cost_a < cost_b:
                cnt_a += 1
                res += cost_a
            elif cost_b <= cost_a:
                cnt_b += 1
                res += cost_b
        return res