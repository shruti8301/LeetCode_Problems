class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c=0
        last=float("-inf")
        for i in range(len(intervals)):
            if intervals[i][0]<last:
                c+=1
                last=min(last,intervals[i][1])
            else:
                last=intervals[i][1]
        return c
            