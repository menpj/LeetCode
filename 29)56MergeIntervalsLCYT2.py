#https://leetcode.com/problems/merge-intervals/
#56. Merge Intervals
#yt soution, optimal
#https://www.youtube.com/watch?v=IexN60k62jo
#minor performance improvement done yt video
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #size=len(intervals)
        
        intervals.sort(key= lambda i:i[0])
        
        '''if size>=1:
            interval=[intervals[0]]
        '''
        interval=[]
        for start,end in intervals:
            #interval[-1][1]
            if interval and interval[-1][1]>=start:
                
                interval[-1][1]=max(end,interval[-1][1])
            #elif lastVal<start:
            else:
                newlist=[start,end]
                interval.append(newlist) 
               
            
        return interval

        