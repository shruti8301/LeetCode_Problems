class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=version1.split(".")
        version2=version2.split(".")
        i=0
        j=0
        while (i<len(version1) or j <len(version2)):
            v1=int(version1[i]) if i<len(version1) else 0
            v2=int(version2[i]) if i<len(version2) else 0
            if v1<v2:
                return -1
            elif v1>v2:
                return 1
            i+=1
            j+=1
        return 0
       
        
        
        
        
        