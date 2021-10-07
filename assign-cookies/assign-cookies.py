class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        c=0
        for i in s:
            if c>=len(g):
                return c
            if i>=g[c]:
                c+=1
        return c

        