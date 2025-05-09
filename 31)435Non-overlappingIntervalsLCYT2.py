#435. Non-overlapping Intervals
#https://leetcode.com/problems/non-overlapping-intervals/
#YT solution, not optimal
#https://www.youtube.com/watch?v=nONCGxWoUfM
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key= lambda i:i[0])
        #intervals.sort()
        #print("Sorted: ")
        #print(intervals)
        interval=intervals[0][1]
        count=0
        for start,end in intervals[1:]:
            #interval[-1][1]
            if interval>start:
                count+=1
                #lastInterval=interval[-1][1]-min(interval[-1][0],start)
                #curInterval=end-min(interval[-1][0],start)
                
                '''if lastInterval>curInterval:
                    interval[-1]=[start,end]'''
                '''if lastInterval>curInterval:
                    interval[-1]=[start,end]'''
                if end<interval:
                    interval=end
                    #print(start)
                    #print(end)
                    #print("hey here")
                    #print(interval[-1])
                #interval[-1][1]=max(end,interval[-1][1])
            #elif lastVal<start:
            else:
                
                interval=end 
        #print("Output Interval:")     
        #print(interval)
        return count
        