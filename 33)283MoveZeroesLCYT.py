#283. Move Zeroes
#https://leetcode.com/problems/move-zeroes/
#https://www.youtube.com/watch?v=aayNRwUN3Do
#YT SOLUTION, BEST SO FAR
#283. Move Zeroes
#https://leetcode.com/problems/move-zeroes/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            
        return nums