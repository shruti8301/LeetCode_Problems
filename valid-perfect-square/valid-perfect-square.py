class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        l=1
        r=num
        while l<=r:
            mid=(l+r)//2
            if mid*mid>num:
                r=mid-1
            elif mid*mid==num:
                return True
            else:
                l=mid+1
        return False
           