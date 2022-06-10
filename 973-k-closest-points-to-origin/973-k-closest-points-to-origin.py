import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[]
        a=[]
        for i in range(len(points)):
            distance.append([sqrt(points[i][0]**2 + points[i][1]**2),points[i]])
        print(distance)
        heapify(distance)
        for i in range(len(distance)):
            a.append(distance[0])
            heappop(distance)
        print(a)
        return [a[i][1] for i in range(k)]