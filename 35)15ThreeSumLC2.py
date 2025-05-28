#15. 3Sum
#https://leetcode.com/problems/3sum/
#solution working, my solution, accepted in leetcode,but not at all optimal soution

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        hashMap={}
        
        size=len(nums)
        result=[]
        
        for i in range(size):
            
            target=0-nums[i]
            
            for j in range(i+1,size):
                curTarget=target-nums[j]
                if curTarget in hashMap and i!=hashMap[curTarget] and j!=hashMap[curTarget]:
                    curList=[nums[i],nums[j],curTarget]
                    curList.sort()
                    if curList not in result:
                        result.append(curList)
            hashMap[nums[i]]=i
                


        
        
                 
        return result
        
        