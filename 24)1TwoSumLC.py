#1. Two Sum
#https://leetcode.com/problems/two-sum/
#My Solution Not idealm solution, o(n^2)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size=len(nums)
        i=0
        while i<size:
            k=i+1
            while k<size:
                if (nums[i]+nums[k])==target:
                    return [i,k]
                k+=1
            i+=1 
        