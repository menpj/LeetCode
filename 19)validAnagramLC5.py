#https://www.youtube.com/watch?v=IRN1VcA8CGc
#youtube base solutuion  not ideal
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
        map = {}
        #map = {}
        for i in range(tlen):
            
            map[tcharlist[i]]=1+map.get(tcharlist[i],0)
                
            
            map[charlist[i]]=map.get(charlist[i],0)-1
        
        for key in map:
            if map[key]!=0:
                return False
        return True
        