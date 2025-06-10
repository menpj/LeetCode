#67. Add Binary
#https://leetcode.com/problems/add-binary/
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a=int(a)
        b=int(b)
        c=0
        
        carry=0
        multiple=1
        while a>0 and b>0:
            #a1=a%2
            #b1=b%2
            sum=a%2+b%2+carry
            c=(sum%2)*multiple+c
            if sum>1:
                
                carry=1
            else:
                
                
                carry=0
            
            multiple=multiple*10
            a=a//10
            #print(a)
            b=b//10
            #print(b)
            #print("inside shit")
            
        while a>0:
            #a1=a%2
            sum=a%2+carry
            c=(sum%2)*multiple+c
            if sum>1:
                
                carry=1
            else:
                
                
                carry=0
            
            multiple=multiple*10
            a=a//10
            #print(a)
            #b=b//10
            #print(b)
            #print("inside shit")
        while b>0:
            #a1=a%2
            #a1=a%2
            #b1=b%2
            sum=b%2+carry
            c=(sum%2)*multiple+c
            if sum>1:
                #c=((a1+b1+carry)%2)*multiple+c
                carry=1
            else:
                #c=1+(10*c)
                
                carry=0
            
            multiple=multiple*10
            #a=a//10
            #print(a)
            b=b//10
            #print(b)
            #print("inside shit")
        if carry==1:
            c=carry*multiple+c
        return str(c)