#57. Insert Interval
#https://leetcode.com/problems/insert-interval/
#my solution optimal solution
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        flag=False
        interval=[]
        '''if not intervals:
            interval=[newInterval]'''
        if not newInterval:
            return intervals
        for start,end in intervals:
            #interval[-1][1]
            if not flag:
                if newInterval[0]<=start and newInterval[1]>=start:
                #if newnewInterval[1]>=start:
                    newList=[newInterval[0],max(newInterval[1],end)]
                    
                    interval.append(newList)
                    flag=True
                    '''if newInterval[1]<start:
                        flag=True
                        continue'''
                elif newInterval[0]<start and newInterval[1]<start:
                    interval.append(newInterval)
                    #print("entered")
                    #print(newInterval)
                    interval.append([start,end])
                    flag=True
                    continue
                elif newInterval[0]>start and newInterval[0]<=end:
                    
                    newList=[start,max(newInterval[1],end)]
                    interval.append(newList)
                    flag=True
                    continue
                else:
                    interval.append([start,end])
            else:
                #print("entered")

                if interval and interval[-1][1]>=start:
                    
                    interval[-1][1]=max(end,interval[-1][1])
                #elif lastVal<start:
                else:
                    newList=[start,end]
                    interval.append(newList) 
            

        if not flag:
            interval.append(newInterval) 
            
            
        return interval
        