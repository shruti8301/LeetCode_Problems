class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr=[]
        def backtrack(a=[],l=0,r=0):
            if len(a)==2*n:
                arr.append("".join(a))
                return 
            if l<n:
                a.append("(")
                backtrack(a,l+1,r)
                a.pop()
            if r<l:
                a.append(")")
                backtrack(a,l,r+1)
                a.pop()
        backtrack()
        return arr
        