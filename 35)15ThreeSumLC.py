#15. 3Sum
#https://leetcode.com/problems/3sum/
#solution working, my solution, but time limit exceeded so not accepted in leetcode,testcases passed in lc
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        #rmCount=0
        hashMap={value:index for index,value in enumerate(nums)}
        result=[]
        size=len(nums)
        #print(nums)
        for i in range(size):
                
                
            target=0-nums[i]
            
            #print("shit1")
            for j in range(i+1,size):
                #print("shit2")
                
                curTarget=target-nums[j]
                
                if curTarget in hashMap and hashMap[curTarget]!=j and i!=j and hashMap[curTarget]!=i:
                    #print("shit3")
                    curList=[nums[i],nums[j],curTarget]
                    curList.sort()
                    if curList not in result:
                        result.append(curList)
                        
                       
        return result
        
        