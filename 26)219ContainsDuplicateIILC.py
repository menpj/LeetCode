#219. Contains Duplicate II
#https://leetcode.com/problems/contains-duplicate-ii/
#my soution, not ideal, best so far
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapDict={}
        for index,item in enumerate(nums):
            if item in mapDict and abs(mapDict[item]-index)<=k:
                return True
            else:
                mapDict[item]=index
                #print(mapDict)
        
        return False
        