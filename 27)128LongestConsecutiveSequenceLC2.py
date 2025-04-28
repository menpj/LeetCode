#128. Longest Consecutive Sequence
#https://leetcode.com/problems/longest-consecutive-sequence/
#my solution, not good solution 
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        #print(nums)
        bigSequence=1
        curSequence=1
        size=len(nums)
        if size==0:
            return 0
        for i in range(size-1):
            if (nums[i]+1)==nums[i+1]:
                curSequence+=1
            elif nums[i+1]==nums[i]:
                pass
            else:
                '''if curSequence>bigSequence:
                    bigSequence=curSequence'''
                
                '''if curSequence>bigSequence:
                    bigSequence=curSequence'''
                    #print(bigSequence)
                curSequence=1
                #print(bigSequence)
            if curSequence>bigSequence:
                    bigSequence=curSequence
        '''if curSequence>bigSequence:
                    bigSequence=curSequence
                    #print(bigSequence)  '''
        return bigSequence