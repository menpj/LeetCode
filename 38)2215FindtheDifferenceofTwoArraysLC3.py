#2215. Find the Difference of Two Arrays
#https://leetcode.com/problems/find-the-difference-of-two-arrays/
#MY SOLUTION,best so far

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        N1={ value:index for index,value in enumerate(nums1)}
        N2={ value:index for index,value in enumerate(nums2)}
        result=[[],[]]
        #print(N1)
        #print(N2)
        for i in N1:
            if i not in N2:
                
                result[0].append(i)
        for i in N2:
            if i not in N1:
                result[1].append(i)
        #result=[list(N1),list(N2)]
        return result