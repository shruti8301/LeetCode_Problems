
class Disjoint_PCO:
    def __init__(self, n_cities):
        self.root = [i for i in range(n_cities)]  # tells the root node for each node, initially itself
        self.rank = [1]*n_cities # rank/height of each node
    
    # find the root of a node x
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x]) # find root-of(root-of (x)) until you meet the highest
        return self.root[x]
    
    # when joining 2 nodes, we assign their roots on the basis of rank of their roots
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rooty] > self.rank[rootx]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
    
    # whether 2 nodes are connected or not
    def connected(self, x, y):
        return self.find(x) == self.find(y)
        
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dpco_obj = Disjoint_PCO(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    dpco_obj.union(i, j)
        
        # need to do this to ensure all have their highest parent assigned to them
        for i in range(len(isConnected)):
            dpco_obj.root[i] = dpco_obj.find(i)
            
        return len(set(dpco_obj.root))