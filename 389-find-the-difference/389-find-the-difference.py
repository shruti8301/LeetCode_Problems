class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_s=0
        s_t=0
        for i in s:
            s_s+=ord(i)
        for j in t:
            s_t+=ord(j)
        return chr(abs(s_t-s_s))