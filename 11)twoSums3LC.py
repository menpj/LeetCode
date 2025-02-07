#167. Two Sum II - Input Array Is Sorted
#working but not very efficient
#youtubve inspired solution https://www.youtube.com/watch?v=cQ1Oz4ckceM

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index=[]
        j=len(numbers)-1
        i=0
        while  i<j:
        
            
            
            cursum=numbers[i]+numbers[j]
            
            if cursum==target:
                return [i+1,j+1]
            elif cursum<target:
                i+=1
                #print("I incremented")
            elif cursum>target:
                j-=1