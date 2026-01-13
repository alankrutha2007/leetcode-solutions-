class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        c=0
        i=len(bits)-2
        while(i>=0 and bits[i]==1):
            c+=1
            i-=1
        return c%2==0      
