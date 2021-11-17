class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        start=intervals[0][0]
        end=intervals[0][1]
        arr=[]
        i=1
        while i<len(intervals):
            if intervals[i][0]<=end:
                end=max(end,intervals[i][1])
            else:
                arr.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
            i+=1
        arr.append([start,end])
        return arr
        