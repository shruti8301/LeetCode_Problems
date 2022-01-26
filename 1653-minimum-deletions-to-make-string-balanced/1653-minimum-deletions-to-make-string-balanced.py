class Solution:
    def minimumDeletions(self, s: str) -> int:
        a=s.count('a')
        b=0
        r=a+b
        for i in s:
            if i=='a':
                a-=1
            else:
                b+=1
            r=min(r,a+b)
        return r