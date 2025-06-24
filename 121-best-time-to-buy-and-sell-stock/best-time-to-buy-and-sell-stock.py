class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit=0
        # buy=prices[0]
        # for sell in prices[1:]:
        #     if sell>buy:
        #         profit=max(profit,sell-buy)
        #     else:
        #         buy=sell
        # return profit
        profit=0
        buy=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            else:
                profit=max(profit,prices[i]-buy)
        return profit