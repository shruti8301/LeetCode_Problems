class Solution:
    def twoEggDrop(self, n: int) -> int:
        t=[[-1 for i in range(n+1)]for i in range(3)]
        return self.solve(2,n,t)
    
    def solve(self,e,f,t):
       
        if e==1 or f==0 or f==1:
            return f
        mn=float('inf')
        if t[e][f]!=-1:
            return t[e][f]
        low=0
        high=f
        while low<=high:
            mid=(low+high)//2
            left=self.solve(e-1,mid-1,t)
            right=self.solve(e,f-mid,t)
            temp=1+max(left,right)
            if left<right:
                low=mid+1
            else:
                high=mid-1
            mn=min(mn,temp)
            t[e][f]=mn
        return t[e][f]
    
                