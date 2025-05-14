#11. Container With Most Water
#my solution, okay solution, best so far
#arrived on it based on hints in lc
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
            cur=(r-l)*min(height[l],height[r])
            curMax=max(cur,curMax)
            
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return curMax