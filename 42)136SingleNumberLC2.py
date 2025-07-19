#136. Single Number
#https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        while i<len(nums):
            if i==len(nums)-1 or nums[i]!=nums[i+1]:
                return nums[i]
            else:
            #if nums[i]==nums[i+1]:
                i=i+2
            '''else:
                return nums[i]'''
        #print(array)
       
        