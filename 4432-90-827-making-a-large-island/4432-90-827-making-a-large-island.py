class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        curr = 0
        vis = set()
        mapp = {}
        size = {}
        
        def inbound(i,j):
            return 0<=i<n and 0<=j<n
        
        def dfs(i,j,num):
            vis.add((i,j))
            mapp[(i,j)] = num
            added = 0
            for ii,jj in dir:
                ni = i+ii
                nj = j+jj
                if (ni,nj) not in vis:
                    vis.add((ni,nj))
                    if  inbound(ni,nj) and grid[ni][nj] == 1:
                        added+=1
                        added += dfs(ni,nj,num)
            return added
        
        num = 0
        for i in range(n):
            for j in range(n):
                if (i,j) not in vis and grid[i][j] == 1:
                    size[num] = dfs(i,j,num) + 1
                    num+=1
        

        f = False
        for i in range(n):
            for j in range(n):
                cur = 1
                if grid[i][j] == 0:
                    f = True
                    viss = set()
                    for ii,jj in dir:
                        if inbound(i+ii,j+jj):
                            if grid[ii+i][j+jj] == 1:
                                mapi = mapp[(i+ii,j+jj)]
                                if mapi not in viss:
                                    viss.add(mapi)
                                    cur+=size[mapi]
                ans = max(ans,cur)
        if f:
            return ans
        return n*n
        
    
        
        



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def dfs(i,j):
        #     added = 0
        #     for ii,jj in dir:
        #         ni = i+ii
        #         nj = j+jj
        #         if (ni,nj) not in vis:
        #             vis.add((ni,nj))
        #             if  inbound(ni,nj) and grid[ni][nj] == 1:
        #                 added+=1
        #                 added += dfs(ni,nj)
        #     return added



        # 

        

        