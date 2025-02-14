#383. Ransom Note
#https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
#hashmap  based solution not ideal
#yoututbe based soution
#https://www.youtube.com/watch?v=i3bvxJyUB40
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        map=defaultdict(int)
        for c in magazine:
            map[c]+=1
          
        #map=Counter(magazine)
        
        for i in ransomNote:
            if i not in map:
                return False

            elif map[i]>1:
                map[i]-=1
            else:
                del map[i]
            
                #print(i)
                #print(map)
                
        return True