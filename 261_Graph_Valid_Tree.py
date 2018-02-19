class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges)!=n-1:
            return False
        neighbors={i:[] for i in range(n)}
        for x,y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)
        self.visit(0,neighbors)
        return len(neighbors)==0
    
    def visit(self,i,neighbors):
        temp=neighbors.pop(i)
        for n in temp:
            if n in neighbors:
                self.visit(n,neighbors)