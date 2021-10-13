class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = {'q','w','e','r','t','y','u','i','o','p'}
        second= {'a','s','d','f','g','h','j','k','l'}
        third = {'z','x','c','v','b','n','m'}
        arr=[]
       
        for i in words:
            
            if set(i.lower())-first==set():
                arr.append(i)
            elif set(i.lower())-second==set():
                arr.append(i)
            elif set(i.lower())-third==set():
                arr.append(i)
        return arr
            
            
        