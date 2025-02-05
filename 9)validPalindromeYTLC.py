class Solution(object):
    def isPalindrome(self,s):
        s=s.lower()
        #s=re.sub(r"[^a-z0-9]","",s)
        #length=len(s)
        
        #print(s)
        #r=""
        popCount=0
        i, popCount=len(s)-1,0
        #for i in range(length-1,(length//2)-1,-1):
        while i>popCount:    
            #print("\n")
            #if i!=popCount:
                #print(s[i])
                #print(s[popCount])
            while i>popCount and not self.isAlphaNumeric(s[i]):
                #print(f"not alphanumeric{s[i]}")
                i-=1
            while i>popCount and not self.isAlphaNumeric(s[popCount]):
                #print(f"not alphanumeric{s[popCount]}")
                popCount+=1
            #print(s[i])
            #print(s[popCount])
            if s[i]!=s[popCount]:
                #print("Not a palindrome!")
                
                return False
            popCount+=1
            i-=1
            
        #print("Its a palindrome.")
        return True
       
        #print(f"{s}")
 
    def isAlphaNumeric(self,c):
        return (ord('a')<= ord(c)<=ord('z')) or (ord('A')<= ord(c)<=ord('Z')) or (ord('0') <= ord(c) <= ord('9')) 