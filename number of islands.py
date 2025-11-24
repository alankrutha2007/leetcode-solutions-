class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j,grid,visit,n,m):
            for row,col in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr=i+row#nr=new_row
                nc=j+col#nc=new_col
                if(nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]=="1" and visit[nr][nc]==0):
                    visit[nr][nc]=1
                    dfs(nr,nc,grid,visit,n,m)
        n=len(grid)#matrix name as grid,no of rows
        m=len(grid[0])#no of columns
        visit =[]
        for i in range(n):
            lst=[0]*m
            visit.append(lst)
        count=0
        for i in range(0,n):
            for j in range(0,m):
                if(grid[i][j]=='1' and visit[i][j]==0):
                    visit[i][j]=1
                    dfs(i,j,grid,visit,n,m)
                    count+=1
        return count

                

                
