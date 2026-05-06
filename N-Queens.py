class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def canWePlace(row,col,mat):
                r,c=row,col #Top
                while(r>=0):
                    if(mat[r][c]=="Q"):
                        return False
                    r-=1
                r,c=row,col #Top-left
                while(r>=0 and c>=0):
                    if(mat[r][c]=="Q"):
                        return False
                    r-=1
                    c-=1
                r,c=row,col #Top-right
                while(r>=0 and c<n):
                    if(mat[r][c]=="Q"):
                        return False
                    r-=1
                    c+=1
                return True
        def generate(row,col,n,ans):
            if(row==n):
                temp=[]
                for r in mat:
                    temp.append(''.join(r))
                ans.append(temp)
                return
            for col in range(0,n):
                if(canWePlace(row,col,mat)):
                    mat[row][col]="Q"
                    generate(row+1,mat,n,ans)
                    mat[row][col]='.'
            return
        mat=[]
        for _ in range(n):
            lst=['.']*n
            mat.append(lst)
        ans=[]
        row=0
        generate(row,mat,n,ans)
        return ans
