class Solution:
    def countCoveredBuildings(self, n, buildings):
        from collections import defaultdict
        
        ys = defaultdict(list)
        xs = defaultdict(list)
        
        
        for x, y in buildings:
            ys[y].append(x)
            xs[x].append(y)
        
      
        for y in ys:
            ys[y].sort()
        for x in xs:
            xs[x].sort()
        
        midX = set()  
        midY = set()  
        
       
        for x, arr in xs.items():
            if len(arr) >= 3:
                for i in range(1, len(arr) - 1):
                    midX.add((x, arr[i]))
        
        
        for y, arr in ys.items():
            if len(arr) >= 3:
                for i in range(1, len(arr) - 1):
                    midY.add((arr[i], y))
       
        common = sum(1 for pt in midX if pt in midY)
        return common
