class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=0
        #l=2
        #listND=[]
        #print(f"First Iteration: \nval: {val}")
        for n in nums:   
            if r<2 or n!=nums[r-2]:
                nums[r] = n
                r+=1
            
                                
            
            #print(f"after iteration {  nums}")

        
          
            

        

            
        
                
        
                
        #print(nums)
        #print(f"counter: {r}")
        return r