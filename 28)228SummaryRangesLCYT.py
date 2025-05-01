#228. Summary Ranges
#https://leetcode.com/problems/summary-ranges/
#https://www.youtube.com/watch?v=ZHJDwbfqoa8

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        size=len(nums)
        ranges=[]
        #startIndex=0
        i=0
        while i<size:
            startIndex=i
            while i<size-1 and nums[i+1]==nums[i]+1:
                i+=1

            
            if startIndex!=i:
                item=str(nums[startIndex])+ "->" +str(nums[i])
            else:
                item=str(nums[i])
            ranges.append(item)
            #startIndex=i+1   
            i+=1
            
        return ranges
            
        