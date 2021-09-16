class Solution:
    # 把问题转换成 求 把一个arr 分成两个group的 和的最小差值
    def lastStoneWeightII(self, stones) -> int:
        total = sum(stones)
        max_weight = total // 2
        
        dp = [0] * (max_weight + 1)
        
        for v in stones:
            for w in range(max_weight, -1, -1):
                if w - v >= 0:
                    # dp[w] mean 如果最多可以拿w 的石头时， 当前group的最大值是多少
                    dp[w] = max(dp[w - v] + v, dp[w])
        return abs(total - dp[-1] - dp[-1])