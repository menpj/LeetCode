#169. Majority Element
#https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
#This is the Boyer-Moore Voting Algorithm
class Solution(object):
    def majorityElement(self,nums):
        maxCount=float('-inf')
        maxKey=None
        
        for i in nums:
            if maxKey==i:
                maxCount+=1
            elif maxKey!=i and maxCount<1:
                maxKey=i 
                maxCount=1
            elif maxKey!=i and maxCount>=1:
                maxCount-=1
            
        
        #print(f"maxvalue: {maxCount} maxkey: {maxKey}")
        return maxKey


        
            
        
        
def main():
    solution=Solution()
    solution.majorityElement([3,2,3])

main()