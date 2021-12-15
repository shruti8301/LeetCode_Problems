class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr=[]
        for i in range(left,right+1):
            if i<10:
                arr.append(i)
            else:
                num=i
                while num!=0:
                    digit=num%10
                    if digit!=0 and i%digit==0:
                        num=num//10
                    else:
                        break

                if num==0:
                    arr.append(i)
        return arr   
                    