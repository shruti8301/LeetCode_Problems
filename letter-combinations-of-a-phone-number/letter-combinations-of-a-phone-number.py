class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        
        result=[]
        
        if len(digits)==0:
            return []
        
        def mapping(i,s):
            if len(s)==len(digits):
                result.append(s)
                return 
            for j in comb[digits[i]]:
                mapping(i+1,s+j)
        mapping(0,"")
        return result
                
                
                
                
        
        