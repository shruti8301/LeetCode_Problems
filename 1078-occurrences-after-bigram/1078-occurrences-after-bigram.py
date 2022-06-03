class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text=text.split(" ")
        arr=[]
        for i in range(len(text)):
            if text[i]==first:
                if i+1<len(text):
                    if text[i+1]==second:
                        if i+2<len(text):
                            arr.append(text[i+2])
        return arr