#https://www.youtube.com/watch?v=5Km3utixwZs
#yt based solution , ideal solution
#https://leetcode.com/problems/number-of-1-bits/
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count=0
        while n:
            count+=1
            n=n&(n-1)
            #print(n)

        #print(count)
        return count
        #n=int(n,2)
        #print(n)
        