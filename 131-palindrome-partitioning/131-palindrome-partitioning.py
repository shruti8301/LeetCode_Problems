class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s)==0:
            return [[]]
        def check(result,arr,s):
            if len(s)==0:
                result.append(list(arr))
                return
            for i in range(1,len(s)+1):
                if s[:i]==s[:i][::-1]:
                    check(result,arr+[s[:i]],s[i:])
        result=[]
        check(result,[],s)
        return result
                