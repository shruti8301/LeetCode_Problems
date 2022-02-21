class Solution:
	def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

		intervals.sort()
		i=0
		while i<len(intervals)-1:

				a,b = intervals[i]
				p,q = intervals[i+1]

				if a <= p and q <= b:
					intervals.remove(intervals[i+1])
					i-=1

				elif p <= a and b <= q:
					intervals.remove(intervals[i])
					i-=1

				i+=1
		return len(intervals)