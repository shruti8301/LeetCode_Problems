class Solution:
	def scheduleCourse(self, courses: List[List[int]]) -> int:
		# Time O(nlogn), Space(O(n))
		courses.sort(key=lambda x:x[1])
		arr = []
		time = 0

		for i,j in courses:
			heappush(arr, -i)
			time += i
			if time > j:
				time += heappop(arr)

		return len(arr)