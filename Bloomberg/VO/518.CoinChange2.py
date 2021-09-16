class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        # classic knapsack
        # coin is the weight of items
        for coin in coins:
            # amount is the maximum Weight you can put all the items(coin)
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        return dp[amount]
        