class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr=sum(matrix,[])
        arr.sort()
        print(arr)
        return arr[k-1]