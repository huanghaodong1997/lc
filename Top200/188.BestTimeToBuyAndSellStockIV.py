class Solution:
    def maxProfit(self, k: int, prices) -> int:
        #unlimited transactionsx
        if k >= len(prices) // 2:
            maxprofit = 0
        
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    maxprofit += prices[i] - prices[i - 1]
            return maxprofit
        
        n = len(prices)
        dp = [[[0, 0]  for _ in range(k + 1)] for _ in range(n)]
        
        #Meaning of dp
        #[day_number][used_transaction_number][stock_holding_status]
        # The best value you can get in [0:i] day with j transaction, hold the stock or not
        
        for i in range(n):
            for j in range(1, k + 1):
                if i == 0:
                    # note that j is at least 1, so you can do buy transaction
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                # hold the stock in i - 1 day then sell it
                # not holding the stock in i - 1 day
                # will not consume transaction number
                # since only buying will consume transaction
                dp[i][j][0] = max(dp[i - 1][j][1] + prices[i], dp[i - 1][j][0])
                
                # not holding stock in i - 1 day with j - 1 transactions, now you can do one more transaction(buying) 
                dp[i][j][1] = max(dp[i - 1][j - 1][0] - prices[i], dp[i - 1][j][1])
        return dp[n - 1][k][0]