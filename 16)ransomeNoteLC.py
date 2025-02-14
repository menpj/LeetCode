#383. Ransom Note
#https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
#my solution not ideal
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:
            if i in magazine:
                magazine=magazine.replace(i,'',1)
                #print(magazine)
            else:
                return False
        return True
        