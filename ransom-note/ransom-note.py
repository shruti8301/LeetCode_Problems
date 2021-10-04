class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        li=list(ransomNote)
        li1=list(magazine)
        for i in li:
            if i in li1:
                li1.remove(i)
            else:
                return False
        return True