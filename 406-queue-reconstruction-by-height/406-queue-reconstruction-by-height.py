class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda person: (-person[0], person[1]))
        ans = []
        for person in people:
            ans.insert(person[1], person)
        return ans


'''
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key= lambda x:(-x[0],x[1]))
        arr=[]
        for i in people:
            arr.insert(i[1],i)
            print(arr)
        return arr
        
'''