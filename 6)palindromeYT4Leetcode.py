class Solution(object):
    def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """
        if num == 0:
            #print(f"{num} is a Palindrome")
            return True
        elif num<0 or num%10==0:
            #print(f"{num} is not a Palindrome")
            return False
        temp=num
        reversed=0
        #length= len(str(temp))
        
        while temp>reversed:
            reversed=(reversed*10)+(temp%10)
            temp=temp//10
            
        if temp==reversed or temp==reversed//10:
            #print(f"{num} is a Palindrome")
            return True
        else:
            #print(f"{num} is not a Palindrome")
            return False