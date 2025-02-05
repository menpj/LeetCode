#125. Valid Palindrome
#https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
#not ideal but okay solution
import re

class Solution(object):
    def isPalindrome(self,s):
        s=s.lower()
        s=re.sub(r"[^a-z0-9]","",s)
        length=len(s)
        
        print(s)
        #r=""
        popCount=0
        for i in range(length-1,(length//2)-1,-1):
            
            if i!=popCount:
                print(s[i])
                print(s[popCount])
                if s[i]!=s[popCount]:
                    print("Not a palindrome!")
                    
                    return False
                popCount+=1
      
            
        print("Its a palindrome.")
        return True
       
        #print(f"{s}")
    
    
def main():
    solution=Solution()
    s = input("Enter a string:")
    solution.isPalindrome(s)
    
    
main()