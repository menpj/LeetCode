#https://leetcode.com/problems/3sum/
#yt based solution, not optimal, but best so far, slight improvement over previous
#https://www.youtube.com/watch?v=jzZsG8n2R9A
#https://www.youtube.com/watch?v=DhFh8Kw7ymk
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        

        size=len(nums)
        result=[]
        nums.sort()
        
        for i in range(size):
            
            
            if i>0 and nums[i-1]==nums[i]:
                continue
            left=i+1
            right=size-1
        
            while left<right:
                
                curval=nums[i]+nums[left]+nums[right] 
                
                
                

                    
                  
                if curval<0:
                    
                    left=left+1
                    
                elif curval>0:
                    
                    
                    right=right-1

                elif  curval==0:
                    curList=[nums[i],nums[left],nums[right]]
                    result.append(curList)
                    left+=1
                    right-=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    while nums[right]==nums[right+1] and left<right:
                        right-=1
                
                 
        return result
        
        