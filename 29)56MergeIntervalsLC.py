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
        
        
        while sub<size:
            lastVal=interval[-1][1]
            if lastVal>=intervals[sub][0] and lastVal<=intervals[sub][1]:
                
                interval[-1][1]=intervals[sub][1]
            elif lastVal<intervals[sub][0]:
                newlist=[intervals[sub][0],intervals[sub][1]]
                interval.append(newlist) 
               
            sub=sub+1
        return interval

        