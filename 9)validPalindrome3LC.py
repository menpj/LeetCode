#another variant of validPalindrome2LC.py
from re import sub
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=sub(r"[^a-z0-9]","",s)
        length=len(s)
        #print(s)
        #r=""
        popCount=0
        for i in range(length-1,-1,-1):
            
            if i!=popCount:
                #print(s[i])
                #print(s[popCount])
                if s[i]!=s[popCount]:
                    #print("Not a palindrome!")
                    
                    return False
                popCount+=1
            else:
                break
            
        #print("Its a palindrome.")
        return True