#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#122. Best Time to Buy and Sell Stock II
#my solution,optimal solution
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
        rightadvanced=2
        #buyindex=0
        curprofit=0
        profit=0
        total_profit=0
        #sellindex=1
        if size==2:
            profit=prices[right]-buy
        while right<size:
            if buy>prices[right]:
                buy=prices[right]
                #buyindex=right   
            else:
                curprofit=prices[right]-buy
                if rightadvanced<size and prices[rightadvanced]<prices[right] and curprofit>0:
                    total_profit+=curprofit
                    buy=prices[rightadvanced]
                    #buyindex=rightadvanced
                    profit=0
                    right=right+1
                    rightadvanced=rightadvanced+1
                    continue
                    
                
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
                    #sellindex=right    
                
                
            
            right=right+1
            rightadvanced=rightadvanced+1
        total_profit=profit+total_profit
        if total_profit>0:
            return total_profit
        else:
            return 0


            

#1 3 8 10 11