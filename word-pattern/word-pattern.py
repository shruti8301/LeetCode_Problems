class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        ar=s.split(" ")
        
        if len(ar)!=len(pattern):
            return False
        if len(set(pattern)) != len(set(ar)):
            return False
        for j in range(len(ar)):
            if pattern[j] in d:
                if d[pattern[j]]!=ar[j]:
                    return False
                
            else:
                d[pattern[j]]=ar[j]
        return True
        
        