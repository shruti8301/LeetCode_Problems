from collections import Counter
class Solution:
    def greatestLetter(self, s: str) -> str:
        
        for i in reversed(ascii_uppercase):
            if i in s and i.lower() in s:
                return i
        return ""
            
            