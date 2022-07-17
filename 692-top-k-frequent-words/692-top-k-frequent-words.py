from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=Counter(sorted(words))
        d=dict(sorted(d.items(),key=lambda x: -x[1]))
        return list(d.keys())[0:k]