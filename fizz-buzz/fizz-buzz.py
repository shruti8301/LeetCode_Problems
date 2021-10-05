class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr=[]
        s=["FizzBuzz","Fizz","Buzz"]
        for i in range(1,n+1):
            if i%3==0 or i%5==0:
                if i%3==0 and i%5==0:
                    arr.append(s[0])
                elif i%3==0:
                    arr.append(s[1])
                else:
                    arr.append(s[2])
            else:
                arr.append(str(i))
                
        return arr

            