#my soution working soution but not accepeted in lc
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        k=k%size
        
        nums=nums[size-k:]+nums[:size-k]
        print("nums is:")
        print(nums)

        '''if nums:
            for i in range(k):
                
            
                
                temp=nums[0]
                for k in range(size):

                    temp2=nums[(k+1)%size]
                    nums[(k+1)%size]=temp
                    temp=temp2
            

        #print(nums)'''