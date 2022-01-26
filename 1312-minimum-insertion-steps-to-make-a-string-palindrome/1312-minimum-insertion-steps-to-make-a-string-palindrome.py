class Solution:
    def minInsertions(self, s: str) -> int:
        def lcs(x,y,n,m):
            if x==y:
                return 0
            else:
                t=[[0 for i in range (m+1)] for i in range (n+1)]
                for i in range(n+1):
                    for j in range(m+1):
                        if i==0 or j==0:
                            t[i][j] = 0
                        elif x[i-1]==y[j-1]:
                            t[i][j]=1+t[i-1][j-1]
                        else:
                            t[i][j]=max(t[i][j-1],t[i-1][j])
                return (len(s)-t[-1][-1])
        return lcs(s,s[::-1],len(s),len(s))
            