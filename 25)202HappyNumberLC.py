#202. Happy Number
#https://leetcode.com/problems/happy-number/
#my solution, optimal solution
#logic = Cycle Detection: If a number is not happy, it will fall into a repeating cycle that does not include 1. For example, numbers like 4, 16, 37, etc., are part of such cycles.
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cycleMap={}
        while n not in cycleMap:
            digitsum=0
            cycleMap[n]=0
            while n:
                curval=n%10
                digitsum+=curval*curval
                n=n/10
            if digitsum==1:
                return True
            n=digitsum
        return False
            
