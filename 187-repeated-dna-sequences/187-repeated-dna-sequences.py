class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, repeat = set(), set()
        
        n = len(s)
        
        if n < 10:
            return repeat
        
        for i in range(0, n - 9):
            seq = s[i:i+10]
            if seq in seen:
                repeat.add(seq)
            else:
                seen.add(seq)
        
        return repeat