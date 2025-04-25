#1. Two Sum
#https://leetcode.com/problems/two-sum/
#YT Solution, oPTIMAL solution
#https://www.youtube.com/watch?v=UXDSeD9mN-k
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


        size= len(nums)
        left=0
        right=size
        while left!=right:
            curval=nums[left]+nums[right] 
            if  curval==target:
                return [left,right]
            elif curval<target:
                left=left+1
            elif curval>target:
                right=right-1