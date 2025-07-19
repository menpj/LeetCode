
#136. Single Number
#https://leetcode.com/problems/single-number/
#YouTube inspired solution , using extra space
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array=set()
        for i in nums:
            
            if i in array:
                array.remove(i)
            else:
                array.add(i)
        #print(array)
        for i in array:
            return i
        