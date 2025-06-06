#2215. Find the Difference of Two Arrays
#https://leetcode.com/problems/find-the-difference-of-two-arrays/
#MY SOLUTION, okay solution, yt inspired
#https://www.youtube.com/watch?v=a4wqKR-znBE

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        #N1=set(nums1)
        #N2=set(nums2)
        N1={ value for value in nums1}
        N2={ value for value in nums2}
        #print(N1)
        #print(N2)
        result=[[],[]]
        
        for i in N1:
            if i not in N2:
                
                result[0].append(i)
        for i in N2:
            if i not in N1:
                result[1].append(i)
        #result=[list(N1),list(N2)]
        return result