class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                max_profit = max(profit, max_profit)
        return max_profit
