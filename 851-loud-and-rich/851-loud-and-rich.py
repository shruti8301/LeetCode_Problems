class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]: 
        graph = defaultdict(list)
        degree = [0]* (len(quiet))
        ans = [-1]* (len(quiet))
    
        for i in range(len(quiet)):
            ans[i] = i
            
        for i,j in richer:
            graph[i].append(j)
            degree[j] += 1

        stack=[]
        for i in range(len(degree)):
            if degree[i] ==0:
                stack.append(i)
        
        while stack:
            a = stack.pop()
            for i in graph[a]:
                if quiet[ans[i]] > quiet[ans[a]]:
                    ans[i] = ans[a]
                degree[i] -= 1
                if degree[i] == 0:
                    stack.append(i)
        
        return ans