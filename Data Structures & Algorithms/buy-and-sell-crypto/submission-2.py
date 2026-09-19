class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        start = prices[0]
        
        for i in range(1, len(prices), 1):
            if max_profit < prices[i] - start:
                max_profit = prices[i] - start
            if  start > prices[i]:
                start = prices[i]
        return max_profit