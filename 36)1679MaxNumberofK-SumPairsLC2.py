#https://leetcode.com/problems/max-number-of-k-sum-pairs/
#yt inspired SOLUTION, OKAY SOLUTION, best so far
#https://www.youtube.com/watch?v=FevSHchkCeo

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        hashMap={}
        for _,value in enumerate(nums):
            hashMap[value]=hashMap.get(value,0)+1  
        for key,qty in hashMap.items():
            target=k-key
            if target in hashMap:
               
                if target!=key:
                    count+=min(hashMap[key],hashMap[target])
                else:
                    count+=(hashMap[key]/2)//1
                del hashMap[key]
                '''if key!=target:
                    del hashMap[target]'''
        return count
        