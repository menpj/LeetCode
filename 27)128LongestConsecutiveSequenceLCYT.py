#128. Longest Consecutive Sequence
#https://leetcode.com/problems/longest-consecutive-sequence/
#https://www.youtube.com/watch?v=P6RZZMu_maU
#yt solution, clean solution, best so far
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bigSequence=0
        hashMap= set(nums)
        for val in hashMap:
            if val-1 not in hashMap:
                curSequence=0
                while val+curSequence in hashMap:
                    curSequence+=1        
                bigSequence=max(curSequence,bigSequence)    
        return bigSequence
        
