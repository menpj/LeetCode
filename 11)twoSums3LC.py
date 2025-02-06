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
        
            
            
            
            
            if (numbers[i]+numbers[j])==target:
                index.append(i+1)
                index.append(j+1)
                #print(index)
                #print("index")
                
                return index
            elif (numbers[i]+numbers[j])<target:
                i+=1
                #print("I incremented")
            elif (numbers[i]+numbers[j])>target:
                j-=1