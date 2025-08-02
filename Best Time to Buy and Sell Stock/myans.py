class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0 
        l = 0
        k = len(prices)
        for r in range(k):
            while prices[l]>prices[r] and l<r:
                l+=1
            max_profit = max(prices[r] - prices[l],max_profit)
        return max_profit 