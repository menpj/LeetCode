#219. Contains Duplicate II
#https://leetcode.com/problems/contains-duplicate-ii/
#yt soution, not ideal
#https://youtube.com/shorts/sKP7LDqKqqM

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        size=len(nums)
        mapDict={}
        for i in range(size):
            if nums[i] in mapDict and abs(mapDict[nums[i]]-i)<=k:
                return True
            else:
                mapDict[nums[i]]=i
                #print(mapDict)
        
        return False
        