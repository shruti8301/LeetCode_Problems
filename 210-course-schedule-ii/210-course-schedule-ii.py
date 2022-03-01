class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree={i:0 for i in range(numCourses)}
        graph=collections.defaultdict(list)
        for j,i in prerequisites:
            graph[i].append(j)
            degree[j]+=1
        lst_no_dep=[i for i in range(numCourses) if degree[i]==0]
        stack=[]
        while lst_no_dep:
            a=lst_no_dep.pop()
            stack.append(a)
            for i in graph[a]:
                degree[i]-=1
                if degree[i]==0:
                    lst_no_dep.append(i)
        if len(stack)!=numCourses:
            return []
        return stack