# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        while l<=n:
            mid=(l+n)//2
            if guess(mid)==-1:
                n=mid-1
            elif guess(mid)==1:
                l=mid+1
            else:
                return mid