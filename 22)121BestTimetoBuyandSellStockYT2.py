#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#121. Best Time to Buy and Sell Stock
#yt solution,better and cleaner than my solution,okay solution
#https://www.youtube.com/watch?v=E2-heUEnZKU
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        size=len(prices)
        '''if size<2:
            return 0
        '''
        buy=prices[0]
        right=1
        buyindex=0
        curprofit=0
        profit=0
        sellindex=1
        while right<size:
            if buy>prices[right]:
                buy=prices[right]
                buyindex=right   
            else:
                curprofit=prices[right]-buy
                '''
                print("curprofit:")
                print(curprofit)
                print("current price:")
                print(prices[right])
                print("current buy price:")
                print(buy)
                print("")
                '''

                if curprofit>profit:

                    profit=curprofit
                    sellindex=right    
                
                
            
            right=right+1
        
        if profit>0:
            return profit
        else:
            return 0


            

        