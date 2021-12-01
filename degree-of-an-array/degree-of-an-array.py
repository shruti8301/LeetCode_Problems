class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        a = max(f.values())
        if a == 1:
            return 1
        solution = [n for n in f if f[n] == a]
        minlen=50000
        for n in solution:
            l=nums.index(n)
            r=len(nums)-nums[::-1].index(n)
            minlen=min(minlen,r-l)
        return minlen
            
        