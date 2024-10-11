class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            potential_profit = price - min_price        
            if potential_profit > max_profit:
                max_profit=potential_profit
                
        return max_profit 