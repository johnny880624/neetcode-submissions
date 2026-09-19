class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp_profit = 0
        max_profit = 0
        start = prices[0]
        
        for i in range(1, len(prices), 1):
            temp_profit = prices[i] - start
            if max_profit < temp_profit:
                max_profit = temp_profit
            if  start > prices[i]:
                start = prices[i]
            
        
        return max_profit