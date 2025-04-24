#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#121. Best Time to Buy and Sell Stock
#my solution,okay solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size=len(prices)
        if size<2:
            return 0
        i=1
        low,buy=0,0
        sell=1
        profit=prices[sell]-prices[buy]
        while i<size:
            if prices[i]-prices[low]>profit:
                sell=i
                buy=low
                profit=prices[sell]-prices[buy]
            #if prices[i]<prices[buy] and prices[i]<prices[low]:
            if prices[i]<prices[buy] and prices[i]<prices[low]:
                low=i
                #print(prices[low])
            i=i+1
        #profit=prices[sell]-prices[buy]
        if profit>0:
            return profit
        else:
            return 0


            

        