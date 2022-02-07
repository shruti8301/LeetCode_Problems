class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if(len(s1) + len(s2) != len(s3)):
            return False
        
        t=[[False for i in range(len(s2)+1)]for i in range(len(s1)+1)]
        
        t[0][0] = True
        
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if(i > 0):
                    t[i][j] = (t[i - 1][j] and (s1[i - 1] == s3[i + j - 1])) or t[i][j]
                if(j > 0):
                    t[i][j] = (t[i][j - 1] and (s2[j - 1] == s3[i + j - 1])) or t[i][j]

                    
        return t[-1][-1]