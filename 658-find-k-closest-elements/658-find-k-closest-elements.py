import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff=[]
        a=[]
        for i in range(len(arr)):
            diff.append([abs(arr[i]-x),arr[i]])
        print(diff)
        heapify(diff)
        for i in range(len(diff)):
            a.append(diff[0])
            heappop(diff)
        print(a)
        return sorted([a[i][1] for i in range(k)])