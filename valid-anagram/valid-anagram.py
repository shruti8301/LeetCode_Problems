class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        if(len(s)!=len(t)):
            return False
        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for j in t:
            if j in d2:
                d2[j]+=1
            else:
                d2[j]=1
                
        if(d1==d2):
            return True
        else:
            return False
                
                
            
           
        