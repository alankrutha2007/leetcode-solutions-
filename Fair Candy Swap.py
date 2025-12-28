class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        x=sum(aliceSizes)
        y=sum(bobSizes)
        z=(y-x)//2
        for i in aliceSizes:
            j=i+z
            if j in bobSizes:
                return [i,j] 
