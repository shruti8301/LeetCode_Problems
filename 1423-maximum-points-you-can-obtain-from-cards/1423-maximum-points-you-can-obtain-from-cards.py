class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        tot=sum(cardPoints)
        rem_len=len(cardPoints)-k
        subarr=sum(cardPoints[:rem_len])
        mina=subarr
        for i in range(rem_len,len(cardPoints)):
            subarr+=cardPoints[i]
            subarr-=cardPoints[i-rem_len]
            mina=min(mina,subarr)
        return tot-mina