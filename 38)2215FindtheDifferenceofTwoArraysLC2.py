#2215. Find the Difference of Two Arrays
#https://leetcode.com/problems/find-the-difference-of-two-arrays/
#MY SOLUTION,not ideal solution, best so far

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        N1=set()
        N2=set()
        for i in nums1:
            if i not in nums2:
                
                N1.add(i)
        for i in nums2:
            if i not in nums1:
                
                N2.add(i)
        result=[list(N1),list(N2)]
        return result