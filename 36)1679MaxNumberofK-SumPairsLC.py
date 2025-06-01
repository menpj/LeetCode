#https://leetcode.com/problems/max-number-of-k-sum-pairs/
#MY SOLUTION, OKAY SOLUTION, NOT IDEAL
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size=len(nums)
        left=0
        right=size-1
        nums.sort()
        count=0
        while left<right:
            val=nums[left]+nums[right]
            '''print("value")
            print(val)
            print(hashMap)
            print("left")
            print(left)
            print("right")
            print(right)
            print(" ")'''
            if k>val:
                left+=1
            elif k<val:
                right-=1
            else:
                
                count+=1
                left+=1
                right-=1
        return count