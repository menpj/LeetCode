class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j=0

        lens=len(s)
        for i in t:
          if j<lens and s[j]==i:
              j+=1
              
        if j==len(s):
            #print("Sub sequence is present.")
            return True
            
        else:
            #print("Not present")
            return False
        
        
        
def main():
    solution= Solution()
    t=input("Enter the string: ")
    s=input("Enter the substring: ")
    solution.isSubsequence(s,t)
    
    
main()