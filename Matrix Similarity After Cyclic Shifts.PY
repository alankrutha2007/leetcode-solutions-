
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            shift = k % n
            
            for j in range(n):
                if i % 2 == 0:
                    # Even row: shift left
                    if mat[i][j] != mat[i][(j + shift) % n]:
                        return False
                else:
                    # Odd row: shift right
                    if mat[i][j] != mat[i][(j - shift) % n]:
                        return False
        
        return True

        
