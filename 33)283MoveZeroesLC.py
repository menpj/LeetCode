#283. Move Zeroes
#https://leetcode.com/problems/move-zeroes/
#MY SOLUTION,NOT CLEAN , OKAY ONE
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroP=0
        nonZP=0
        size=len(nums)
        #while zeroP<size and nonZP<size:
        while True:
            while zeroP<size and nums[zeroP]!=0:
                zeroP+=1
            while nonZP<size and nums[nonZP]==0:
                nonZP+=1
            if zeroP<size and nonZP<size:
                if nonZP>zeroP:
                    nums[zeroP]=nums[nonZP]
                    nums[nonZP]=0
                    nonZP+=1
                    zeroP+=1
                else:
                    nonZP+=1
            else:
                break
        #print(nums)
        return nums