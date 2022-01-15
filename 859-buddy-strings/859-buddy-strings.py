class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        
        comparisson = [i for i in range(len(s)) if s[i]!=goal[i]]
        
        if len(comparisson) > 2:
            return False
        if len(comparisson) == 2 and s[comparisson[0]]==goal[comparisson[1]] and s[comparisson[1]]==goal[comparisson[0]]: 
            return True
        if len(comparisson) == 0 and len(s) > len(set(list(s))): #check if there are duplicate characters for swap
            return True