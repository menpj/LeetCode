#125. Valid Palindrome
#https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
#not an ideal solution
import re

class Solution(object):
    def isPalindrome(self,s):
        s=re.sub(r"[^a-zA-Z0-9]","",s)
        length=len(s)
        s=s.lower()
        r=""
        for i in range(length-1,-1,-1):
            r+=s[i]
            
        print(f"r:{r}")
        if r==s:
            
            print("Its a palindrome.")
            return True
        else:
            print("Not a palindromez")
            return False
        #print(f"{s}")
    
    
def main():
    solution=Solution()
    s = input("Enter a string:")
    solution.isPalindrome(s)
    
    
main()