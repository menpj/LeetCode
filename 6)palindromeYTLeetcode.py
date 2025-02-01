#9. Palindrome Number
#https://leetcode.com/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150
#https://www.youtube.com/watch?v=yubRKwixN-U inspired from this video but solution is not ideal
#solution is not ideal
class Solution(object):
    def isPalindrome(self, temp):
        """
        :type x: int
        :rtype: bool
        """
        if temp<0:
            #print(f"{num} is not a Palindrome")
            return False
        #temp=num
        #length= len(str(temp))
        length =1
        while temp>=length*10:
            length*=10
        i=0
        
        #while temp>0 and length>1:
        while temp:
            if temp%10 == temp//length:
                #temp=temp%(10**length-1)
                temp=(temp%length)//10
            
                
                length=length//100
                #print(f"After iteration {temp} length: {length}")
            else:
                #print(f"{num} is not a Palindrome")
                return False
            
        
        
            
        #print(f"{num} is a Palindrome")
        return True