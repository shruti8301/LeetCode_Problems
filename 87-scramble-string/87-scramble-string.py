class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def f(a, b):
            if a == b:
                return True
    
            if len(a) == 1:
                return False
            
            if len(a) != len(b):
                return False
            
            for i in range(1, len(a)):
                # no swap
                if f(a[:i], b[:i]) and f(a[i:], b[i:]):
                    return True
                
                # swap
                if f(a[:i], b[-i:]) and f(a[i:], b[:len(a)-i]):
                    return True
            return False
        
        return f(s1, s2)