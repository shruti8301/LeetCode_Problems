class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def lcs(x,y,n,m):
            t=[[0 for i in range(m+1)] for i in range(n+1)]
            for i in range(n+1):
                for j in range(m+1):
                    if i==0 or j==0:
                        t[i][j]=0
                    elif x[i-1]==y[j-1]:
                        t[i][j]=1+t[i-1][j-1]
                    else:
                        t[i][j]=max(t[i][j-1],t[i-1][j])
            i=n
            j=m
            s=""
            while i>0 and j>0:
                if x[i-1]==y[j-1]:
                    s+=x[i-1]
                    i-=1
                    j-=1
                else:
                    if t[i][j-1]>t[i-1][j]:
                        s+=y[j-1]
                        j-=1
                    else:
                        s+=x[i-1]
                        i-=1
            while i>0:
                s+=x[i-1]
                i-=1
            while j>0:
                s+=y[j-1]
                j-=1
    
            return s[::-1]
        
        return lcs(str1,str2,len(str1),len(str2))