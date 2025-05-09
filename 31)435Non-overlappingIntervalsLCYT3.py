#435. Non-overlapping Intervals
#https://leetcode.com/problems/non-overlapping-intervals/
#YT solution, optimal solution,clean solution
#https://www.youtube.com/watch?v=HDHQ8lAWakY

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #interval is prevEnd
        intervals.sort(key= lambda i:i[1])
        
        interval=intervals[0][1]
        count=1
        for start,end in intervals[1:]:
            
            if start>=interval:
                count+=1
              
                interval=end
                   
        return (len(intervals)-count)
        