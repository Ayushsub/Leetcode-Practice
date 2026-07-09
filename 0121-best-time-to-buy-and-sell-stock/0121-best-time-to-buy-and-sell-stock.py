class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_return=0
        for i in range(1,len(prices)):
            max_return=max(max_return,prices[i]-min_price)
            min_price=min(prices[i],min_price)
        return max_return

            

        