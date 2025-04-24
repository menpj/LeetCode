#1. Two Sum
#https://leetcode.com/problems/two-sum/
#My Solution, okay solution , bets so far

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size=len(nums)
        numsDict={ item:index for index, item in enumerate(nums) }
        #print(numsDict)
        i=0
        while i<size:
            
             
            
            value=target-nums[i]
            #print(value)
            try:
                if numsDict[value]!=i:
                    return [i,numsDict[value]]
            except KeyError:
                pass
                
            i+=1 