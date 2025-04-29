#128. Longest Consecutive Sequence
#https://leetcode.com/problems/longest-consecutive-sequence/
#my solution, O(n) time complexity, but taking more runtime than earlier, clean solution
#https://www.youtube.com/watch?v=P6RZZMu_maU
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        bigSequence=0
        
        
        
        hashMap= {item:index for index,item in enumerate(nums)}
        hsize=len(hashMap)
        
        
        for i in hashMap.keys():
            
            val=i
            
            curSequence=0
            while True:
                if val in hashMap:
                    if val-1 in hashMap:
                        val=val-1
                        continue
                    curSequence+=1
                    
                    hashMap.pop(val)
                    val+=1
                    
                else:
                    break
          
            if curSequence>bigSequence:
                bigSequence=curSequence
        
        return bigSequence
        
