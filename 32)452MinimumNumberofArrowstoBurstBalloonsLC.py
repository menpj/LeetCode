#452. Minimum Number of Arrows to Burst Balloons
#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """ 
        points.sort(key=lambda i:i[0])
        #points.sort()
        #points.sort(key=lambda i: (i[0], i[1]))
        #print(points)
        if not points:
            return 0
        count=1
        prevend=points[0][1]
        for  start,end in points:
            if start>prevend:
                #print("oola")
                #print(str(start)+":"+str(end))
                count+=1
                prevend=end
            elif end<prevend:
                prevend=end

        return count


        