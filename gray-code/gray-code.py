class Solution:
    def grayCode(self, n: int) -> List[int]:
        result=[0]
        for i in range(1,n+1):
            result+=[2**(i-1)+j for j in result[::-1]]
        return result
        