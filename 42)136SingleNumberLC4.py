#136. Single Number
#https://leetcode.com/problems/single-number/
#YouTube inspired solution , ideal solution
#https://www.youtube.com/watch?v=qMPX1AOa83k
#136. Single Number
#https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for i in nums:
            
            res=i^res
        #print(array)
        return res
        