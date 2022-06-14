class Solution:
    def eventualSafeNodes(self, graphs: List[List[int]]) -> List[int]:
        
        d=collections.defaultdict(list)
        for i in range(len(graphs)):
            for j in graphs[i]:
                d[j].append(i)
        lst_no_dep=[i for i in range(len(graphs)) if len(graphs[i])==0]
        stack=[]
        while lst_no_dep:
            a=lst_no_dep.pop()
            stack.append(a)
            for i in d[a]:
                #degree[i]-=1
                graphs[i].remove(a)
                if len(graphs[i])==0:
                    lst_no_dep.append(i)
        #if len(stack)!=len(graphs):
           # return []
        stack.sort()
        return stack