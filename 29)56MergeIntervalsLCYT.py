#https://leetcode.com/problems/merge-intervals/
#56. Merge Intervals
#my soution, not optimal
#https://www.youtube.com/watch?v=44H3cEC2fFM
#minor performance improvement done yt video
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        size=len(intervals)
        sub=1
        intervals.sort(key= lambda i:i[0])
        
        if size>=1:
            interval=[intervals[0]]
        
        
        for start,end in intervals[1:]:
            lastVal=interval[-1][1]
            if lastVal>=start and lastVal<=end:
                
                interval[-1][1]=end
            elif lastVal<start:
                newlist=[start,end]
                interval.append(newlist) 
               
            
        return interval

        