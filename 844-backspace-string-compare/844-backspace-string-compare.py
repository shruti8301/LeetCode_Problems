class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            a=[]
            for i in s:
                if i!='#':
                    a.append(i)
                elif a:
                    a.pop()
            return "".join(a)
        return build(s)==build(t)