
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        dict1 = dict()
        
        for u, v, w in edges:
            uf.union(u, v)
        
        for u,v,w in edges:
            pu = uf.find(u)
            pv = uf.find(v)

            if pu == pv:
                if pu in dict1:
                    dict1[pu] &= w
                else:
                    dict1[pu] = w
        
        ans = []
        for u,v in queries:
            pu = uf.find(u)
            pv = uf.find(v)

            if pu == pv:
                ans.append(dict1[pu])
            else:
                ans.append(-1)
        return ans

            



        
        
