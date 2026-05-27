class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(set(candyType))
        m=len(candyType)  
        return min(m//2,n)
