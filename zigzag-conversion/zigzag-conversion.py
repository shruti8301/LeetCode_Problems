class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        result=[""]*numRows
        index=0
        direction='down'
        for i in s:
            result[index]+=i
            if direction=='down':
                index+=1
                if index==numRows:
                    direction='up'
                    index-=1
            if direction=='up':
                index-=1
                if index<0:
                    direction='down'
                    index=1
        return ''.join(result)