class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1==word2:
            return 0
        t=[[0 for i in range(len(word2)+1)] for i in range(len(word1)+1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i==0 or j==0:
                    t[i][j]=0
                elif word1[i-1]==word2[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i][j-1],t[i-1][j])
        return len(word1)+len(word2)-2*t[-1][-1]