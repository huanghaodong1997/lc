class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = float('inf')
        
        for p in prices:
            if p < minprice:
                minprice = p
            elif maxprofit < p - minprice:
                maxprofit = p - minprice
        return maxprofit