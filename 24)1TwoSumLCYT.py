#1. Two Sum
#https://leetcode.com/problems/two-sum/
#YT Solution, oPTIMAL solution , bets so far
#https://www.youtube.com/watch?v=KLlXCFG5TnA

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict={}
        for index, item in enumerate(nums):
            value=target-item
            if value in numsDict:
                return [numsDict[value],index]
            
            numsDict[item]=index


                
            