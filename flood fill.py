class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i,j,image,element,color,n,m):
            for row,col in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr=row+i
                nc=col+j
                if(nr>=0 and nr<n and nc>=0 and nc<m and element==image[nr][nc]):
                    image[nr][nc]=color
                    dfs(nr,nc,image,element,color,n,m)
        n=len(image)
        m=len(image[0])
        if(image[sr][sc]==color):
            return image
        element=image[sr][sc]
        image[sr][sc]=color
        dfs(sr,sc,image,element,color,n,m)
        return image

        
