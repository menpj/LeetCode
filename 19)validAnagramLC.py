#mysoution not ideal
#https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150
#242. Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charlist=list(s)
        tcharlist=list(t)
        #print(tcharlist)
        popcount=0
        for i in range(len(tcharlist)):
            #print(i-popcount)
            
            if tcharlist[i-popcount] in charlist:
                #print(i)
                

                charlist.remove(tcharlist[i-popcount])
                tcharlist.pop(i-popcount)
                popcount+=1
                #print(magazine)
            else:
                #print("executed1")
                return False
                  
                #print(magazine)
        if charlist or tcharlist: 
            #print("executed2")
            #print(charlist)
            #print(tcharlist)
            return  False
        else:
            return True
        