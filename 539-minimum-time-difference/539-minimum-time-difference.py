class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        l = len(timePoints)
        for t in timePoints:
            times.append((int(t[:2])*60)+(int(t[3:])))
        times.sort()

        res = min(times[-1]-times[0], 1440-times[-1]+times[0])

        for i in range(0, l-1):
            res = min(res, min(times[i+1]-times[i], 1440-times[i+1]+times[i]))

        return res    