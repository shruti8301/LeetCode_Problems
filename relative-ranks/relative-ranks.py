class Solution:
    def findRelativeRanks(self, score):
        a=sorted(score,reverse=True)
        if len(a)==1:
            score[score.index(a[0])]='Gold Medal'
        if len(a)==2:
            score[score.index(a[0])]='Gold Medal'
            score[score.index(a[1])]='Silver Medal'    
        if len(a)==3:
            score[score.index(a[0])]='Gold Medal'
            score[score.index(a[1])]='Silver Medal'
            score[score.index(a[2])]='Bronze Medal'
        if len(a)>3:
            score[score.index(a[0])]='Gold Medal'
            score[score.index(a[1])]='Silver Medal'
            score[score.index(a[2])]='Bronze Medal'
            for i in range(3,len(a)):
                score[score.index(a[i])]=str(i+1)
        return score
        
        