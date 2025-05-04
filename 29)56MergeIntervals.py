#https://leetcode.com/problems/merge-intervals/
#56. Merge Intervals
#my soution, not optimal
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        size=len(intervals)
        sub=1
        intervals.sort()
        
        if size>=1:
            interval=[intervals[0]]
        
        
        while sub<size:
           
            if interval[len(interval)-1][1]>=intervals[sub][0] and interval[len(interval)-1][1]<=intervals[sub][1]:
                
                interval[len(interval)-1][1]=intervals[sub][1]
            elif interval[len(interval)-1][1]<intervals[sub][0]:
                newlist=[intervals[sub][0],intervals[sub][1]]
                interval.append(newlist) 
               
            sub=sub+1
        return interval

        