#136. Single Number
#https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array={}
        for i in nums:
            try:
                if array[i]==None:
                    array[i]=i
            except KeyError:
                array[i]=None
        #print(array)
        for i in array:
            if array[i]==None:
                return i
            else:
                continue
        