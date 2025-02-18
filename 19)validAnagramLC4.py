#youtube base solutuion  not ideal
#https://www.youtube.com/watch?v=9UtInBqnCgA
#https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150
#242. Valid Anagram
class Solution(object):
    def isAnagram(self, charlist, tcharlist):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #charlist=s
        #tcharlist=t
        #print(tcharlist)
        slen=len(charlist)
        tlen=len(tcharlist)
        
        if slen!=tlen:
            return False
        smap = {}
        tmap = {}
        for i in range(tlen):
            
            tmap[tcharlist[i]]=1+tmap.get(tcharlist[i],0)
                
            
            smap[charlist[i]]=1+smap.get(charlist[i],0)
        
        if tmap==smap:
            return True
        else:
            return False
        