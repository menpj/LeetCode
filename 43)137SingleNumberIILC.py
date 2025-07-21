#137. Single Number II
#https://leetcode.com/problems/single-number-ii/
#MY SOLUTION, works but not as per requireemnts, extra memory used, CONSTANT MEMORY SOLUTION IS REQUIRED
#required solution is with bitwise operations
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array={}
        for i in nums:
            try:
                if array[i]:
                    array[i]+=1
            except KeyError:
                array[i]=1
        #print(array)
        for i in array:
            if array[i]==1:
                return i
            
        