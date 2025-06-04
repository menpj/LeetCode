#2215. Find the Difference of Two Arrays
#https://leetcode.com/problems/find-the-difference-of-two-arrays/
#MY SOLUTION,not ideal solution
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        result=[[],[]]
        for i in nums1:
            if i not in nums2 and i not in result[0]:
                result[0].append(i)

        for i in nums2:
            if i not in nums1 and i not in result[1]:
                result[1].append(i)
        
        return result