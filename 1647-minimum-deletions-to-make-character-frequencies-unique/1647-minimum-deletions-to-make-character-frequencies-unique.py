from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        d=Counter(s)
        arr=set()
        c=0
        for i,j in d.items():
            while j>0 and j in arr:
                j-=1
                c+=1
            arr.add(j)
        return c
        
        
        '''
        sorted_tuples = sorted(d.items(), key=lambda item: item[1])
        print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
        sorted_dict = {k: v for k, v in sorted_tuples}

        print(sorted_dict)  #
        for i in range(26):
            while sorted_dict[i]!=0 and sorted_dict[i] in arr:
                sorted_dict[i]-=1
                c+=1
            else:
                arr.add(sorted_dict[i])
        print(arr)
        return(c)
        '''