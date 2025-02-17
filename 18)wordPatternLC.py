#290. Word Pattern
#https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150
#my solution, ideal solution

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s=s.split()
        t=pattern
        len1=len(s)
        len2=len(t)
        if not len1==len2:
            return False
        map ={}
        for i in range(len2):
            if s[i] in map:
                temp=map[s[i]]
                if t[i]==temp:
                    continue
                else:
                    return False
            elif t[i] in map.values():
                #print("executed")
                return False
            elif t[i] not in map.values():
                map[s[i]]=t[i]
                
            
        return True
        