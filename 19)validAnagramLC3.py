#youtube inspired solution, not ideal , but best sof far
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
        for i in range(len(tcharlist)):
            if tcharlist[i] in tmap:
                tmap[tcharlist[i]]+=1
            else:
                tmap[tcharlist[i]]=1
                
            if charlist[i] in smap:
                smap[charlist[i]]+=1
            else:
                smap[charlist[i]]=1
        
        if tmap==smap:
            return True
        else:
            return False
        