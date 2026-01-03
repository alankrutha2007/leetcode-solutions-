class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for row in grid:
            for i in row:
                if(i<0):
                    c+=1
        return c
        
