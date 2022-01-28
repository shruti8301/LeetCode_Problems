class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        A=sum(aliceSizes)
        B=sum(bobSizes)
        setb=set(bobSizes)
        for i in aliceSizes:
            if i + (B-A)/2 in setb:
                return [i,i+(B-A)/2 ]