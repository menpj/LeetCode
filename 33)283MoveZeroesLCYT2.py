#283. Move Zeroes
#https://leetcode.com/problems/move-zeroes/
#yt based solution
#optimal solution
#https://www.youtube.com/watch?v=k5lIW5XxC7g
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        size=len(nums)
        for r in range(size):
            if nums[r]:
                nums[l]=nums[r]
                l+=1
        while l<size:
            nums[l]=0
            l+=1
            
        return nums