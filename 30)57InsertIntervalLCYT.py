#57. Insert Interval
#https://leetcode.com/problems/insert-interval/
#yt solution,cleaner optimal solution,better simpler logic
#https://www.youtube.com/watch?v=A8NUOmlwOlM

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        interval=[]
        if not newInterval:
            return intervals
        for i in range(len(intervals)):
            
                if newInterval[1]<intervals[i][0]:
                    interval.append(newInterval)
                    return interval+intervals[i:]

                elif newInterval[0]>intervals[i][1]:
                    interval.append(intervals[i])

                else: #newInterval[0]<=intervals[i][1]:
                    newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])] 
    
        interval.append(newInterval)        
        return interval
        