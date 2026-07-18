class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #sorted by start time 

        temp_intervals = []
        i = 0
        n = len(intervals)

        
        while i < n and intervals[i][1] < newInterval[0]:
            temp_intervals.append(intervals[i])
            i += 1
        # new_s, new_e = -1, -1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0],newInterval[0] )
            newInterval[1] = max(intervals[i][1],newInterval[1] )
            i += 1
        temp_intervals.append(newInterval)
        while i < n:
            temp_intervals.append(intervals[i])
            i += 1

        return temp_intervals
        
            

        