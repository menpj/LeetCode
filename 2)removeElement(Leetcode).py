class Solution(object):
    def removeElement(self, nums, val):
        
        
        
        counter=len(nums)
       
        i=0
        while(i<len(nums)):
            
            if nums[i]==val:
                
                
                counter=counter-1
                for j in range(i+1,len(nums)):
                    nums[j-1]=nums[j]
                nums[counter]=-999
                i=i-1
                
            
            i+=1    
                    
        
       
        return counter