class Solution:
    def arrangeCoins(self, n: int) -> int:
        r=1
        count=0
        while(n>=r):
            n-=r
            r+=1
            count+=1
        return count
        
