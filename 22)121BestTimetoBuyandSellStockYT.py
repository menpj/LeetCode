
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#121. Best Time to Buy and Sell Stock
#yt solution,better and cleaner than my solution,okay solution
#https://www.youtube.com/watch?v=1pkOgXD63yU
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size=len(prices)
        if size<2:
            return 0
        
        left,right=0,1
        buy,sell=left,right
        profit=prices[right]-prices[left]
        while right<size:
            if prices[right]>prices[left]:
                
                curprofit=prices[right]-prices[left]
                if curprofit>profit:
                    profit=curprofit
                    buy,sell=left,right           
            else:
                left=right
                
            
            right=right+1
        
        if profit>0:
            return profit
        else:
            return 0


            

        