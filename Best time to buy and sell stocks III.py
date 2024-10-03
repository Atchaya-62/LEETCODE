class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        selltwo=0
        holdtwo=-math.inf
        sellone=0
        holdone=-math.inf
        for price in prices:
            selltwo=max(selltwo,holdtwo+price)
            holdtwo=max(holdtwo,sellone-price)
            sellone=max(sellone,holdone+price)
            holdone=max(holdone,-price)
        return selltwo
        
