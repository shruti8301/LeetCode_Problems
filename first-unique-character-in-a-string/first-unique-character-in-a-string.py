class Solution:
    def firstUniqChar(self, s: str) -> int:
        li=list(s)
        a=Counter(li)
        for i in li:
            if a[i]==1:
                return s.index(i)
        return -1   
           
        