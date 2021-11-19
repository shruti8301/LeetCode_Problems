class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m>n:
            m,n=n,m
        arr=[1]*m
        for i in range(1,n):
            for j in range(1,m):
                arr[j]+=arr[j-1]
        return arr[-1]
        
        