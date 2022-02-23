class Solution:
    def factorial(self,n):
        if n == 0 or n == 1:
            return 1
        else:
            fact = 1
            while(n > 1):
                fact *= n
                n -= 1
            return fact
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        c=0
        while n>=5:
            n=n//5
            c+=n
        return c
    