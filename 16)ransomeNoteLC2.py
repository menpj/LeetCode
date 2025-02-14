#383. Ransom Note
#https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
#not ideal solution nnbut best so far
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        charlist=list(magazine)
        for i in ransomNote:
             
            
            if i in charlist:
                charlist.remove(i)
                
                #print(magazine)
            else:
                return False
                  
                #print(magazine)
            
        return True
        