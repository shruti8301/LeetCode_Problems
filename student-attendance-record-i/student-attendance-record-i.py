from collections import Counter
class Solution:
    def checkRecord(self, s: str) -> bool:
        count_a=s.count('A')
        s_l='LLL'
        if s_l not in s and count_a<2:
            return True
        else:
            return False
        
        