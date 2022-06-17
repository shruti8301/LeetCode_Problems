class Solution:
	def scheduleCourse(self, courses: List[List[int]]) -> int:
		# Time O(nlogn), Space(O(n))
		courses.sort(key=lambda x:x[1])
		pq = []
		time = 0

		for start,end in courses:
			heappush(pq, -start)
			time += start
			if time > end:
				time += heappop(pq)

		return len(pq)