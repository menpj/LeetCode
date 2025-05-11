#452. Minimum Number of Arrows to Burst Balloons
#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
#YT INSPIRED SOLUTION,OPTIMAL SOLUTION
#https://www.youtube.com/watch?v=fvBhjAp0j9c
class Solution(object):
    def findMinArrowShots(self, points):
        '''if not points:
            return 0 '''
        #ABOVE PART IS OPTIONAL
        points.sort(key=lambda i:i[1])
        count=1
        prevend=points[0][1]
        for  start,end in points[1:]:
            if start>prevend:
                count+=1
                prevend=end
        return count


        