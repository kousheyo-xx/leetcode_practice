class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        maxProfit=0
        minPrice=prices[0]
        for i in range(1,n):
            minPrice=min(prices[i],minPrice)
            maxProfit=max(maxProfit,prices[i]-minPrice)
        return maxProfit