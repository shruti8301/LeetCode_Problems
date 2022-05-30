class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count=0
        for i in arr:
            if i==0:
                count+=1     
        for i in arr:
            if i in arr and i*2 in arr and i!=0:
                return True
            elif i==0 and count>1:
                return True    
        return False