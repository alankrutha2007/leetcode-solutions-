class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c=0
        n=high-low+1  
        if n%2==0:
            c+=n//2
        else:
            if low%2!=0 or high%2!=0:
                c+=(n//2+1)
            else:
                c+=n//2
        return c
