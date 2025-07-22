#youtube BAsed solution, okay solution, not ideal
#https://leetcode.com/problems/counting-bits/
#338. Counting Bits 
#https://www.youtube.com/watch?v=RyBM56RIWrM
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #ans={}
        #ans[0]=0
        ans=[0]*(n+1)
        
        #print(ans[0])
        k=1
        for i in range(1,n+1):
            #print(i/2)
            '''if i%2==0:
                ans.append(ans[i/2])
            else:
                ans.append(ans[i/2]+1)'''
            if k*2==i:
                k=k*2
            ans[i]=ans[i-k]+1
        #print(ans)
        return ans