class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr=[]
        for i in ops:
            if i=="+":
                arr.append(int(arr[-1])+int(arr[-2]))
            elif i=="D":
                arr.append(2*arr[-1])
            elif i=="C":
                arr.pop()
            else:
                arr.append(int(i))
        return sum(arr)