class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(row,col,grid,visit,n,m):
            for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr=r+row
                nc=c+col
                if(nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]==1 and visit[nr][nc]==0 ):
                    visit[nr][nc]=1
                    dfs(nr,nc,grid,visit,n,m)
        n=len(grid)
        m=len(grid[0])
        visit=[]
        for i in range(n):
            lst=[0]*m
            visit.append(lst)
        for row in range(n):
            for col in range(m):
                if((row==0 or row==n-1 or col==0 or col==m-1) and grid[row][col]==1 and visit[row][col]==0):
                    visit[row][col]=1
                    dfs(row,col,grid,visit,n,m)
        count=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1 and visit[i][j]==0):
                    count+=1
        return count

        
