class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        c=1
        for i in range(1,int(sqrt(area))+1):
            if area%i==0: c=i
        return [area//c,c]

            
        