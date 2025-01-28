class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print(f"initial array {nums}")
        
        counter=len(nums)
        print("length of nums: ",counter)
        i=0
        while(i<len(nums)):
            print(i)
            if nums[i]==val:
                print(f"same value detected at {i}")
                
                counter=counter-1
                for j in range(i+1,len(nums)):
                    nums[j-1]=nums[j]
                nums[counter]=-999
                i=i-1
                
            print(nums)
            i+=1    
                    
        
        print(f"final array {nums} ")
        print(f"length of nums: {counter}")
        return counter
        
        
        
        
def main():
    solution=Solution()
    solution.removeElement([2,3,2,3,2,2,3],2)
 
main()