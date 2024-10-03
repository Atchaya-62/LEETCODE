class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell=0
        hold=-math.inf
        for price in prices:
            sell=max(sell,hold+price)
            hold=max(hold,-price)

        return sell
        
