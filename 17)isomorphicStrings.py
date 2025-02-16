#205. Isomorphic Strings
#https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
#my solution, ideal soultion
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
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
        
        
def main():
    solution= Solution()
    s=input("Enter string 1:")
    t=input("Enter string 2:")
    bool=solution.isIsomorphic(s,t)
    if bool:
        print("Strings are isomorphic.")
    else:
        print("Strign are not isomorphic.")
main()