# Leetcode https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i , j = 0, 1
        while j < len(prices):
            buy = prices[i]
            sell = prices[j]

            if sell - buy > profit:
                profit = sell - buy
                
            if sell - buy < 0:
                i = i+1 #1
                j = i+1 #2
                continue            
            j = j+1

        return profit 

# 2nd Approach
