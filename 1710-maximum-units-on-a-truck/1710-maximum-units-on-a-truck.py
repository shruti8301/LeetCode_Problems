class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes=sorted(boxTypes,key=lambda x:-x[1])
        a=0
        for i in range(len(boxTypes)):
            
            if boxTypes[i][0]<truckSize and truckSize!=0:
                a+=boxTypes[i][0]*boxTypes[i][1]
                truckSize-=boxTypes[i][0]
            else:
                a+=(truckSize)*boxTypes[i][1]
                truckSize-=truckSize
        return (a)
            