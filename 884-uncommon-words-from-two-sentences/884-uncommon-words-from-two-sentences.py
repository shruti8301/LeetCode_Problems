from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        count=Counter(s1)
        count+=Counter(s2)
        return [a for a in count if count[a]==1]