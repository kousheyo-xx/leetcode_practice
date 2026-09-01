class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxProfit=0
        minPrice=prices[0]
        for i in range(n):
            maxProfit=max(maxProfit,prices[i]-minPrice)
            minPrice=min(minPrice,prices[i])
        return maxProfit