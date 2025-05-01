#228. Summary Ranges
#https://leetcode.com/problems/summary-ranges/
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        size=len(nums)
        ranges=[]
        startIndex=0
        for i in range(size):
            try:
                if nums[i+1]!=nums[i]+1:
                    if startIndex!=i:
                        item=str(nums[startIndex])+ "->" +str(nums[i])
                    else:
                        item=str(nums[i])
                    ranges.append(item)
                    startIndex=i+1   
            except IndexError:
                if startIndex!=i:
                    #print(startIndex)
                    item=str(nums[startIndex])+ "->" +str(nums[i])
                else:
                    item=str(nums[i])
                ranges.append(item)
        return ranges
            
        