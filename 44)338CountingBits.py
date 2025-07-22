#my youtube absed solution, okay solution, not ideal
#https://leetcode.com/problems/counting-bits/
#338. Counting Bits 
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #ans={}
        #ans[0]=0
        ans=list()
        ans.append(0)
        #print(ans[0])
        for i in range(1,n+1):
            #print(i/2)
            if i%2==0:
                ans.append(ans[i/2])
            else:
                ans.append(ans[i/2]+1)
        #print(ans)
        return ans