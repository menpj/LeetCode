#11. Container With Most Water
#yt inspired solution, okay solution, best so far
#arrived on it based on hints in lc
#https://www.youtube.com/watch?v=6PrIRPpTI9Q
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size=len(height)
        l=0
        r=size-1
        curMax=0
        while l<r:
            
            if height[l]>height[r]:
                curMax=max((r-l)*height[r],curMax)
                r-=1
            else:
                curMax=max((r-l)*height[l],curMax)
                l+=1
        return curMax