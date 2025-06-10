#67. Add Binary
#https://leetcode.com/problems/add-binary/
#YT BASED solution, best so far
#https://www.youtube.com/watch?v=keuWJ47xG8g
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a=a[::-1]
        b=b[::-1]
        c=""
        
        carry=0
        #multiple=1
        sizeA=len(a)
        sizeB=len(b)
        i=0
        while i<max(sizeA,sizeB):
            a1=int(a[i]) if i<sizeA else 0
            b1=int(b[i]) if i<sizeB else 0
            #b1=b%2
            sum=a1+b1+carry
            c=str(sum%2)+c
            if sum>1:
                carry=1
            else:
                carry=0
            #carry=sum//2
            i+=1
           
        if carry:
            c="1"+c
        return c